from enum import Enum

from regast.exceptions import ParsingError

class StringTokenEnum:
    tokens = []

    @classmethod
    def token_to_enum(cls, token):
        if token not in cls.tokens:
            raise ParsingError(f"Failed to convert {token} to {cls.__name__}")
        return cls(cls.tokens.index(token))

    def __str__(self):
        return self.tokens[self.value]

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        return self == other

class VariableStorageLocationTokens(StringTokenEnum):
    tokens = ['memory', 'storage', 'calldata']

class VariableStorageLocation(VariableStorageLocationTokens, Enum):
    MEMORY = 0
    STORAGE = 1
    CALLDATA = 2

class StateVariableMutabilityTokens(StringTokenEnum):
    tokens = ['', 'immutable', 'constant']

class StateVariableMutability(StateVariableMutabilityTokens, Enum):
    MUTABLE = 0
    IMMUTABLE = 1
    CONSTANT = 2

class StateVariableVisibilityTokens(StringTokenEnum):
    tokens = ['public', 'private', 'internal', 'external']

class StateVariableVisibility(StateVariableVisibilityTokens, Enum):
    PUBLIC = 0
    PRIVATE = 1
    INTERNAL = 2 
    EXTERNAL = 3

class FunctionStateMutabilityTokens(StringTokenEnum):
    tokens = ['', 'pure', 'constant', 'view', 'payable']

class FunctionStateMutability(FunctionStateMutabilityTokens, Enum):
    NON_PAYABLE = 0
    PURE = 1
    CONSTANT = 2
    VIEW = 3
    PAYABLE = 4

class ContractTypeTokens(StringTokenEnum):
    tokens = ['contract', 'interface', 'abstract', 'library']

class ContractType(ContractTypeTokens, Enum):
    CONTRACT = 0
    INTERFACE = 1
    ABSTRACT = 2
    LIBRARY = 3

# TODO Convert these to string enums