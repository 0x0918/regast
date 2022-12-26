from typing import List

from regast.core.core import Core
from regast.core.expressions.identifier import Identifier

class Enum(Core):
    def __init__(
        self,
        name: Identifier,
        values: List[Identifier]
    ):
        super().__init__()

        self._name: Identifier = name
        self._values: List[Identifier] = values

    @property
    def name(self) -> Identifier:
        return self._name

    @property
    def values(self) -> List[Identifier]:
        return list(self._values)

    def __eq__(self, other):
        if isinstance(other, Enum):
            return self.name == other.name and self.values == other.values
        return False