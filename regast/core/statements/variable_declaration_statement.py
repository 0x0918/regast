from typing import List, Optional

from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.statements.statement import Statement
from regast.core.types.type import Type
from regast.core.variables.local_variable import LocalVariable
from regast.core.variables.variable import DataLocation

class VariableDeclarationStatement(Statement):
    def __init__(
        self,
        variable: LocalVariable
    ):
        super().__init__()

        self._variable: LocalVariable = variable

    @property
    def variable(self) -> LocalVariable:
        self._variable

    @property
    def type(self) -> Type:
        return self.variable.type

    @property
    def name(self) -> Identifier:
        return self.variable.name

    @property
    def data_location(self) -> Optional[DataLocation]:
        return self.variable.data_location

    @property
    def initial_expression(self) -> Optional[Expression]:
        return self.variable.initial_expression

    def __eq__(self, other):
        if isinstance(other, VariableDeclarationStatement):
            return self.variable == other.variable
        return False

class VariableDeclarationFromTupleStatement(Statement):
    def __init__(
        self,
        variables: List[LocalVariable],
    ):
        super().__init__()

        self._variables: List[LocalVariable] = variables

    @property
    def variables(self) -> List[LocalVariable]:
        return list(self._variables)

    @property
    def initial_expression(self) -> Optional[Expression]:
        return self.variables[0].initial_expression

    def __eq__(self, other):
        if isinstance(other, VariableDeclarationFromTupleStatement):
            return self.variables == other.variables
        return False

class VariableDeclarationWithVarStatement(Statement):
    def __init__(
        self,
        identifiers: List[Identifier],
        initial_expression: Expression,
    ):
        """
        Deprecated since v0.4.20
        var (x, y, z) = f()
        """
        super().__init__()

        assert initial_expression

        self._names: List[Identifier] = identifiers
        self._expression: Expression = initial_expression

    @property
    def names(self) -> List[Identifier]:
        return self._names

    @property
    def initial_expression(self) -> Optional[Expression]:
        return self._expression

    def __eq__(self, other):
        if isinstance(other, VariableDeclarationWithVarStatement):
            return self.names == other.names and self.initial_expression == other.initial_expression
        return False