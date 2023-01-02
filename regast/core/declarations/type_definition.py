from typing import List
from regast.core.core import Core
from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type

class TypeDefinition(Core):
    def __init__(
        self,
        alias: Identifier,
        type: Type
    ):
        super().__init__()

        self._alias: Identifier = alias
        self._type: Type = type

    @property
    def alias(self) -> Identifier:
        return self._alias

    @property
    def type(self) -> Type:
        return self._type

    @property
    def children(self) -> List:
        return [self.alias, self.type]

    def __eq__(self, other):
        if isinstance(other, TypeDefinition):
            return self.alias == other.alias and self.type == other.type
        return False