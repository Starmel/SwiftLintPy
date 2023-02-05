import asyncio
import json
import subprocess
import sys


class SourceKittenExecutor:

    def check_source_kitten_installed(self):
        process = subprocess.run(['which', 'sourcekitten'], stdout=subprocess.PIPE)
        installed = process.returncode == 0
        if not installed:
            print('SourceKitten is not installed. Please install it from brew:\nbrew install sourcekitten')
            sys.exit(1)

    async def execute_async(self, file_path: str) -> dict:
        process = await asyncio.create_subprocess_exec('sourcekitten', 'structure', '--file', file_path,
                                                       stdout=asyncio.subprocess.PIPE)
        stdout, stderr = await process.communicate()
        return json.loads(stdout.decode('utf-8'))
