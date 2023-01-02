from typing import List
from regast.core.expressions.expression import Expression
from regast.core.statements.statement import Statement


class WhileStatement(Statement):
    def __init__(
        self,
        condition: Expression,
        body: Statement,
    ):
        """
        while ( <condition> ) { <body> }
        """
        super().__init__()

        self._condition: Expression = condition
        self._body: Statement = body

    @property
    def condition(self) -> Expression:
        return self._condition

    @property
    def body(self) -> Statement:
        return self._body

    @property
    def children(self) -> List:
        return [self.condition, self.body]

    def __eq__(self, other):
        if isinstance(other, WhileStatement):
            return self.condition == other.condition and self.body == other.body
        return False