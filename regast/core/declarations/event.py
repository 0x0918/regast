from typing import List

from regast.core.core import Core
from regast.core.expressions.identifier import Identifier
from regast.core.variables.event_parameter import EventParameter

class Event(Core):
    def __init__(
        self,
        name: Identifier,
        parameters: List[EventParameter] = [],
        anonymous: bool = False
    ):
        super().__init__()

        self._name: Identifier = name
        self._parameters: List[EventParameter] = parameters
        self._anonymous: bool = anonymous

    @property
    def name(self) -> Identifier:
        return self._name

    @property
    def parameters(self) -> List[EventParameter]:
        return list(self._parameters)

    @property
    def is_anonymous(self) -> bool:
        return self._anonymous

    @property
    def children(self) -> List:
        return [self.name] + self.parameters

    def __eq__(self, other):
        if isinstance(other, Event):
            return (
                self.name == other.name and 
                self.parameters == other.parameters and 
                self.is_anonymous == other.is_anonymous
            )
        return False