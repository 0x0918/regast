from typing import List, Optional

from regast.core.declarations.contracts.contract import Contract
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
from regast.core.expressions.identifier import Identifier
from regast.core.variables.state_variable import StateVariable

class Library(Contract):
    """
    Libraries do not have inheritance specifiers, unlike contracts and interfaces
    """
    def __init__(
        self,
        name: Identifier,
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
        super().__init__(
            name,
            abstract=abstract,
            constructor=constructor,
            fallback_function=fallback_function,
            receive_function=receive_function,
            functions=functions,
            modifiers=modifiers,
            structs=structs,
            enums=enums,
            type_definitions=type_definitions,
            state_variables=state_variables,
            events=events,
            custom_errors=custom_errors,
            using_directives=using_directives
        )