from typing import List

from regast.parsing.context.context import Context
from regast.parsing.declarations.contract import Contract
from regast.parsing.declarations.custom_error import CustomError
from regast.parsing.declarations.enum import Enum
from regast.parsing.declarations.function import Function
from regast.parsing.declarations.import_directive import Import
from regast.parsing.declarations.pragma_directive import Pragma
from regast.parsing.declarations.struct import Struct
from regast.parsing.variables.constant import Constant

class SourceUnit(Context):
    def __init__(self, ctx):    # SourceUnitContext
        super().__init__(ctx)

        self._pragma_directives: List[Pragma] = []
        self._import_directives: List[Import] = []
        self._contracts: List[Contract] = []
        self._enums: List[Enum] = []
        self._structs: List[Struct] = []
        self._functions: List[Function] = []
        self._constants: List[Constant] = []
        self._custom_errors: List[CustomError] = []

        self._type_definitions = []
        self._using_for = []

        print(self.contracts[0].state_variables[0].type)

    @property
    def pragma_directives(self) -> List[Pragma]:
        if not self._pragma_directives:
            self._pragma_directives = [Pragma(x) for x in self.context.pragmaDirective()]
        return list(self._pragma_directives)

    @property
    def import_directives(self) -> List[Import]:
        if not self._import_directives:
            self._import_directives = [Import(x) for x in self.context.importDirective()]
        return list(self._import_directives)

    @property
    def contracts(self) -> List[Contract]:
        if not self._contracts:
            self._contracts = [Contract(x) for x in self.context.contractDefinition()]
        return list(self._contracts)

    @property
    def enums(self) -> List[Enum]:
        if not self._enums:
            self._enums = [Enum(x) for x in self.context.enumDefinition()]
        return list(self._enums)

    @property
    def structs(self) -> List[Struct]:
        if not self._structs:
            self._structs = [Struct(x) for x in self.context.structDefinition()]
        return list(self._structs)

    @property
    def functions(self) -> List[Function]:
        if not self._functions:
            self._functions = [Function(x) for x in self.context.functionDefinition()]
        return list(self._functions)

    @property
    def constants(self) -> List[Constant]:
        if not self._constants:
            self._constants = [Constant(x) for x in self.context.fileLevelConstant()]
        return list(self._constants)

    @property
    def custom_errors(self) -> List[CustomError]:
        if not self._custom_errors:
            self._custom_errors = [CustomError(x) for x in self.context.customErrorDefinition()]
        return list(self._custom_errors)
