from typing import List, Optional

from regast.core.core import Core
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.statements.statement import Statement
from regast.core.statements.block import Block
from regast.core.variables.parameter import Parameter

class CatchClause(Core):
    def __init__(
        self,
        block: Block,
        parameters: List[Parameter] = [],
        error: Optional[Identifier] = None,
    ):
        super().__init__()

        self._block: Block = block
        self._parameters: List[Parameter] = parameters
        self._error: Optional[Identifier] = error

    @property
    def body(self) -> Block:
        return self._block
    
    @property
    def parameters(self) -> List[Parameter]:
        return list(self._parameters)

    @property
    def error(self) -> Optional[Identifier]:
        return self._error

    @property
    def children(self) -> List:
        children = [self.body] + self.parameters
        if self.error:
            children.append(self.error)
        return children

    def __eq__(self, other):
        if isinstance(other, CatchClause):
            return self.block == other.block and self.parameters == other.parameters and self.error == other.error
        return False

class TryStatement(Statement):
    def __init__(
        self,
        try_expression: Expression,
        body: Block,
        catch_clauses: List[CatchClause],
        parameters: List[Parameter] = []
    ):
        super().__init__()

        self._try_expression: Expression = try_expression
        self._body: Block = body
        self._catch_clauses: List[CatchClause] = catch_clauses
        self._parameters: List[Parameter] = parameters

    @property
    def try_expression(self) -> Expression:
        return self._try_expression

    @property
    def body(self) -> Block:
        return self._body

    @property
    def catch_clauses(self) -> List[CatchClause]:
        return list(self._catch_clauses)

    @property
    def parameters(self) -> List[Parameter]:
        return list(self._try_expression)

    @property
    def children(self) -> List:
        return [self.try_expression, self.body] + self.catch_clauses + self.parameters

    def __eq__(self, other):
        if isinstance(other, TryStatement):
            return self.try_expression == other.try_expression and self.body == other.body and self.catch_clauses == other.catch_clauses and self.parameters == other.parameters
        return False

