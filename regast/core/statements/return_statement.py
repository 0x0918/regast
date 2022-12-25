from typing import Optional

from regast.core.expressions.expression import Expression
from regast.core.statements.statement import Statement

class ReturnStatement(Statement):
    def __init__(
        self,
        return_value: Optional[Expression] = None,
    ):
        super().__init__()

        self._return_value: Optional[Expression] = return_value

    @property
    def return_value(self) -> Optional[Expression]:
        return self._return_value

    def __eq__(self, other):
        if isinstance(other, ReturnStatement):
            return self.return_value == other.return_value
        return False
            