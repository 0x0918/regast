from typing import List

from regast.parsing.declarations.contract import Contract
from regast.parsing.declarations.custom_error import CustomError
from regast.parsing.declarations.enum import Enum
from regast.parsing.declarations.function import Function
from regast.parsing.declarations.import_directive import Import
from regast.parsing.declarations.pragma_directive import Pragma
from regast.parsing.declarations.struct import Struct
from regast.parsing.variables.constant import Constant

class SourceUnit:
    def __init__(self, ctx):
        self._pragma_directives: List[Pragma] = [Pragma(x) for x in ctx.pragmaDirective()]
        self._import_directives: List[Import] = [Import(x) for x in ctx.importDirective()]
        self._contracts: List[Contract] = [Contract(x) for x in ctx.contractDefinition()]
        self._enums: List[Enum] = [Enum(x) for x in ctx.enumDefinition()]
        self._structs: List[Struct] = [Struct(x) for x in ctx.structDefinition()]
        self._functions: List[Function] = [Function(x) for x in ctx.functionDefinition()]
        self._constants: List[Constant] = [Constant(x) for x in ctx.fileLevelConstant()]
        self._custom_errors: List[CustomError] = [CustomError(x) for x in ctx.customErrorDefinition()]

        self._type_definitions = []
        self._using_for = []