from enum import Enum
from typing import List

from regast.parsing.expressions.expression import Expression
from regast.parsing.expressions.expression_parsing import parse_expression

class BinaryOperator(str, Enum):
    POWER = "**"
    MULTIPLICATION = "*"
    DIVISION = "/"
    MODULO = "%"
    ADDITION = "+"
    SUBTRACTION = "-"
    LEFT_SHIFT = "<<"
    RIGHT_SHIFT = ">>"
    AND = "&"
    CARET = "^"
    OR = "|"
    LESS = "<"
    GREATER = ">"
    LESS_EQUAL = "<="
    GREATER_EQUAL = ">="
    EQUAL = "=="
    NOT_EQUAL = "!="
    ANDAND = "&&"
    OROR = "||"


class BinaryOperation(Expression):
    def __init__(self, ctx):
        super().__init__(ctx)

        self._expressions: List[Expression] = []
        self._binary_operator: BinaryOperation = None

    @property
    def expressions(self) -> List[Expression]:
        if not self._expressions:
            expressions = self.context.expression()
            assert len(expressions) == 2
            self._expressions = [parse_expression(x) for x in expressions]
        return list(self._expressions)

    @property
    def left_expression(self) -> Expression:
        return self.expressions[0]

    @property
    def right_expression(self) -> Expression:
        return self.expressions[1]

    @property
    def operator(self) -> BinaryOperator:
        if not self._binary_operator:
            binary_operator_str = self.context.getText().replace(str(self.left_expression), '').replace(str(self.right_expression, ''))
            self._binary_operator = BinaryOperator(binary_operator_str)
        return self._binary_operator

    def __str__(self):
        return str(self.left_expression) + ' ' + str(self.operator) + ' ' + str(self.right_expression)

    def __eq__(self, other):
        if isinstance(other, BinaryOperation):
            return self.expressions == other.expressions and self.operator == other.operator
        return False