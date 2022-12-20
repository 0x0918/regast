from typing import List, Dict, Optional

from regast.exceptions import ParsingError
from regast.parsing.context.context import Context
from regast.parsing.expressions.identifier import Identifier

class Import(Context):
    def __init__(self, ctx):    # ImportDeclarationContext
        super().__init__(ctx)

        self._filename: str = None
        self._identifiers: List[Identifier] = []
        self._imported: List[str] = []
        self._renaming: Dict[str, str] = {}

        for import_declaration in ctx.importDeclaration():
            if len(import_declaration.children) == 1:
                self._imported.append(import_declaration.getText())
            elif len(import_declaration.children) == 3:
                imported, _, name = import_declaration.children

                self._imported.append(imported.getText())
                self._renaming[imported.getText()] = name.getText()
            else:
                raise ParsingError(f"Failed to parse import directive")

        if len(self._identifiers) > 1:
            ParsingError("Import directive has more than one identifier")

    @property
    def filename(self) -> str:
        if not self._filename:
            self._filename = self.context.importPath().getText().strip("\"")
        return self._filename

    @property
    def identifiers(self) -> List[Identifier]:
        if not self._identifiers:
            self._identifiers = [Identifier(x) for x in self.context.identifier()]
        return list(self._identifiers)

    @property
    def alias(self) -> Optional[str]:
        if self.identifiers:
            return self.identifiers[0]

    @property
    def imported_objects(self) -> List[str]:
        return list(self._imported)

    @property
    def imported_object_to_alias(self, imported_object: str) -> Optional[str]:
        if imported_object in self._renaming:
            return self._renaming[imported_object]

    def __str__(self):
        s = "import "
        if self.imported_objects:
            s += "{ "
            for imported_object in self.imported_objects:
                s += imported_object
                if imported_object in self._renaming:
                    s += " as " + self._renaming[imported_object]
                if imported_object != self.imported_objects[-1]:
                    s += ", "
            s += "} from"
        s += "\"" + self.filename + "\""
        if self.identifiers:
            s += " as " + str(self._identifiers[0])
        return s


