from typing import List

from regast.core.expressions.expression import Expression

class ConditionalExpression(Expression):
    def __init__(
        self,
        expressions: List[Expression]
    ):
        super().__init__()

        assert len(expressions) == 3

        self._expressions: List[Expression] = expressions

    @property
    def expressions(self) -> Expression:
        return self._expressions

    @property
    def condition(self) -> Expression:
        return self._expressions[0]

    @property
    def true_expression(self) -> Expression:
        return self._expressions[1]

    @property
    def false_expression(self) -> Expression:
        return self._expressions[2]

    def __str__(self):
        return str(self.condition) + " ? " + str(self.true_expression) + " : " + str(self.false_expression)

    def __eq__(self, other):
        if isinstance(other, ConditionalExpression):
            return self.expressions == other.expressions
        return False