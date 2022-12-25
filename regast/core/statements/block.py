from typing import List

from regast.core.statements.statement import Statement

class Block(Statement):
    def __init__(
        self,
        statements: List[Statement],
        unchecked: bool = False
    ):
        super().__init__()

        self._statements: List[Statement] = statements
        self._unchecked: bool = unchecked
    
    @property
    def statements(self) -> List[Statement]:
        return list(self._statements)

    @property
    def is_unchecked(self) -> bool:
        return self._unchecked

    def __eq__(self, other):
        if isinstance(other, Block):
            return self.statements == other.statements
        return False