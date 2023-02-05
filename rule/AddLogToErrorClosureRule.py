from framework.SwiftLintObject import SwiftLintObject
from framework.SwiftLintObjectVisitor import SwiftLintObjectVisitor
from framework.WriteEmitter import WriteEmitter


class AddLogToErrorClosureRule(SwiftLintObjectVisitor, WriteEmitter):

    def visitArgument(self, swift_lint_object: SwiftLintObject):
        if swift_lint_object.getName() == "onError":
            closure: SwiftLintObject = swift_lint_object.child_clousures()[0]
            braces: SwiftLintObject = closure.child_braces()[0]
            parameter = closure.child_parameters()[0]

            if not braces.has_call("Vital.log"):

                if parameter.read_content() == "_":
                    self.replace(swift_lint_object, parameter.getOffset(), parameter.getLength(), "error")

                braces_content = braces.read_content()
                parameter_in_index = braces_content.find("in") + 2 + braces.getOffset()

                whitespaces = 0
                for char in braces_content[braces_content.find("in") + 3:]:
                    if char == "\t":
                        whitespaces += 4
                    elif char == "\n":
                        continue
                    if char == " ":
                        whitespaces += 1
                    else:
                        # print("breaking at char: " + char)
                        break

                containing_type = swift_lint_object.containing_type().getName()
                containing_function = swift_lint_object.containing_function().getName().split("(")[0]
                padding_string = " " * whitespaces

                self.insert(braces, parameter_in_index,
                            "\n" + padding_string + "Vital.log(\"" + containing_type + "." + containing_function + "\", error)\n")
