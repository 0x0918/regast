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

    @property
    def children(self) -> List:
        return self.variable.children

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

        # Ensure all variables have the same initial_expression
        assert len(set([v.initial_expression for v in variables])) == 1

        self._variables: List[LocalVariable] = variables
        
        self._types: List[Type] = []
        self._names: List[Identifier] = []
        self._data_locations: List[Optional[DataLocation]] = []
        
    @property
    def variables(self) -> List[LocalVariable]:
        return list(self._variables)

    @property
    def types(self) -> List[Type]:
        if not self._types:
            self._types = [v.type for v in self.variables]
        return self._types

    @property
    def names(self) -> List[Identifier]:
        if not self._names:
            self._names = [v.name for v in self.variables]
        return self._names

    @property
    def data_locations(self) -> Optional[DataLocation]:
        if not self._data_locations:
            self._data_locations = [v.data_location for v in self.variables]
        return self._data_locations

    @property
    def initial_expression(self) -> Optional[Expression]:
        return self.variables[0].initial_expression

    @property
    def children(self) -> List:
        children = self.types + self.names
        if self.initial_expression:
            children.append(self.initial_expression)
        return children
        
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

    @property
    def children(self) -> List:
        if self.initial_expression:
            return self.names + [self.initial_expression]
        return self.names        

    def __eq__(self, other):
        if isinstance(other, VariableDeclarationWithVarStatement):
            return self.names == other.names and self.initial_expression == other.initial_expression
        return False

# TODO Need to account for the overlap in .children of this and localvariable
# Idea: Implement __hash__ in core, then do list(set(children))