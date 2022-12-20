import enum
from typing import List

from regast.exceptions import ParsingError
from regast.parsing.context.context import Context
from regast.parsing.declarations.custom_error import CustomError
from regast.parsing.declarations.enum import Enum
from regast.parsing.declarations.event import Event
from regast.parsing.declarations.function import Function
from regast.parsing.declarations.struct import Struct
from regast.parsing.expressions.identifier import Identifier
from regast.parsing.variables.state_variable import StateVariable

class ContractTypeTokens:
    tokens = ['contract', 'interface', 'abstract', 'library']

class ContractType(ContractTypeTokens, enum.Enum):
    CONTRACT = 0
    INTERFACE = 1
    ABSTRACT = 2
    LIBRARY = 3

    @classmethod
    def token_to_enum(cls, token):
        if token not in cls.tokens:
            raise ParsingError(f"Failed to convert {token} to ContractType")
        return cls(cls.tokens.index(token))

    def __str__(self):
        return self.tokens[self.value]

    def __eq__(self, other):
        if isinstance(other, str):
            return str(self) == other
        return self == other

class Contract(Context):
    def __init__(self, ctx):    # ContractDefinitionContext 
        super().__init__(ctx)

        self._contract_type: ContractType = None

        self._name: Identifier = None
        self._constructor: Function = None
        self._receive: Function = None
        self._fallback: Function = None

        self._state_variables: List[StateVariable] = []
        self._structs:  List[Struct] = []
        self._modifiers: List[Function] = [] 
        self._functions: List[Function] = []
        self._events: List[Event] = []
        self._enums: List[Enum] = []
        self._custom_errors: List[CustomError] = []

        self._inheritance: List[Contract] = []

        self._using_for = []
        self._type_definitions = []

    @property
    def contract_type(self) -> ContractType:
        if not self._contract_type:
            contract_type_token = self.context.getChild(0).getText()
            self._contract_type = ContractType.token_to_enum(contract_type_token)
        return self._contract_type

    @property
    def name(self) -> Identifier:
        if not self._name:
            self._name = Identifier(self.context.identifier())
        return self._name

    @property
    def state_variables(self) -> List[StateVariable]:
        if not self._state_variables:
            for contract_part in self.context.contractPart():
                state_variable_declaration = contract_part.stateVariableDeclaration()
                if state_variable_declaration:
                    self._state_variables.append(StateVariable(state_variable_declaration))
                    
        return self._state_variables

    # TODO Still need to handle inheritanceSpecifiers (self.context.inheritanceSpecifier())