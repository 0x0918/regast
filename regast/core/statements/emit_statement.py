from regast.core.expressions.call_expression import CallExpression
from regast.core.statements.statement import Statement

class EmitStatement(Statement):
    def __init__(
        self,
        call: CallExpression,
    ):
        super().__init__()

        self._call: CallExpression = call

    @property
    def call(self) -> CallExpression:
        return self._call

    def __eq__(self, other):
        if isinstance(other, EmitStatement):
            return self.call == other.call
        return False