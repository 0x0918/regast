from enum import Enum

from regast.parsing.expressions.expression import Expression
from regast.parsing.expressions.identifier import Identifier
from regast.parsing.variables.variable import Variable

class StateVariableMutabilityTokens:
    tokens = ['', 'immutable', 'constant']

class StateVariableMutability(StateVariableMutabilityTokens, Enum):
    MUTABLE = 0
    IMMUTABLE = 1
    CONSTANT = 2

    @classmethod
    def token_to_enum(cls, token):
        # if token not in cls.tokens:
        #     raise ParsingError(f"Failed to convert {token} to ContractType")
        return cls(cls.tokens.index(token))

    def __str__(self):
        return self.tokens[self.value]

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        return self == other

class StateVariableVisibilityTokens:
    tokens = ['public', 'private', 'internal', 'external']

class StateVariableVisibility(StateVariableVisibilityTokens, Enum):
    PUBLIC = 0
    PRIVATE = 1
    INTERNAL = 2 
    EXTERNAL = 3

    @classmethod
    def token_to_enum(cls, token):
        return cls(cls.tokens.index(token))

    def __str__(self):
        return self.tokens[self.value]

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        return self == other

class StateVariable(Variable):
    def __init__(self, ctx):    # StateVariableDeclarationContext
        super().__init__(ctx)

        self._mutability: StateVariableMutability = None
        self._visibility: StateVariableVisibility = None

# TODO To complete