from typing import Union
from regast.core.common import StateMutability, Visibility
from regast.core.declarations.contracts.contract import Contract, InheritanceSpecifier
from regast.core.declarations.contracts.interface import Interface
from regast.core.declarations.contracts.library import Library
from regast.core.declarations.custom_error import CustomError
from regast.core.declarations.directives.import_directive import Import
from regast.core.declarations.directives.pragma_directive import Pragma
from regast.core.declarations.directives.using_directive import UsingDirective
from regast.core.declarations.enum import Enum
from regast.core.declarations.functions.constructor import Constructor
from regast.core.declarations.functions.fallback_function import FallbackFunction
from regast.core.declarations.functions.function import Function, ModifierInvocation
from regast.core.declarations.functions.modifier import Modifier
from regast.core.declarations.functions.receive_function import ReceiveFunction
from regast.core.declarations.source_unit import SourceUnit
from regast.core.declarations.struct import Struct
from regast.exceptions import ParsingException
from regast.parsing.expressions import ExpressionParser
from regast.parsing.helpers import extract_call_arguments
from regast.parsing.statements import StatementParser
from regast.parsing.tree_sitter_node import TreeSitterNode
from regast.parsing.types import TypeParser
from regast.parsing.variables import VariableParser


class DeclarationParser:
    @staticmethod
    def parse_source_unit(node: TreeSitterNode, fname: str) -> SourceUnit:
        assert node.type == 'source_file'

        source_unit = SourceUnit(node, fname)
        for child_node in node.children:
            match child_node.type:
                # Directives
                case 'pragma_directive':
                    pragma_directive = DeclarationParser.parse_pragma_directive(child_node)
                    source_unit._pragma_directives.append(pragma_directive)
                    
                case 'import_directive':
                    import_directive = DeclarationParser.parse_import_directive(child_node)
                    source_unit._import_directives.append(import_directive)

                # Contracts
                case 'contract_declaration':
                    contract = DeclarationParser.parse_contracts(child_node)
                    assert isinstance(contract, Contract)
                    source_unit._contracts.append(contract)

                case 'interface_declaration':
                    interface = DeclarationParser.parse_contracts(child_node)
                    assert isinstance(interface, Interface)
                    source_unit._interfaces.append(contract)

                case 'library_declaration':
                    library = DeclarationParser.parse_contracts(child_node)
                    assert isinstance(library, Library)
                    source_unit._libraries.append(library)

                # Declarations
                case 'error_declaration':
                    custom_error = DeclarationParser.parse_error_declaration(child_node)
                    source_unit._custom_errors.append(custom_error)
                    
                case 'struct_declaration':
                    struct = DeclarationParser.parse_struct_declaration(child_node)
                    source_unit._structs.append(struct)
                    
                case 'enum_declaration':
                    enum = DeclarationParser.parse_enum_declaration(child_node)
                    source_unit._enums.append(enum)

                case 'function_definition':
                    function = DeclarationParser.parse_function_definition(child_node)
                    source_unit._functions.append(function)

                case 'constant_variable_declaration':
                    constant = VariableParser.parse_constant_variable_declaration(child_node)
                    source_unit._constants.append(constant)

                case 'user_defined_type_definition':
                    type_definition = DeclarationParser.parse_user_defined_type_definition(child_node)
                    source_unit._type_definitions.append(type_definition) 

                case 'ERROR':
                    pass

                case other:
                    raise ParsingException(f'Unknown tree-sitter node for source_unit: {other}')
                    
        return source_unit

    # CONTRACTS
    @staticmethod
    def parse_contracts(node: TreeSitterNode) -> Union[Contract, Interface, Library]:
        assert node.type in ['contract_declaration', 'interface_declaration', 'library_declaration']

        contract = None
        match node.type:
            case 'contract_declaration':
                contract = Contract(node)
            case 'interface_declaration':
                contract = Interface(node)
            case 'library_declaration':
                contract = Library(node)

        def parse_inheritance_specifier(node: TreeSitterNode):
            assert node.type == 'inheritance_specifier'

            [ancestor], arguments, struct_arguments = extract_call_arguments(node.children)
            assert ancestor.type == 'user_defined_type'

            inheritance_specifier = InheritanceSpecifier(node)
            inheritance_specifier._name = TypeParser.parse_user_defined_type(ancestor)
            inheritance_specifier._arguments = arguments
            inheritance_specifier._struct_arguments = struct_arguments

            contract._inheritance_specifiers.append(inheritance_specifier)

        def parse_contract_body(node: TreeSitterNode):
            assert node.type == 'contract_body'

            for child_node in node.children:
                match child_node.type:
                    case 'function_definition':
                        function = DeclarationParser.parse_functions(child_node)
                        assert isinstance(function, Function)
                        contract._functions.append(function)

                    case 'modifier_definition':
                        modifier = DeclarationParser.parse_functions(child_node)
                        assert isinstance(modifier, Modifier)
                        contract._modifiers.append(modifier)

                    case 'error_declaration':
                        custom_error = DeclarationParser.parse_error_declaration(child_node)
                        contract._custom_errors.append(custom_error)

                    case 'state_variable_declaration':
                        state_variable = VariableParser.parse_state_variable_declaration(child_node)
                        contract._state_variables.append(state_variable)
                        
                    case 'struct_declaration':
                        struct = DeclarationParser.parse_struct_declaration(child_node)
                        contract._structs.append(struct)
                        
                    case 'enum_declaration':
                        enum = DeclarationParser.parse_enum_declaration(child_node)
                        contract._enums.append(enum)

                    case 'event_definition':
                        event = DeclarationParser.parse_event_definition(child_node)
                        contract._events.append(event)
                        
                    case 'using_directive':
                        using_directive = DeclarationParser.parse_using_directive(child_node)
                        contract._using_directives.append(using_directive)
                        
                    case 'constructor_definition':
                        assert not contract.constructor
                        constructor = DeclarationParser.parse_functions(child_node)
                        assert isinstance(constructor, Constructor)
                        contract._constructor = constructor
                        
                    case 'fallback_receive_definition':
                        f = DeclarationParser.parse_functions(child_node)
                        if isinstance(f, FallbackFunction):
                            assert not contract.fallback_function
                            contract._fallback_function = f
                        elif isinstance(f, ReceiveFunction):
                            assert not contract.receive_function
                            contract._receive_function = f
                        # else:
                            # raise ParsingException(f'Unknown resulting fallback_receive_definition: {child_node.text}')

                        # TODO Implement fallback_receive_definition and uncomment the exception above
                            
                    case 'user_defined_type_definition':
                        type_definition = DeclarationParser.parse_user_defined_type_definition(child_node)
                        contract._type_definitions.append(type_definition)

                    case '{' | '}':
                        pass

                    case other:
                        raise ParsingException(f'Unknown tree-sitter node type for contract member: {other}')

        for child_node in node.children:
            match child_node.type:
                case 'abstract':
                    contract._abstract = True
                    
                case 'identifier':
                    assert not contract.name
                    contract._name = ExpressionParser.parse_identifier(child_node)
                    
                case 'inheritance_specifier':
                    parse_inheritance_specifier(child_node)
                    
                case 'contract_body':
                    parse_contract_body(child_node)

                case 'contract' | 'interface' | 'library' | 'is' | ',':
                    pass

                case other:
                    raise ParsingException(f'Unknown tree-sitter node for contract_declaration: {other}')

        return contract

    # DIRECTIVES
    @staticmethod
    def parse_import_directive(node) -> Import:
        assert node.type == 'import_directive'

        import_directive = Import(node)
        match [x.type for x in node.children]:
            # _source_import without _import_alias
            case ['import', 'string']:
                _, source = node.children
                import_directive._import_path = source.text

            # _source_import with _import_alias
            case ['import', 'string', 'as', 'identifier']:
                _, source, _, alias = node.children
                import_directive._import_path = source.text
                import_directive._alias = alias.text

            # from import
            case ['import', *import_clause_types, 'from', 'string']:
                _, *import_clause, _, source = node.children
                import_directive._import_path = source.text

                match import_clause_types:
                    # _single_import without _import_alias
                    case ['*'] | ['identifier']:
                        import_name, = import_clause
                        import_identifier = ExpressionParser.parse_identifier(import_name)
                        import_directive._imported.append(import_identifier)

                    # _single_import with _import_alias
                    case ['*', 'as', 'string'] | ['identifier', 'as', 'string']:
                        import_name, _, alias = import_clause
                        
                        import_identifier = ExpressionParser.parse_identifier(import_name)
                        import_directive._imported.append(import_identifier)

                        alias_identifier = ExpressionParser.parse_identifier(alias)
                        import_directive._renaming[import_identifier] = alias_identifier

                    # _multiple_import
                    case ['{', *import_declaration_types, '}']:
                        _, *import_declarations, _ = import_clause

                        lo = 0
                        for hi in range(len(import_declarations) + 1):
                            if hi == len(import_declarations) or import_declarations[hi].type == ',':
                                match import_declaration_types[lo:hi]:
                                    # import without _import_alias
                                    case ['identifier']:
                                        import_name, = import_declarations[lo:hi]
                                        import_identifier = ExpressionParser.parse_identifier(import_name)
                                        import_directive._imported.append(import_identifier)

                                    # import with _import_alias
                                    case ['identifier', 'as', 'identifier']:
                                        import_name, _, alias = import_declarations[lo:hi]
                                        
                                        import_identifier = ExpressionParser.parse_identifier(import_name)
                                        import_directive._imported.append(import_identifier)

                                        alias_identifier = ExpressionParser.parse_identifier(alias)
                                        import_directive._renaming[import_identifier] = alias_identifier

                                    case _:
                                        raise ParsingException(f'Unable to parse import_clause with multiple imports for import_directive: {node.text}')

                                lo = hi + 1

                    case _:
                        raise ParsingException(f'Unable to parse import_clause for import_directive: {node.text}')

            case _:
                raise ParsingException(f'Unable to parse import_directive: {node.text}')

        return import_directive


    @staticmethod
    def parse_pragma_directive(node) -> Pragma:
        assert node.type == 'pragma_directive'

        p, pragma_token = node.children
        assert p.type == 'pragma'

        pragma_directive = Pragma(node)
        match pragma_token.type:
            case 'any_pragma_token':
                identifier, pragma_value = pragma_token.children
                pragma_directive._name = ExpressionParser.parse_identifier(identifier)
                pragma_directive._value = pragma_value.text

            case 'solidity_pragma_token':
                solidity, *value = pragma_token.children
                assert solidity.type == 'solidity'
                
                pragma_directive._name = ExpressionParser.parse_identifier(solidity)
                pragma_directive._value = ''.join([x.text for x in value])

            case other:
                raise ParsingException(f'Unknown pragma_token for pragma_directive: {other}')        

        return pragma_directive

    @staticmethod
    def parse_using_directive(node) -> UsingDirective:
        assert node.type == 'using_directive'

        using_token, type_alias, for_token, source = node.children
        assert using_token.type == 'using' and type_alias.type == 'type_alias' and for_token.type == 'for'

        using_directive = UsingDirective(node)

        library = ExpressionParser.parse_user_defined_type(type_alias) 
        using_directive._libraries.append(library)
        
        match source.type:
            case 'any_source_type':
                using_directive._any_type = True
            case 'type_name':
                using_directive._type = TypeParser.parse_type_name(source)
            case other:
                raise ParsingException(f'Unknwon source type for using_directive: {other}')
    
        return using_directive

    # FUNCTIONS
    @staticmethod
    def parse_functions(node) -> Union[Function, Constructor, Modifier, FallbackFunction, ReceiveFunction]:
        assert node.type in ['function_definition', 'constructor_definition', 'modifier_definition', 'fallback_receive_definition']

        function = None
        match node.type:
            case 'constructor_definition':
                function = Constructor(node)
            case 'function_definition': 
                function = Function(node)
            case 'fallback_receive_definition':
                function = ReceiveFunction(node) if node.children[0] == 'receive' else FallbackFunction(node)
            case 'modifier_definition':
                function = Modifier(node)

        def parse_modifier_invocation(node: TreeSitterNode):
            assert node.type == 'modifier_invocation'

            identifier_path, arguments, struct_arguments = extract_call_arguments(node.children)

            modifier_invocation = ModifierInvocation(node)
            modifier_invocation._arguments = arguments
            modifier_invocation._struct_arguments = struct_arguments

            for child_node in identifier_path:
                match child_node.type:
                    case 'identifier':
                        identifier = ExpressionParser.parse_identifier(child_node)
                        modifier_invocation._identifiers.append(identifier)
                    case '.':
                        pass
                    case other:
                        raise ParsingException(f'Unknown tree-sitter node type in modifier_invocation: {other}')

            function._modifiers.append(modifier_invocation)

        def parse_override_specifier(node: TreeSitterNode):
            assert node.type == 'override_specifier'

            override_token, *user_defined_types = node.children
            assert override_token.type == 'override'

            function._override = True
            for child_node in user_defined_types:
                match child_node.type:
                    case 'user_defined_type':
                        user_defined_type = ExpressionParser.parse_user_defined_type(child_node)
                        function._overrides.append(user_defined_type)
                    case '(' | ')' | ',':
                        pass
                    case other:
                        raise ParsingException(f'Unknown tree-sitter node type in override_specifier: {other}')

        def parse_return_type_definition(node: TreeSitterNode):
            assert node.type == 'return_type_definition'

            returns_token, open_bracket_token, *parameters, close_bracket_token = node.children
            assert returns_token.type == 'returns' and open_bracket_token.type == '(' and close_bracket_token.type == ')'

            for child_node in parameters:
                match child_node.type:
                    case 'parameter':
                        parameter = VariableParser.parse_parameter(child_node)
                        function._return_parameters.append(parameter)
                    case ',':
                        pass
                    case other:
                        raise ParsingException(f'Unknown tree-sitter node type in return_type_definition: {other}')

        for child_node in node.children:
            match child_node.type:
                case 'identifier':
                    assert not function.name
                    function._name = ExpressionParser.parse_identifier(child_node)

                case 'parameter':
                    parameter = VariableParser.parse_parameter(child_node)
                    function._parameters.append(parameter)

                case 'modifier_invocation':
                    parse_modifier_invocation(child_node)

                case 'visibility' | 'internal' | 'public':
                    assert not function.declared_visibility
                    function._visibility = Visibility(child_node.text)

                case 'state_mutability' | 'payable':
                    assert not function.declared_mutability
                    function._mutability = StateMutability(child_node.text)

                case 'virtual':
                    function._virtual = True

                case 'override_specifier':
                    parse_override_specifier(child_node)

                case 'return_type_definition':
                    parse_return_type_definition(child_node)

                case 'function_body':
                    function._body = StatementParser.parse_block_statement(child_node)

                case 'function' | 'constructor' | 'modifier' | 'fallback' | 'receive' | '(' | ')' | ',':
                    pass

                case other:
                    raise ParsingException(f'Unknown tree-sitter node in function_definition: {other}')

        return function

    # OTHERS
    @staticmethod
    def parse_error_declaration(node):
        assert node.type == 'error_declaration'

        error_token, name, open_bracket_token, *error_parameters, close_bracket_token = node.children
        assert error_token.type == 'error' and open_bracket_token.type == '(' and close_bracket_token.type == ')'
        assert name.type == 'identifier'

        custom_error = CustomError(node)
        custom_error._name = ExpressionParser.parse_identifier(name)

        for child_node in error_parameters:
            match child_node.type:
                case 'error_paramter':
                    error_paramter = VariableParser.parse_error_parameter(child_node)
                    custom_error._parameters.append(error_paramter)
                case ',':
                    pass
                case other:
                    raise ParsingException(f'Unknown tree-sitter node type in error_declaration: {other}')

        return custom_error

    @staticmethod
    def parse_enum_declaration(node):
        assert node.type == 'enum_declaration'
    
        enum_token, name, open_bracket_token, *enum_values, close_bracket_token = node.children
        assert enum_token.type == 'enum' and open_bracket_token.type == '{' and close_bracket_token.type == '}'
        assert name.type == 'identifier'

        enum = Enum(node)
        enum._name = ExpressionParser.parse_identifier(name)

        for child_node in enum_values:
            match child_node.type:
                case 'enum_value':
                    enum_value = ExpressionParser.parse_identifier(child_node)
                    enum._values.append(enum_value)
                case ',':
                    pass
                case other:
                    raise ParsingException(f'Unknown tree-sitter node type in enum_declaration: {other}')

        return enum

    @staticmethod
    def parse_struct_declaration(node):
        assert node.type == 'struct_declaration'
    
        struct_token, name, open_bracket_token, *struct_members, close_bracket_token = node.children
        assert struct_token.type == 'struct' and open_bracket_token.type == '{' and close_bracket_token.type == '}'
        assert name.type == 'identifier'

        struct = Struct(node)
        struct._name = ExpressionParser.parse_identifier(name)

        for struct_member_node in struct_members:
            assert struct_member_node.type == 'struct_member'
            struct_member = VariableParser.parse_struct_member(struct_member_node)
            struct._members.append(struct_member)

        return struct

    @staticmethod
    def parse_event_definition(node):
        pass

    @staticmethod
    def parse_user_defined_type_definition(node):
        pass