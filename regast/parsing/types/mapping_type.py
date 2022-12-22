from typing import Tuple, Union

from regast.exceptions import ParsingError
from regast.parsing.types.elementary_type import ElementaryType
from regast.parsing.types.type import Type
from regast.parsing.types.type_parsing import parse_type
from regast.parsing.types.user_defined_type import UserDefinedType

class MappingType(Type):
    def __init__(self, ctx):    # MappingContext
        super().__init__(ctx)

        self._key_type: Union[ElementaryType, UserDefinedType] = None
        self._value_type: Type = None

    @property
    def key_type(self) -> Union[ElementaryType, UserDefinedType]:
        if not self._key_type:
            key = self.context.mappingKey()
            elementary_type = key.elementaryTypeName()
            user_defined_type = key.userDefinedTypeName()

            if elementary_type:
                self._key_type = ElementaryType(elementary_type)
            elif user_defined_type:
                self._key_type = UserDefinedType(user_defined_type)
            else:
                raise ParsingError(f'Failed to parse mapping key type: {key.getText()}')
            
        return self._key_type

    @property
    def value_type(self) -> Type:
        if not self._value_type:
            self._value_type = parse_type(self.context.typeName())
        return self._value_type

    @property
    def storage_size(self) -> Tuple[int, bool]:
        return 32, True

    def __str__(self):
        return f"mapping({str(self.key_type)} => {str(self.value_type)})"

    def __eq__(self, other):
        if isinstance(other, MappingType):
            return self.key_type == other.key_type and self.value_type == other.value_type
        return False