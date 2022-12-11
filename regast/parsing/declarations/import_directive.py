from typing import List, Dict, Optional

from regast.exceptions import ParsingError

class Import:
    def __init__(self, ctx):
        self._filename: str = ctx.importPath().getText().strip("\"")
        self._identifiers: List[str] = [x.getText() for x in ctx.identifier()]
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
        return self._filename

    @property
    def identifiers(self) -> str:
        return self._identifiers

    @property
    def alias(self) -> Optional[str]:
        if self._identifiers:
            return self._identifiers[0]

    @property
    def imported_objects(self) -> List[str]:
        return self._imported

    @property
    def imported_object_to_alias(self, imported_object: str) -> Optional[str]:
        if imported_object in self._renaming:
            return self._renaming[imported_object]

    def __str__(self):
        s = "import "
        if self._imported:
            s += "{ "
            for imported_object in self._imported:
                s += imported_object
                if imported_object in self._renaming:
                    s += " as " + self._renaming[imported_object]
                if imported_object != self._imported[-1]:
                    s += ", "
            s += "} from"
        s += "\"" + self._filename + "\""
        if self._identifiers:
            s += " as " + self._identifiers[0]
        return s


