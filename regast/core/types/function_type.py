from typing import List, Optional, Tuple
from regast.core.common import StateMutability, Visibility

from regast.core.types.type import Type
from regast.core.variables.function_type_variable import FunctionTypeVariable

class FunctionType(Type):
    def __init__(
        self,
        parameters: List[FunctionTypeVariable],
        return_parameters: List[FunctionTypeVariable],
        visibility: Optional[Visibility] = None,
        state_mutability: Optional[StateMutability] = None,        
    ):
        super().__init__()

        self._parameters: List[FunctionTypeVariable] = parameters
        self._return_parameters: List[FunctionTypeVariable] = return_parameters
        self._visibility: Optional[Visibility] = visibility
        self._state_mutability: Optional[StateMutability] = state_mutability

    @property
    def parameters(self) -> List[FunctionTypeVariable]:
        return list(self._parameters)

    @property
    def return_parameters(self) -> List[FunctionTypeVariable]:
        return list(self.return_parameters)

    @property
    def visibility(self) -> Optional[Visibility]:
        return self._visibility

    @property                
    def state_mutability(self) -> Optional[StateMutability]:
        return self._state_mutability

    @property
    def storage_size(self) -> Tuple[int, bool]:
        return 24, False

    @property
    def children(self) -> List:
        return self.parameters + self.return_parameters

    def __str__(self):
        s = 'function'
        if self.parameters:
            s += ' (' + ', '.join([str(x) for x in self.parameters]) + ')'
        if self.visibility:
            s += ' ' + self.visibility.value
        if self.state_mutability:
            s += ' ' + self.state_mutability.value
        if self.return_parameters:
            s += ' (' + ', '.join([str(x) for x in self.return_parameters]) + ')'
        return s

    def __eq__(self, other):
        if isinstance(other, FunctionType):
            return self.parameters == other.parameters and self.return_parameters == other.return_parameters and self.visibility == other.visibility and other.state_mutability == other.state_mutability
        return False
        