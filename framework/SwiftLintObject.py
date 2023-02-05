class SwiftLintObject:

    def __init__(self, data, file_path, parent):
        self.data = data
        self.file_path = file_path
        self.parent = parent

    # Custom methods

    def read_content(self) -> str:
        from framework.FileReadCache import file_read_cache
        content = file_read_cache.read_content(self.file_path, self.getOffset(), self.getLength())
        return content

    # region containing methods
    def containing_function(self) -> 'SwiftLintObject':
        if self.getKind() == 'source.lang.swift.decl.function.method.instance':
            return self
        elif self.parent is None:
            return None
        else:
            return self.parent.containing_function()

    def containing_class(self) -> 'SwiftLintObject':
        if self.getKind() == 'source.lang.swift.decl.class':
            return self
        elif self.parent is None:
            return None
        else:
            return self.parent.containing_class()

    def containing_struct(self) -> 'SwiftLintObject':
        if self.getKind() == 'source.lang.swift.decl.struct':
            return self
        elif self.parent is None:
            return None
        else:
            return self.parent.containing_struct()

    def containing_enum(self) -> 'SwiftLintObject':
        if self.getKind() == 'source.lang.swift.decl.enum':
            return self
        elif self.parent is None:
            return None
        else:
            return self.parent.containing_enum()

    def containing_protocol(self) -> 'SwiftLintObject':
        if self.getKind() == 'source.lang.swift.decl.protocol':
            return self
        elif self.parent is None:
            return None
        else:
            return self.parent.containing_protocol()

    def containing_extension(self) -> 'SwiftLintObject':
        if self.getKind() == 'source.lang.swift.decl.extension':
            return self
        elif self.parent is None:
            return None
        else:
            return self.parent.containing_extension()

    def containing_type(self) -> 'SwiftLintObject':
        if self.getKind() == 'source.lang.swift.decl.class' or \
                self.getKind() == 'source.lang.swift.decl.struct' or \
                self.getKind() == 'source.lang.swift.decl.enum' or \
                self.getKind() == 'source.lang.swift.decl.protocol' or \
                self.getKind() == 'source.lang.swift.decl.extension':
            return self
        elif self.parent is None:
            return None
        else:
            return self.parent.containing_type()

    # endregion

    # region child type methods

    def child_clousures(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.expr.closure', self.getSubstructure()))

    def child_functions(self) -> list:
        return list(
            filter(lambda x: x.getKind() == 'source.lang.swift.decl.function.method.instance', self.getSubstructure()))

    def child_classes(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.class', self.getSubstructure()))

    def child_structs(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.struct', self.getSubstructure()))

    def child_enums(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.enum', self.getSubstructure()))

    def child_protocols(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.protocol', self.getSubstructure()))

    def child_extensions(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.extension', self.getSubstructure()))

    def child_types(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.class' or
                                     x.getKind() == 'source.lang.swift.decl.struct' or
                                     x.getKind() == 'source.lang.swift.decl.enum' or
                                     x.getKind() == 'source.lang.swift.decl.protocol' or
                                     x.getKind() == 'source.lang.swift.decl.extension', self.getSubstructure()))

    def child_variables(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.var.instance', self.getSubstructure()))

    def child_constants(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.var.global', self.getSubstructure()))

    def child_properties(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.var.instance' or
                                     x.getKind() == 'source.lang.swift.decl.var.global', self.getSubstructure()))

    def child_variables_and_constants(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.var.instance' or
                                     x.getKind() == 'source.lang.swift.decl.var.global', self.getSubstructure()))

    def child_variables_and_constants_and_properties(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.var.instance' or
                                     x.getKind() == 'source.lang.swift.decl.var.global', self.getSubstructure()))

    def child_parameters(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.decl.var.parameter', self.getSubstructure()))

    def child_braces(self) -> list:
        return list(filter(lambda x: x.getKind() == 'source.lang.swift.stmt.brace', self.getSubstructure()))

    # endregion

    # region Has checks

    def has_call(self, name: str) -> bool:
        return len(list(filter(lambda x: x.getKind() == 'source.lang.swift.expr.call' and x.getName() == name,
                               self.getSubstructure()))) > 0

    # endregion

    # Generated methods

    # region Generated methods
    def getAnnotatedDeclaration(self) -> str:
        return self.data.get('key.annotated_decl')

    def getBodyLength(self) -> int:
        return self.data.get('key.bodylength')

    def getBodyOffset(self) -> int:
        return self.data.get('key.bodyoffset')

    def getDiagnosticStage(self) -> str:
        return self.data.get('key.diagnostic_stage')

    def getElements(self) -> list:
        # map self.data.get('key.elements') to SwiftLintObject
        objects = map(lambda x: SwiftLintObject(x, self.file_path, self), self.data.get('key.elements'))
        return list(objects)

    def getFilePath(self) -> str:
        return self.data.get('key.filepath')

    def getFullXMLDocs(self) -> str:
        return self.data.get('key.doc.full_as_xml')

    def getKind(self) -> str:
        return self.data.get('key.kind')

    def getLength(self) -> int:
        return self.data.get('key.length')

    def getName(self) -> str:
        return self.data.get('key.name')

    def getNameLength(self) -> int:
        return self.data.get('key.namelength')

    def getNameOffset(self) -> int:
        return self.data.get('key.nameoffset')

    def getOffset(self) -> int:
        return self.data.get('key.offset')

    def getSubstructure(self) -> list:

        is_exist = self.data.get('key.substructure') is not None

        if is_exist:
            swift_lint_objects = map(lambda x: SwiftLintObject(x, self.file_path, self),
                                     self.data.get('key.substructure'))
            return list(swift_lint_objects)
        else:
            return []

    def getSyntaxMap(self) -> str:
        return self.data.get('key.syntaxmap')

    def getTypeName(self) -> str:
        return self.data.get('key.typename')

    def getInheritedTypes(self) -> list:
        return self.data.get('key.inheritedtypes')

    def getDocColumn(self) -> int:
        return self.data.get('key.doc.column')

    def getDocumentationComment(self) -> str:
        return self.data.get('key.doc.comment')

    def getDocDeclaration(self) -> str:
        return self.data.get('key.doc.declaration')

    def getDocDiscussion(self) -> list:
        return self.data.get('key.doc.discussion')

    def getDocFile(self) -> str:
        return self.data.get('key.doc.file')

    def getDocLine(self) -> int:
        return self.data.get('key.doc.line')

    def getDocName(self) -> str:
        return self.data.get('key.doc.name')

    def getDocParameters(self) -> list:
        return self.data.get('key.doc.parameters')

    def getDocResultDiscussion(self) -> str:
        return self.data.get('key.doc.result_discussion')

    def getDocType(self) -> str:
        return self.data.get('key.doc.type')

    def getUsr(self) -> str:
        return self.data.get('key.usr')

    def getParsedDeclaration(self) -> str:
        return self.data.get('key.parsed_declaration')

    def getParsedScopeEnd(self) -> int:
        return self.data.get('key.parsed_scope.end')

    def getParsedScopeStart(self) -> int:
        return self.data.get('key.parsed_scope.start')

    def getSwiftDeclaration(self) -> str:
        return self.data.get('key.swift_declaration')

    def getSwiftName(self) -> str:
        return self.data.get('key.swift_name')

    def getAlwaysDeprecated(self) -> bool:
        return self.data.get('key.always_deprecated')

    def getAlwaysUnavailable(self) -> bool:
        return self.data.get('key.always_unavailable')

    def getDeprecationMessage(self) -> str:
        return self.data.get('key.deprecation_message')

    def getUnavailableMessage(self) -> str:
        return self.data.get('key.unavailable_message')

    def getAnnotations(self) -> list:
        return self.data.get('key.annotations')

    def getAttributes(self) -> list:
        return self.data.get('key.attributes')

    def getAttribute(self) -> str:
        return self.data.get('key.attribute')

    # endregion

    def __str__(self):
        return str(self.data)

    def printable_value(self):
        # Return name if it is not None, if kind is parameter, return content of the parameter
        if self.getName() is not None:
            return self.getName()
        elif self.getKind() == 'source.lang.swift.decl.var.parameter':
            return self.read_content()
        else:
            return ''

    def print_substructure(self, level=0):
        print(' - ' * level + self.getKind() + ' ' + self.printable_value())
        for sub in self.getSubstructure():
            sub.print_substructure(level + 1)
