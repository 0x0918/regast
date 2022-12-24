from typing import Tuple, Union

from regast.core.types.elementary_type import ElementaryType
from regast.core.types.type import Type
from regast.core.types.user_defined_type import UserDefinedType

class MappingType(Type):
    def __init__(
        self,
        key_type: Union[ElementaryType, UserDefinedType],
        value_type: Type
    ):
        super().__init__()

        self._key_type: Union[ElementaryType, UserDefinedType] = key_type
        self._value_type: Type = value_type

    @property
    def key_type(self) -> Union[ElementaryType, UserDefinedType]:
        return self._key_type

    @property
    def value_type(self) -> Type:
        return self._value_type

    @property
    def storage_size(self) -> Tuple[int, bool]:
        return 32, True

    def __str__(self):
        return "mapping(" + str(self.key_type) + " => " + str(self.value_type) + ")"

    def __eq__(self, other):
        if isinstance(other, MappingType):
            return self.key_type == other.key_type and self.value_type == other.value_type
        return False