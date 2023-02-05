import argparse
import asyncio
import sys

from framework.ChangesWriter import ChangesWriter
from framework.FileReadCache import file_read_cache
from framework.FileTreeIterator import FileTreeIterator
from framework.SourceKittenExecutor import SourceKittenExecutor
from framework.SwiftLintObject import SwiftLintObject
from rule.AddLogToErrorClosureRule import AddLogToErrorClosureRule


def collect_value_from_whole_json(json_object, key):
    if isinstance(json_object, dict):
        for k, v in json_object.items():
            if k == key:
                yield v
            else:
                yield from collect_value_from_whole_json(v, key)
    elif isinstance(json_object, list):
        for item in json_object:
            yield from collect_value_from_whole_json(item, key)


files_count_done = 0


async def iterate_file(file_path):
    global files_count_done

    visitor = AddLogToErrorClosureRule()
    swift_structure_result = await source_kitten.execute_async(file_path)
    root = SwiftLintObject(swift_structure_result, file_path, None)
    visitor.visit(root)
    file_read_cache.close_file(file_path)

    if len(visitor.changes) > 0:
        changes_writer.write(visitor.changes, file_path)

    files_count_done += 1
    print("Files done: " + str(files_count_done))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Lint Swift files'
    )
    parser.add_argument(
        '--path',
        help='Path to Swift files',
        required=True
    )
    args = parser.parse_args()
    source_kitten = SourceKittenExecutor()
    source_kitten.check_source_kitten_installed()

    iterate = FileTreeIterator(args.path).iterate_files()

    print("Files to process: " + str(len(list(iterate))))

    changes_writer = ChangesWriter()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(*[iterate_file(file_path) for file_path in iterate]))
    loop.close()

    # print(set(list(collect_value_from_whole_json(response_json, 'key.kind'))))
