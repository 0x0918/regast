from typing import List

from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type

class UserDefinedType(Type):
    def __init__(
        self,
        identifiers: List[Identifier],
    ):
        super().__init__()

        self._identifiers: List[Identifier] = identifiers

    @property
    def type(self) -> str:
        return ".".join([str(x) for x in self._identifiers])

    def __str__(self):
        return self.type

    def __eq__(self, other):
        if isinstance(other, str):
            return self.type == other
        elif isinstance(other, UserDefinedType):
            return self.type == other.type
        return False