from enum import Enum

class VariableStorageLocation(str, Enum):
    MEMORY = 'memory'
    STORAGE = 'storage'
    CALLDATA = 'calldata'

class Visibility(str, Enum):
    PUBLIC = 'public'
    PRIVATE = 'private'
    INTERNAL = 'internal'
    EXTERNAL = 'external'

class StateVariableMutability(str, Enum):
    MUTABLE = ''
    IMMUTABLE = 'immutable'
    CONSTANT = 'constant'

class StateMutability(str, Enum):
    NON_PAYABLE = ''
    PURE = 'pure'
    CONSTANT = 'constant'
    VIEW = 'view'
    PAYABLE = 'payable'

class FunctionInheritance(str, Enum):
    NONE = ''
    VIRTUAL = 'virtual'
    OVERRIDE = 'override'

class ContractType(str, Enum):
    CONTRACT = 'contract'
    INTERFACE = 'interface'
    ABSTRACT = 'abstract'
    LIBRARY = 'library'