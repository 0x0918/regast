from enum import Enum
from typing import List

from regast.core.expressions.expression import Expression

class BinaryOperator(str, Enum):
    POWER = "**"
    MULTIPLICATION = "*"
    DIVISION = "/"
    MODULO = "%"
    ADDITION = "+"
    SUBTRACTION = "-"
    LEFT_SHIFT = "<<"
    RIGHT_SHIFT = ">>"
    THREE_RIGHT_SHIFT = ">>>"
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
    def __init__(
        self,
        expressions: List[Expression],
        operator: BinaryOperator
    ):
        super().__init__()

        assert len(expressions) == 2

        self._expressions: List[Expression] = expressions
        self._operator: BinaryOperation = operator

    @property
    def expressions(self) -> List[Expression]:
        return list(self._expressions)

    @property
    def left_expression(self) -> Expression:
        return self.expressions[0]

    @property
    def right_expression(self) -> Expression:
        return self.expressions[1]

    @property
    def operator(self) -> BinaryOperator:
        return self._operator
        
    @property
    def children(self) -> List:
        return self.expressions

    def __str__(self):
        return str(self.left_expression) + ' ' + str(self.operator) + ' ' + str(self.right_expression)

    def __eq__(self, other):
        if isinstance(other, BinaryOperation):
            return self.expressions == other.expressions and self.operator == other.operator
        return False