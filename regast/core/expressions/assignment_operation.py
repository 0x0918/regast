from enum import Enum
from typing import List

from regast.core.expressions.expression import Expression

class AssignmentOperator(str, Enum):
    ASSIGN = "="
    ASSIGN_OR = "|="
    ASSIGN_CARET = "^="
    ASSIGN_AND = "&="
    ASSIGN_LEFT_SHIFT = "<<="
    ASSIGN_RIGHT_SHIFT = ">>="
    ASSIGN_THREE_RIGHT_SHIFT = ">>>="
    ASSIGN_ADDITION = "+="
    ASSIGN_SUBTRACTION = "-="
    ASSIGN_MULTIPLICATION = "*="
    ASSIGN_DIVISION = "/="
    ASSIGN_MODULO = "%="

class AssignmentOperation(Expression):
    def __init__(
        self,
        expressions: List[Expression],
        operator: AssignmentOperator
    ):
        super().__init__()

        assert len(expressions) == 2

        self._expressions: List[Expression] = expressions
        self._operator: AssignmentOperator = operator

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
    def operator(self) -> AssignmentOperator:
        return self._operator

    @property
    def children(self) -> List:
        return self.expressions

    def __str__(self):
        return str(self.left_expression) + ' ' + str(self.operator) + ' ' + str(self.right_expression)

    def __eq__(self, other):
        if isinstance(other, AssignmentOperation):
            return self.expressions == other.expressions and self.operator == other.operator
        return False