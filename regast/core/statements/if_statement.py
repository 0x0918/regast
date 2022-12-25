from typing import Optional

from regast.core.expressions.expression import Expression
from regast.core.statements.statement import Statement

class IfStatement(Statement):
    def __init__(
        self,
        condition: Expression,
        true_body: Statement,
        false_body: Optional[Statement] = None
    ):
        """
        if ( <condition> ) { <true_body> } else { <false_body> }
        """
        super().__init__()

        self._condition: Expression = condition
        self._true_body: Statement = true_body
        self._false_body: Optional[Statement] = false_body
    
    @property
    def condition(self) -> Expression:
        return self._condition

    @property
    def true_body(self) -> Statement:
        return self._true_body

    @property
    def false_body(self) -> Optional[Statement]:
        return self._false_body

    def __eq__(self, other):
        if isinstance(other, IfStatement):
            return self.condition == other.condition and self.true_body == other.true_body and self.false_body == other.false_body