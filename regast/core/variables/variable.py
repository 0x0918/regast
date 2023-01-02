from enum import Enum
from typing import List, Optional

from regast.core.core import Core
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type

class DataLocation(str, Enum):
    MEMORY = 'memory'
    STORAGE = 'storage'
    CALLDATA = 'calldata'

class Variable(Core):
    def __init__(
        self, 
        type: Type,
        name: Optional[Identifier] = None,
        data_location: Optional[DataLocation] = None,
        expression: Optional[Expression] = None
    ):
        super().__init__()

        self._type: Type = type
        self._name: Optional[Identifier] = name
        self._data_location: Optional[DataLocation] = data_location
        self._expression: Optional[Expression] = expression

    @property
    def type(self) -> Type:
        return self._type

    @property
    def name(self) -> Optional[Identifier]:
        return self._name

    @property
    def data_location(self) -> Optional[DataLocation]:
        return self._data_location

    @property
    def initial_expression(self) -> Optional[Expression]:
        return self._expression

    @property
    def is_initialized(self) -> bool:
        return bool(self.initial_expression)

    @property
    def children(self) -> List:
        return [self.type] + [x for x in [self.name, self.initial_expression] if x]

    def __str__(self):
        s = str(self.type)
        if self.data_location:
            s += ' ' + self.data_location.value
        if self.name:
            s += ' ' + str(self.name)
        if self.is_initialized:
            s += ' = ' + str(self.initial_expression)
        return s

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.type == other.type and self.name == other.name and self.data_location == other.data_location and self.initial_expression == other.initial_expression
        return False
            
