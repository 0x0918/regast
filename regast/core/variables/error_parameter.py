from typing import Optional
from regast.core.expressions.identifier import Identifier

from regast.core.variables.variable import Variable
from regast.core.types.type import Type

class ErrorParameter(Variable):
    def __init__(
        self, 
        type: Type,
        name: Optional[Identifier] = None
    ):
        super().__init__(type, name=name)