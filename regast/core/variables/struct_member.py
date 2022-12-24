from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type
from regast.core.variables.variable import Variable

class StructMember(Variable):
    def __init__(
        self,
        type: Type,
        name: Identifier,
    ):
        super().__init__(type, name=name)
