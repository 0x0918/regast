from typing import Optional

from regast.core.expressions.identifier import Identifier
from regast.core.types.type import Type
from regast.core.variables.variable import DataLocation, Variable

class Parameter(Variable):
    def __init__(
        type: Type, 
        name: Optional[Identifier] = None, 
        data_location: Optional[DataLocation] = None
    ):
        super().__init__(
            type,
            name=name, 
            data_location=data_location
        )