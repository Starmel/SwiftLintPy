from abc import ABC

from framework.SwiftLintObject import SwiftLintObject


class SwiftLintObjectVisitor(ABC):

    def visit(self, swift_lint_object: SwiftLintObject):

        kind = swift_lint_object.getKind()

        if kind == 'source.lang.swift.decl.function.method.instance':
            self.visitFunction(swift_lint_object)
        elif kind == 'source.lang.swift.stmt.if':
            self.visitIf(swift_lint_object)
        elif kind == 'source.lang.swift.stmt.guard':
            self.visitGuard(swift_lint_object)
        elif kind == 'source.lang.swift.structure.elem.typeref':
            self.visitTypeRef(swift_lint_object)
        elif kind == 'source.lang.swift.decl.class':
            self.visitClass(swift_lint_object)
        elif kind == 'source.lang.swift.stmt.switch':
            self.visitSwitch(swift_lint_object)
        elif kind == 'source.lang.swift.decl.enumcase':
            self.visitEnumCase(swift_lint_object)
        elif kind == 'source.lang.swift.decl.protocol':
            self.visitProtocol(swift_lint_object)
        elif kind == 'source.lang.swift.decl.var.instance':
            self.visitInstanceVariable(swift_lint_object)
        elif kind == 'source.lang.swift.expr.array':
            self.visitArray(swift_lint_object)
        elif kind == 'source.lang.swift.stmt.foreach':
            self.visitForEach(swift_lint_object)
        elif kind == 'source.lang.swift.decl.enumelement':
            self.visitEnumElement(swift_lint_object)
        elif kind == 'source.lang.swift.structure.elem.condition_expr':
            self.visitConditionExpr(swift_lint_object)
        elif kind == 'source.lang.swift.decl.var.local':
            self.visitLocalVariable(swift_lint_object)
        elif kind == 'source.lang.swift.decl.var.parameter':
            self.visitParameter(swift_lint_object)
        elif kind == 'source.lang.swift.syntaxtype.comment.mark':
            self.visitCommentMark(swift_lint_object)
        elif kind == 'source.lang.swift.structure.elem.expr':
            self.visitExpr(swift_lint_object)
        elif kind == 'source.lang.swift.decl.extension':
            self.visitExtension(swift_lint_object)
        elif kind == 'source.lang.swift.stmt.case':
            self.visitCase(swift_lint_object)
        elif kind == 'source.lang.swift.expr.call':
            self.visitCall(swift_lint_object)
        elif kind == 'source.lang.swift.structure.elem.id':
            self.visitId(swift_lint_object)
        elif kind == 'source.lang.swift.decl.enum':
            self.visitEnum(swift_lint_object)
        elif kind == 'source.lang.swift.expr.closure':
            self.visitClosure(swift_lint_object)
        elif kind == 'source.lang.swift.structure.elem.pattern':
            self.visitPattern(swift_lint_object)
        elif kind == 'source.lang.swift.expr.argument':
            self.visitArgument(swift_lint_object)
        elif kind == 'source.lang.swift.stmt.brace':
            self.visitBrace(swift_lint_object)

        for substructure in swift_lint_object.getSubstructure():
            self.visit(substructure)

    def visitFunction(self, swift_lint_object: SwiftLintObject):
        pass

    def visitIf(self, swift_lint_object: SwiftLintObject):
        pass

    def visitGuard(self, swift_lint_object: SwiftLintObject):
        pass

    def visitTypeRef(self, swift_lint_object: SwiftLintObject):
        pass

    def visitClass(self, swift_lint_object: SwiftLintObject):
        pass

    def visitSwitch(self, swift_lint_object: SwiftLintObject):
        pass

    def visitEnumCase(self, swift_lint_object: SwiftLintObject):
        pass

    def visitProtocol(self, swift_lint_object: SwiftLintObject):
        pass

    def visitInstanceVariable(self, swift_lint_object: SwiftLintObject):
        pass

    def visitArray(self, swift_lint_object: SwiftLintObject):
        pass

    def visitForEach(self, swift_lint_object: SwiftLintObject):
        pass

    def visitEnumElement(self, swift_lint_object: SwiftLintObject):
        pass

    def visitConditionExpr(self, swift_lint_object: SwiftLintObject):
        pass

    def visitLocalVariable(self, swift_lint_object: SwiftLintObject):
        pass

    def visitParameter(self, swift_lint_object: SwiftLintObject):
        pass

    def visitCommentMark(self, swift_lint_object: SwiftLintObject):
        pass

    def visitExpr(self, swift_lint_object: SwiftLintObject):
        pass

    def visitExtension(self, swift_lint_object: SwiftLintObject):
        pass

    def visitCase(self, swift_lint_object: SwiftLintObject):
        pass

    def visitCall(self, swift_lint_object: SwiftLintObject):
        pass

    def visitId(self, swift_lint_object: SwiftLintObject):
        pass

    def visitEnum(self, swift_lint_object: SwiftLintObject):
        pass

    def visitClosure(self, swift_lint_object: SwiftLintObject):
        pass

    def visitPattern(self, swift_lint_object: SwiftLintObject):
        pass

    def visitArgument(self, swift_lint_object: SwiftLintObject):
        pass

    def visitBrace(self, swift_lint_object: SwiftLintObject):
        pass
