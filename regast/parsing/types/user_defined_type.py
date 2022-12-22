from typing import List

from regast.parsing.expressions.identifier import Identifier
from regast.parsing.types.type import Type

class UserDefinedType(Type):
    def __init__(self, ctx):
        super().__init__(ctx)

        self._identifiers: List[Identifier] = []

    @property
    def type(self) -> str:
        if not self._identifiers:
            self._identifiers = [Identifier(x) for x in self.context.identifier()]
        return ".".join([str(x) for x in self._identifiers])

    def __str__(self):
        return self.type

    def __eq__(self, other):
        if isinstance(other, str):
            return self.type == other
        elif isinstance(other, UserDefinedType):
            return self.type == other.type
        return False
