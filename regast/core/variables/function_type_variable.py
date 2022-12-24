from typing import Optional

from regast.core.variables.variable import DataLocation, Variable
from regast.core.types.type import Type

class FunctionTypeVariable(Variable):
    def __init__(
        self, 
        type: Type,
        data_location: Optional[DataLocation] = None,
    ):
        super().__init__(type, data_location=data_location)