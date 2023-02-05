class FileReadCache:

    def __init__(self):
        self.cache = {}

    def read_content(self, file_path: str, offset: int, length: int) -> str:
        if file_path not in self.cache:
            self.cache[file_path] = open(file_path, 'r')

        self.cache[file_path].seek(offset)
        return self.cache[file_path].read(length)

    def close_file(self, file_path: str):
        if file_path not in self.cache:
            return
        self.cache[file_path].close()
        self.cache.pop(file_path, None)


file_read_cache = FileReadCache()
