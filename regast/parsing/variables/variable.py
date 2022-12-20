from typing import Optional

from regast.parsing.context.context import Context
from regast.parsing.expressions.expression import Expression
from regast.parsing.expressions.identifier import Identifier
from regast.parsing.tokens import VariableStorageLocation
from regast.parsing.types.type import Type
from regast.parsing.types.type_parsing import parse_type

class Variable(Context):
    def __init__(self, ctx):
        super().__init__(ctx)

        self._type: Type = None
        self._name: Optional[Identifier] = None
        self._storage_location: Optional[VariableStorageLocation] = None
        self._expression: Optional[Expression] = None

    @property
    def type(self) -> Type:
        if not self._type:
            self._type = parse_type(self.context.typeName())
        return self._type

    @property
    def name(self) -> Optional[Identifier]:
        if not self._name:
            if callable(getattr(self.context, 'identifier', None)):
                identifier = self.context.identifier()
                if identifier:
                    self._name = Identifier(identifier)
        return self._name

    @property
    def storage_location(self) -> VariableStorageLocation:
        if not self._storage_location:
            if callable(getattr(self.context, 'storageLocation', None)):
                storage_location = self.context.storageLocation()
                if storage_location:
                    self._storage_location = VariableStorageLocation.token_to_enum(storage_location.getText())
                else:
                    self._storage_location = VariableStorageLocation.MEMORY
        return self._storage_location

    @property
    def initial_expression(self) -> Optional[Expression]:
        if not self._expression:
            if callable(getattr(self.context, 'expression', None)):
                expression = self.context.expression()
                if expression:
                    self._expression = Expression(expression)
        return self._expression

    @property
    def is_initialized(self) -> bool:
        return bool(self.initial_expression)
            
