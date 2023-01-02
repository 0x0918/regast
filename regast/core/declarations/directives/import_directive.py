from typing import List, Dict, Optional, Union

from regast.core.core import Core
from regast.core.expressions.identifier import Identifier

class Import(Core):
    def __init__(
        self,
        import_path: str,
        imported: List[Identifier],
        alias: Optional[Identifier] = None,
        renaming: Dict[Identifier, Identifier] = {},
    ):
        super().__init__()

        self._import_path: str = import_path
        self._imported: List[Identifier] = imported
        self._alias: Optional[Identifier] = alias
        self._renaming: Dict[Identifier, Identifier] = renaming

    @property
    def import_path(self) -> str:
        return self._import_path

    @property
    def imported_objects(self) -> List[Identifier]:
        return list(self._imported)

    @property
    def alias(self) -> Optional[Identifier]:
        return self._alias

    @property
    def renaming(self) -> Dict[Identifier, Identifier]:
        return dict(self._renaming)

    @property
    def imported_object_to_alias(self, imported_object: Union[str, Identifier]) -> Optional[Identifier]:
        if imported_object in self._renaming:
            return self._renaming[imported_object]

    def __eq__(self, other):
        if isinstance(other, Import):
            return self.import_path == other.import_path and self.imported_objects == other.imported_objects and self.alias == other.alias and self.renaming == other.renaming
        return False