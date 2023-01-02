from typing import List

from regast.core.core import Core
from regast.core.expressions.identifier import Identifier
from regast.core.variables.error_parameter import ErrorParameter

class CustomError(Core):
    def __init__(
        self,
        name: Identifier,
        parameters: List[ErrorParameter] = []
    ):
        super().__init__()

        self._name: Identifier = name
        self._parameters: List[ErrorParameter] = parameters

    @property
    def name(self) -> Identifier:
        return self._name

    @property
    def parameters(self) -> List[ErrorParameter]:
        return list(self._parameters)

    @property
    def children(self) -> List:
        return [self.name] + self.parameters

    def __eq__(self, other):
        if isinstance(other, CustomError):
            return self.name == other.name and self.parameters == other.parameters
        return False