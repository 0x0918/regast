from typing import Dict

from regast.core.declarations.source_unit import SourceUnit

class Parser:
    """
    Parsers should inherit this class and implement the parse_source_file() function,
    which takes in a source file (fname) and does the following:
    - Parses it into a SourceUnit
    - Adds it to self.fname_to_source_unit[fname]

    See tree_sitter_parser.py for reference
    """
    def __init__(self):
        self.fname_to_source_unit: Dict[str, SourceUnit] = {}
    
    """
    Move the following to base detector?

    @property
    def fnames(self) -> List[str]:
        return list(self.fname_to_source_unit.keys())

    @property
    def source_units(self) -> List[SourceUnit]:
        return list(self.fname_to_source_unit.values())

    @property
    def get_source_unit_by_fname(self, fname: str) -> Optional[SourceUnit]:
        if fname in self.fname_to_source_unit:
            return self.fname_to_source_unit[fname]
    """

    def parse_source_file(self, fname: str):
        raise NotImplementedError(f"parse_file() not implemented for {self.__class__.__name__}")
