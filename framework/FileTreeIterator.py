import os


class FileTreeIterator:

    def __init__(self, path: str):
        self.path = os.path.abspath(path)

    def iterate_files(self):
        print("Iterating files in path: " + self.path)
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.endswith(".swift"):
                    yield os.path.join(root, file)
