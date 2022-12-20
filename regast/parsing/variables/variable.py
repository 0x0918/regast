from enum import Enum
from typing import Optional

from regast.parsing.context.context import Context
from regast.parsing.expressions.expression import Expression
from regast.parsing.expressions.identifier import Identifier
from regast.parsing.types.type import Type
from regast.parsing.types.type_parsing import parse_type

class VariableStorageLocationTokens:
    tokens = ['memory', 'storage', 'calldata']

class VariableStorageLocation(Enum, VariableStorageLocationTokens):
    MEMORY = 0
    STORAGE = 1
    CALLDATA = 2

    @classmethod
    def token_to_enum(cls, token):
        return cls(cls.tokens.index(token))

    def __str__(self):
        return self.tokens[self.value]

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        return self == other

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
            identifier = self.context.identifier()
            if identifier:
                self._name = Identifier(identifier)
        return self._name

    @property
    def initial_expression(self) -> Optional[Expression]:
        if not self._expression:
            expression = self.context.expression()
            if expression:
                self._expression = Expression(expression)
        return self._expression

    @property
    def is_initialized(self) -> bool:
        return bool(self.initial_expression)