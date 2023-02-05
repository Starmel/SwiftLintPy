from framework.WriteEmitter import ContentAction


class ChangesWriter:

    def write(self, changes: list[ContentAction], file_path: str):

        changes.sort(key=lambda change: change.offset, reverse=True)

        with open(file_path, 'r') as file:
            file_content = file.read()

            for change in changes:
                change.apply(file_content)

        # print(file_content)
        with open(file_path, 'w') as file:
            file.write(file_content)
