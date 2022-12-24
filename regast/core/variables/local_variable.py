from typing import List, Optional
from regast.core.core import Core
from regast.core.expressions.expression import Expression

from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type
from regast.core.variables.variable import DataLocation, Variable

class LocalVariable(Variable):
    def __init__(
        type: Type,
        name: Identifier,
        data_location: Optional[DataLocation] = None,
        initial_expression: Optional[Expression] = None,
    ):
        super().__init__(
            type,
            name=name,
            data_location=data_location,
            expression=initial_expression
        )

class LocalVariableWithVar(Core):
    def __init__(
        self,
        identifiers: List[Identifier],
        initial_expression: Expression,
    ):
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

    def __str__(self):
        return "(" + ", ".join([str(x) for x in self.names]) + ") = " + str(self.initial_expression)

    def __eq__(self, other):
        if isinstance(other, LocalVariableWithVar):
            return self.names == other.names and self.initial_expression == other.initial_expression
        return False

# Consider adding LocalVariableFromTuple: (int x, int y, int z) = f()