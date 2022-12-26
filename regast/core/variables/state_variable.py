from enum import Enum
from typing import List, Optional

from regast.core.common import Visibility
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type
from regast.core.types.user_defined_type import UserDefinedType
from regast.core.variables.variable import Variable

class StateVariableMutability(str, Enum):
    MUTABLE = ''
    IMMUTABLE = 'immutable'
    CONSTANT = 'constant'

class StateVariable(Variable):
    def __init__(
        self, 
        type: Type,
        name: Identifier,
        visibility: Optional[Visibility] = None,
        mutability: Optional[StateVariableMutability] = None,
        overrides: List[UserDefinedType] = [],
        initial_expression: Optional[Expression] = None
    ):
        super().__init__(
            type,
            name=name,
            expression=initial_expression
        )

        self._visibility: Optional[Visibility] = visibility
        self._mutability: Optional[StateVariableMutability] = mutability
        self._overrides: List[UserDefinedType] = overrides

    @property    
    def visibility(self) -> Visibility:
        if self._visibility:
            return self._visibility
        return Visibility.PUBLIC

    @property
    def declared_visibility(self) -> Optional[Visibility]:
        """
        This is used to differentiate state variables explicitly declared public
        """
        return self._visibility

    @property
    def mutability(self) -> StateVariableMutability:
        if self._mutability:
            return self._mutability
        return StateVariableMutability.MUTABLE

    @property
    def declared_mutability(self) -> Optional[StateVariableMutability]:
        return self._mutability

    @property
    def overrides(self) -> List[UserDefinedType]:
        return list(self._overrides)

    def __str__(self):
        s = str(self.type)
        if self.declared_visibility:
            s += " " + self.declared_visibility
        if self.mutability != StateVariableMutability.MUTABLE:
            s += " " + self.mutability.value
        if self.overrides:
            s += " override (" + ", ".join([str(x) for x in self.overrides]) + ")"
        s += str(self.name)
        if self.is_initialized:
            s += " = " + str(self.initial_expression)    

    def __eq__(self, other):
        if isinstance(other, StateVariable):
            return self.type == other.type and self.name == other.name and self.declared_visibility == other.declared_visibility and self.mutability == other.mutability and self.overrides == other.overrides and self.initial_expression == other.initial_expression
        return False 