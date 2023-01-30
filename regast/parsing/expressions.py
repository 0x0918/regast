"""
No conditional expression
"""

from typing import Union
from regast.core.expressions.expression import Expression
from regast.core.expressions.struct_expression import StructArguments
from regast.exceptions import ParsingException


class ExpressionParser:
    @staticmethod
    def parse_expression(node) -> Expression:
        match node.type:
            case 'struct_arguments': return ExpressionParser.parse_struct_arguments(node)

            # Regular Expressions
            case 'binary_expression': return ExpressionParser.parse_binary_expression(node)    
            case 'unary_expression': return ExpressionParser.parse_unary_expression(node)
            case 'update_expression': return ExpressionParser.parse_update_expression(node)
            case 'call_expression': return ExpressionParser.parse_call_expression(node)
            case 'payable_conversion_expression': return ExpressionParser.parse_payable_conversion_expression(node)
            case 'meta_type_expression': return ExpressionParser.parse_meta_type_expression(node)
            case 'struct_expression': return ExpressionParser.parse_struct_expression(node)
            case 'ternary_expression': return ExpressionParser.parse_ternary_expression(node)
            case 'type_cast_expression': return ExpressionParser.parse_type_cast_expression(node)    

            # Primary Expressions
            case 'parenthesized_expression': return ExpressionParser.parse_parenthesized_expression(node)
            case 'member_expression': return ExpressionParser.parse_member_expression(node)
            case 'array_access': return ExpressionParser.parse_array_access(node)
            case 'slice_access': return ExpressionParser.parse_slice_access(node)
            case 'primitive_type': return ExpressionParser.parse_primitive_type(node)
            case 'assignment_expression': return ExpressionParser.parse_assignment_expression(node)
            case 'augmented_assignment_expression': return ExpressionParser.parse_augmented_assignment_expression(node)
            case 'user_defined_type': return ExpressionParser.parse_user_defined_type(node)
            case 'tuple_expression': return ExpressionParser.parse_tuple_expression(node)
            case 'inline_array_expression': return ExpressionParser.parse_inline_array_expression(node)
            case 'identifier': return ExpressionParser.parse_identifier(node)
            case 'new_expression': return ExpressionParser.parse_new_expression(node)
            
            case 'string_literal' | 'number_literal' | 'boolean_literal' | 'hex_string_literal' | 'unicode_string_literal':
                return ExpressionParser.parse_literal(node)
            
            case other: 
                raise ParsingException(f'Unknown tree-sitter node type for expression: {other}')

    @staticmethod
    def parse_call_argument(node) -> Union[Expression, StructArguments]:
        assert node.type == 'call_argument'

        match [x.type for x in node.children]:
            # expression (normal argument)
            case [_]:
                return ExpressionParser.parse_expression(node.children[0])

            # struct arguments
            case ['{', *_, '}']:
                return ExpressionParser.parse_struct_arguments(node)

            case _:
                raise ParsingException(f'Unable to parse call_argument: {node.text}')

    @staticmethod
    def parse_binary_expression(node):
        assert node.type == 'binary_expression'

    @staticmethod
    def parse_unary_expression(node):
        pass

    @staticmethod
    def parse_update_expression(node):
        pass

    @staticmethod
    def parse_call_expression(node):
        pass

    @staticmethod
    def parse_payable_conversion_expression(node):
        pass

    @staticmethod
    def parse_meta_type_expression(node):
        pass

    @staticmethod
    def parse_struct_arguments(node):
        pass

    @staticmethod
    def parse_struct_expression(node):
        pass

    @staticmethod
    def parse_ternary_expression(node):
        pass

    @staticmethod
    def parse_type_cast_expression(node):
        pass
    
    # PRIMARY EXPRESSIONS
    @staticmethod
    def parse_parenthesized_expression(node):
        pass

    @staticmethod
    def parse_member_expression(node):
        pass

    @staticmethod
    def parse_array_access(node):
        pass

    @staticmethod
    def parse_slice_access(node):
        pass

    @staticmethod
    def parse_primitive_type(node):
        pass

    @staticmethod
    def parse_assignment_expression(node):
        pass

    @staticmethod
    def parse_augmented_assignment_expression(node):
        pass

    @staticmethod
    def parse_user_defined_type(node):
        assert node.type in ['user_defined_type', 'type_alias']

    @staticmethod
    def parse_tuple_expression(node):
        pass

    @staticmethod
    def parse_inline_array_expression(node):
        pass

    @staticmethod
    def parse_identifier(node):
        pass

    @staticmethod
    def parse_literal(node):
        pass

    @staticmethod
    def parse_new_expression(node):
        pass
