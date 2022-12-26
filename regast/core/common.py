from enum import Enum

class Visibility(str, Enum):
    PUBLIC = 'public'
    PRIVATE = 'private'
    INTERNAL = 'internal'
    EXTERNAL = 'external'

class StateMutability(str, Enum):
    NON_PAYABLE = ''
    PURE = 'pure'
    CONSTANT = 'constant'
    VIEW = 'view'
    PAYABLE = 'payable'