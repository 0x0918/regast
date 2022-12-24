from typing import Optional
from regast.core.expressions.identifier import Identifier

from regast.core.variables.variable import Variable
from regast.core.types.type import Type

class EventParameter(Variable):
    def __init__(
        self, 
        type: Type,
        indexed: bool = False,
        name: Optional[Identifier] = None
    ):
        super().__init__(type, name=name)

        self._indexed = indexed

    @property
    def is_indexed(self) -> bool:
        return self._indexed

    def __str__(self):
        s = str(self.type)
        if self.is_indexed:
            s += " indexed"
        if self.name:
            s += " " + str(self.name)
        return s
        
    def __eq__(self, other):
        if isinstance(other, EventParameter):
            return self.type == other.type and self.is_indexed == other.is_indexed and self.name == other.name
        return False