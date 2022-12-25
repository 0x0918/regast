from typing import Optional

from regast.core.expressions.expression import Expression
from regast.core.statements.statement import Statement
from regast.core.variables.local_variable import LocalVariable


class ForStatement(Statement):
    def __init__(
        self,
        body: Statement,
        initialization: Optional[LocalVariable] = None,
        condition: Optional[Expression] = None,
        iteration: Optional[Expression] = None
    ):
        """
        for ( <initialization> ; <condition> ; <iteration> ) { <body> }
        """
        super().__init__()

        self._body: Statement = body
        self._initialization: Optional[LocalVariable] = initialization
        self._condition: Optional[Expression] = condition
        self._iteration: Optional[Expression] = iteration

    @property
    def body(self) -> Statement:
        return self._body

    @property
    def initialization(self) -> Optional[LocalVariable]:
        return self._initialization

    @property
    def condition(self) -> Optional[Expression]:
        return self._condition

    @property
    def iteration(self) -> Optional[Expression]:
        return self._iteration

    def __eq__(self, other):
        if isinstance(other, ForStatement):
            return self.body == other.body and self.initialization == other.initialization and self.condition == other.condition and self.iteration == other.iteration
        return False