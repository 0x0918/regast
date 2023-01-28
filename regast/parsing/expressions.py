"""
No conditional expression
"""

from typing import Union
from regast.core.expressions.expression import Expression
from regast.core.expressions.struct_expression import StructArguments
from regast.exceptions import ParsingException


class ExpressionParser:
    @staticmethod
    def parse_expression(node):
        pass

    @staticmethod
    def parse_call_argument(node) -> Union[Expression, StructArguments]:
        assert node.type == 'call_argument'

        match [x.type for x in node.children]:
            # expression (normal argument)
            case [expression_node]:
                return ExpressionParser.parse_expression(expression_node)

            # struct arguments
            case ['{', *_, '}']:
                return ExpressionParser.parse_struct_arguments(node)

            case _:
                raise ParsingException(f'Unable to parse call_argument: {node.text}')

    @staticmethod
    def parse_binary_expression(node):
        pass

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
