from enum import Enum
from typing import List

from regast.parsing.expressions.expression import Expression
from regast.parsing.expressions.expression_parsing import parse_expression

class AssignmentOperator(str, Enum):
    ASSIGN = "="
    ASSIGN_OR = "|="
    ASSIGN_CARET = "^="
    ASSIGN_AND = "&="
    ASSIGN_LEFT_SHIFT = "<<="
    ASSIGN_RIGHT_SHIFT = ">>="
    ASSIGN_ADDITION = "+="
    ASSIGN_SUBTRACTION = "-="
    ASSIGN_MULTIPLICATION = "*="
    ASSIGN_DIVISION = "/="
    ASSIGN_MODULO = "%="

class AssignmentOperation(Expression):
    def __init__(self, ctx):
        super().__init__(ctx)

        self._expressions: List[Expression] = []
        self._assignment_operator: AssignmentOperator = None

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
    def operator(self) -> AssignmentOperator:
        if not self._assignment_operator:
            assignment_operator_str = self.context.getText().replace(str(self.left_expression), '').replace(str(self.right_expression, ''))
            self._assignment_operator = AssignmentOperator(assignment_operator_str)
        return self._assignment_operator

    def __str__(self):
        return str(self.left_expression) + ' ' + str(self.operator) + ' ' + str(self.right_expression)

    def __eq__(self, other):
        if isinstance(other, AssignmentOperation):
            return self.expressions == other.expressions and self.operator == other.operator
        return False