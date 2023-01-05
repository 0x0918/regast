from regast.core.declarations.comment import Comment
from regast.core.declarations.source_unit import SourceUnit
from regast.exceptions import ParsingException
from regast.parsing.variables import VariableParser


class DeclarationParser:
    @staticmethod
    def parse_source_unit(fname: str, node):
        assert node.type == 'source_file'
        
        source_unit = SourceUnit(node, fname)
        for child_node in node.children:
            # Comments
            if child_node.type == 'comment':
                comment = DeclarationParser.parse_comment(child_node)
                source_unit._comments.append(comment)

            # Directives
            elif child_node.type == 'pragma_directive':
                pragma_directive = DeclarationParser.parse_pragma_directive(child_node)
                source_unit._pragma_directives.append(pragma_directive)
            elif child_node.type == 'import_directive':
                import_directive = DeclarationParser.parse_import_directive(child_node)
                source_unit._import_directives.append(import_directive)

            # Contracts
            elif child_node.type == 'contract_declaration':
                contract = DeclarationParser.parse_contract_declaration(child_node)
                source_unit._contracts.append(contract)
            elif child_node.type == 'interface_declaration': 
                interface = DeclarationParser.parse_interface_declaration(child_node)
                source_unit._contracts.append(interface)
            elif child_node.type == 'library_declaration':
                library = DeclarationParser.parse_library_declaration(child_node)
                source_unit._contracts.append(library)
            
            # Declarations
            elif child_node.type == 'error_declaration':
                custom_error = DeclarationParser.parse_error_declaration(child_node)
                source_unit._custom_errors.append(custom_error)
            elif child_node.type == 'struct_declaration':
                struct = DeclarationParser.parse_struct_declaration(child_node)
                source_unit._structs.append(struct)
            elif child_node.type == 'enum_declaration':
                enum = DeclarationParser.parse_enum_declaration(child_node)
                source_unit._enums.append(enum)
            elif child_node.type == 'function_definition':
                function = DeclarationParser.parse_function_definition(child_node)
                source_unit._functions.append(function)
            elif child_node.type == 'constant_variable_declaration':
                constant = VariableParser.parse_constant_variable_declaration(child_node)
                source_unit._constants.append(constant)
            elif child_node.type == 'user_defined_type_definition':
                type_definition = DeclarationParser.parse_user_defined_type_definition(child_node)
                source_unit._type_definitions.append(type_definition)

            else:
                raise ParsingException(f'Unknown tree-sitter node for source_unit: {child_node.type}')
        
        return source_unit

    @staticmethod
    def parse_comment(node):
        assert node.type == 'comment'
        return Comment(node)

    # CONTRACTS
    @staticmethod
    def parse_contract_declaration(node):
        """
        TODO Stopped here:
        - Continue parsing from top-down
        - Change core to only take in node as argument, and access private attributes directly
        """
        pass

    @staticmethod
    def parse_interface_declaration(node):
        pass

    @staticmethod
    def parse_library_declaration(node):
        pass

    # DIRECTIVES
    @staticmethod
    def parse_import_directive(node):
        pass

    @staticmethod
    def parse_pragma_directive(node):
        pass

    @staticmethod
    def parse_using_directive(node):
        pass

    # FUNCTIONS
    @staticmethod
    def parse_constructor_definition(node):
        pass

    @staticmethod
    def parse_fallback_receive_definition(node):
        pass

    @staticmethod
    def parse_modifier_definition(node):
        pass

    @staticmethod
    def parse_function_definition(node):
        pass

    # OTHERS
    @staticmethod
    def parse_error_declaration(node):
        pass

    @staticmethod
    def parse_enum_declaration(node):
        pass
    
    @staticmethod
    def parse_struct_declaration(node):
        pass

    @staticmethod
    def parse_event_definition(node):
        pass

    @staticmethod
    def parse_user_defined_type_definition(node):
        pass