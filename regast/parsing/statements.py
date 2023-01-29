"""
No throw statement
"""

from regast.core.expressions.expression import Expression
from regast.core.statements.block import Block
from regast.core.statements.statement import Statement
from regast.core.statements.variable_declaration_statement import VariableDeclaration, VariableDeclarationFromTupleStatement, VariableDeclarationStatement, VariableDeclarationWithVarStatement
from regast.core.variables.variable import DataLocation
from regast.exceptions import ParsingException
from regast.parsing.expressions import ExpressionParser
from regast.parsing.types import TypeParser


class StatementParser:
    @staticmethod
    def parse_statement(node) -> Statement:
        match node.type:
            case 'block_statement': return StatementParser.parse_block_statement(node)
            case 'expression_statement': return StatementParser.parse_expression_statement(node)
            case 'variable_declaration_statement': return StatementParser.parse_variable_declaration_statement(node)
            case 'if_statement': return StatementParser.parse_if_statement(node)
            case 'for_statement': return StatementParser.parse_for_statement(node)
            case 'while_statement': return StatementParser.parse_while_statement(node)
            case 'do_while_statement': return StatementParser.parse_do_while_statement(node)
            case 'continue_statement': return StatementParser.parse_continue_statement(node)
            case 'break_statement': return StatementParser.parse_break_statement(node)
            case 'try_statement': return StatementParser.parse_try_statement(node)
            case 'return_statement': return StatementParser.parse_return_statement(node)
            case 'emit_statement': return StatementParser.parse_emit_statement(node)
            case 'assembly_statement': return StatementParser.parse_assembly_statement(node)
            case 'revert_statement': return StatementParser.parse_revert_statement(node)
    
            case other:
                raise ParsingException(f'Unknown tree-sitter node type for statement: {other}')

    @staticmethod    
    def parse_block_statement(node) -> Block:
        assert node.type in ['function_body', 'block_statement']

        block = Block(node)

        statements = []
        match node.children_types:
            case ['{', *_, '}']:
                _, *statements, _ = node.children

            case ['unchecked', '{', *_, '}']:
                _, _, *statements, _ = node.children
                block._unchecked = True

            case _:
                raise ParsingException(f'Unable to parse block_statement: {node.text}')

        for child_node in statements:
            statement = StatementParser.parse_statement(child_node)
            block._statements.append(statement)

        return block

    @staticmethod    
    def parse_expression_statement(node) -> Expression:
        assert node.type == 'expression_statement'
        return ExpressionParser.parse_expression(node.children[0])

    @staticmethod    
    def parse_variable_declaration_statement(node):
        assert node.type == 'variable_declaration_statement'

        def parse_variable_declaration(node) -> VariableDeclaration:
            assert node.type == 'variable_declaration'

            type_name = location = name = None
            match node.children_types:
                case ['type_name', 'identifier']:
                    type_name, name = node.children
                case ['type_name', ('memory' | 'storage' | 'calldata'), 'identifier']:
                    type_name, location, name = node.children
                case _:
                    raise ParsingException(f'Unable to parse variable_declaration: {node.text}')

            variable_declaration = VariableDeclaration(node)
            variable_declaration._type = TypeParser.parse_type_name(type_name)
            variable_declaration._name = ExpressionParser.parse_identifier(name)
            if location:
                variable_declaration._data_location = DataLocation(location.text)

            return variable_declaration

        match node.children_types:
            case ['variable_declaration', *remaining_types]:
                variable_declaration, *remaining_nodes = node.children

                statement = VariableDeclarationStatement(node)
                statement._variable_declaration = parse_variable_declaration(variable_declaration)

                match remaining_types:
                    # uint256 a;
                    case []:
                        return statement
                    
                    # uint256 a = 10;
                    case ['=', _]:
                        _, expression = remaining_nodes
                        statement._expression = ExpressionParser.parse_expression(expression)
                        return statement

            case ['variable_declaration_tuple', '=', _]:
                variable_declaration_tuple, _, expression = node.children

                match variable_declaration_tuple.children_types:
                    # (uint256 a, uint256 b) = f()
                    case ['(', *_, ')']:
                        _, *variable_declarations, _ = variable_declaration_tuple.children
                        statement = VariableDeclarationFromTupleStatement(node)
                        statement._expression = ExpressionParser.parse_expression(expression)

                        for child_node in variable_declarations:
                            match child_node.type:
                                case 'variable_declaration':
                                    variable_declaration = parse_variable_declaration(child_node)
                                    statement._variable_declarations.append(variable_declaration)
                                case ',':
                                    pass
                                case other:
                                    raise ParsingException(f'Unknown tree-sitter node type in variable_declaration_tuple: {other}')

                        return statement

                    case ['var', '(', *_, ')']:
                        # var (a, b, c) = f()
                        _, _, *identifiers, _ = variable_declaration_tuple.children
                        statement = VariableDeclarationWithVarStatement(node)
                        statement._expression = ExpressionParser.parse_expression(expression)

                        for child_node in identifiers:
                            match child_node.type:
                                case 'identifier':
                                    identifier = ExpressionParser.parse_identifier(identifier)
                                    statement._names.append(identifier)
                                case ',':
                                    pass
                                case other:
                                    raise ParsingException(f'Unknown tree-sitter node type in variable_declaration_tuple: {other}')

                        return statement

        raise ParsingException(f'Unable to parse variable_declaration_statement: {node.text}')

    @staticmethod    
    def parse_if_statement(node):
        pass

    @staticmethod    
    def parse_for_statement(node):
        pass

    @staticmethod    
    def parse_while_statement(node):
        pass

    @staticmethod    
    def parse_do_while_statement(node):
        pass

    @staticmethod    
    def parse_continue_statement(node):
        pass

    @staticmethod    
    def parse_break_statement(node):
        pass

    @staticmethod    
    def parse_try_statement(node):
        pass

    @staticmethod    
    def parse_return_statement(node):
        pass

    @staticmethod    
    def parse_emit_statement(node):
        pass

    @staticmethod    
    def parse_assembly_statement(node):
        pass

    @staticmethod    
    def parse_revert_statement(node):
        pass

