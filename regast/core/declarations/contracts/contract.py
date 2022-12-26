from typing import List, Optional

from regast.core.core import Core
from regast.core.declarations.custom_error import CustomError
from regast.core.declarations.enum import Enum
from regast.core.declarations.event import Event
from regast.core.declarations.functions.constructor import Constructor
from regast.core.declarations.functions.fallback_function import FallbackFunction
from regast.core.declarations.functions.function import Function
from regast.core.declarations.functions.modifier import Modifier
from regast.core.declarations.functions.receive_function import ReceiveFunction
from regast.core.declarations.struct import Struct
from regast.core.declarations.type_definition import TypeDefinition
from regast.core.directives.using_directive import UsingDirective
from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.expressions.struct_expression import StructArguments
from regast.core.types.user_defined_type import UserDefinedType
from regast.core.variables.state_variable import StateVariable


class InheritanceSpecifier(Core):
    def __init__(
        self, 
        name: UserDefinedType,
        struct_arguments: Optional[StructArguments] = None,
        arguments: List[Expression] = [],
    ):
        super().__init__()

        self._name: UserDefinedType = name
        self._struct_arguments: Optional[StructArguments] = struct_arguments
        self._arguments: List[Expression] = arguments

    @property
    def name(self) -> str:
        return ".".join([str(x) for x in self.identifiers])

    @property
    def struct_arguments(self) -> Optional[StructArguments]:
        return self._struct_arguments

    @property
    def arguments(self) -> List[Expression]:
        return list(self._arguments)

class Contract(Core):
    def __init__(
        self,
        name: Identifier,
        inheritance_specifiers: List[InheritanceSpecifier] = [],
        abstract: bool = False,
        
        constructor: Optional[Constructor] = None,
        fallback_function: Optional[FallbackFunction] = None,
        receive_function: Optional[ReceiveFunction] = None,
        functions: List[Function] = [],
        modifiers: List[Modifier] = [],

        structs: List[Struct] = [],
        enums: List[Enum] = [],
        type_definitions: List[TypeDefinition] = [],
        state_variables: List[StateVariable] = [],
        events: List[Event] = [],
        custom_errors: List[CustomError] = [],
        using_directives: List[UsingDirective] = [],
    ):
        super().__init__()
        
        self._name: Identifier = name
        self._inheritance_specifiers: List[InheritanceSpecifier] = inheritance_specifiers
        self._abstract: bool = abstract

        self._constructor: Optional[Constructor] = constructor
        self._fallback_function: Optional[FallbackFunction] = fallback_function
        self._receive_function: Optional[ReceiveFunction] = receive_function
        self._functions: List[Function] = functions
        self._modifiers: List[Modifier] = modifiers

        self._structs: List[Struct] = structs
        self._enums: List[Enum] = enums
        self._type_definitions: List[TypeDefinition] = type_definitions
        self._state_variables: List[StateVariable] = state_variables
        self._events: List[Event] = events
        self._custom_errors: List[CustomError] = custom_errors
        self._using_directives: List[UsingDirective] = using_directives

    @property
    def name(self) -> Identifier:
        return self._name
        
    @property
    def inheritance_specifiers(self) -> List[InheritanceSpecifier]:
        return list(self._inheritance_specifiers)
        
    @property
    def is_abstract(self) -> bool:
        return self._abstract
        
    @property
    def constructor(self) -> Optional[Constructor]:
        return self._constructor
        
    @property
    def fallback_function(self) -> Optional[FallbackFunction]:
        return self._fallback_function
        
    @property
    def receive_function(self) -> Optional[ReceiveFunction]:
        return self._receive_function
        
    @property
    def functions(self) -> List[Function]:
        return list(self._functions)
        
    @property
    def modifiers(self) -> List[Modifier]:
        return list(self._modifiers)

    @property
    def all_functions(self) -> List[Function]:
        """
        All functions, inclusive of modifiers, constructor, receive and fallback functions
        """
        return self.functions + self.modifiers + [x for x in [self.constructor, self.fallback_function, self.receive_function] if x]
        
    @property
    def structs(self) -> List[Struct]:
        return list(self._structs)
        
    @property
    def enums(self) -> List[Enum]:
        return list(self._enums)
        
    @property
    def type_definitions(self) -> List[TypeDefinition]:
        return list(self._type_definitions)
        
    @property
    def state_variables(self) -> List[StateVariable]:
        return list(self._state_variables)
        
    @property
    def events(self) -> List[Event]:
        return list(self._events)
        
    @property
    def custom_errors(self) -> List[CustomError]:
        return list(self._custom_errors)
        
    @property
    def using_directives(self) -> List[UsingDirective]:
        return list(self._using_directives)
            
    def __eq__(self, other):
        if isinstance(other, Contract):
            return (
                self.name == other.name and
                self.inheritance_specifiers == other.inheritance_specifiers and
                self.is_abstract == other.is_abstract and
                self.constructor == other.constructor and
                self.fallback_function == other.fallback_function and
                self.receive_function == other.receive_function and
                self.functions == other.functions and
                self.modifiers == other.modifiers and
                self.structs == other.structs and
                self.enums == other.enums and
                self.type_definitions == other.type_definitions and
                self.state_variables == other.state_variables and
                self.events == other.events and
                self.custom_errors == other.custom_errors and
                self.using_directives == other.using_directives
            )
        return False