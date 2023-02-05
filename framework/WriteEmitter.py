from abc import ABC, abstractmethod

from framework.SwiftLintObject import SwiftLintObject


# Fix diffraction between SourceKit result offsets and python string offsets
def count_non_ascii_characters(string: str):
    count = 0
    for char in string:
        if ord(char) > 127:
            count += 1
    return count


class ContentAction(ABC):

    def __init__(self, swift_lint_object: SwiftLintObject, offset: int):
        self.swift_lint_object = swift_lint_object
        self.offset = offset

    def apply(self, content: str) -> str:
        utf8_offset = self.offset - count_non_ascii_characters(content[:self.offset])
        return self.apply_utf8(content, utf8_offset)

    @abstractmethod
    def apply_utf8(self, content: str, utf8_offset: int) -> str:
        pass


class WriteContentAction(ContentAction):

    def __init__(self, swift_lint_object: SwiftLintObject, offset: int, content: str):
        super().__init__(swift_lint_object, offset)
        self.swift_lint_object = swift_lint_object
        self.offset = offset
        self.content = content

    def apply_utf8(self, content: str, utf8_offset) -> str:
        content = content[:utf8_offset] + self.content + content[utf8_offset:]
        return content

    def __str__(self):
        return "WriteEmitterChange(offset: " + str(self.offset) + ", content: " + self.content + ")"


class ReplaceContentAction(ContentAction):

    def __init__(self, swift_lint_object: SwiftLintObject, offset: int, length: int, content: str):
        super().__init__(swift_lint_object, offset)
        self.length = length
        self.swift_lint_object = swift_lint_object
        self.offset = offset
        self.content = content

    def apply_utf8(self, content: str, utf8_offset: int) -> str:
        content = content[:utf8_offset] + content[utf8_offset + self.length:]
        content = content[:utf8_offset] + self.content + content[utf8_offset:]
        return content

    def __str__(self):
        return "ReplaceEmitterChange(offset: " + str(self.offset) + ", length: " + str(
            self.length) + ", content: " + self.content + ")"


class WriteEmitter:

    def __init__(self):
        self.changes = []

    def insert(self, swift_lint_object: SwiftLintObject, offset: int, content: str):
        self.changes.append(WriteContentAction(swift_lint_object, offset, content))

    def replace(self, swift_lint_object: SwiftLintObject, offset: int, length: int, content: str):
        self.changes.append(ReplaceContentAction(swift_lint_object, offset, length, content))
