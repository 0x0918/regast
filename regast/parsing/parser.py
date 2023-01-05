from typing import Dict
import tree_sitter as ts

from regast.core.declarations.source_unit import SourceUnit
from regast.exceptions import ParsingException
from regast.parsing.declarations import DeclarationParser
from regast.utilities.definitions import TREE_SITTER_SOLIDITY_LIBRARY_PATH


class Parser:
    def __init__(self):
        super().__init__()

        self.fname_to_source_unit: Dict[str, SourceUnit] = {}

        # Initialize parser
        solidity_language = ts.Language(TREE_SITTER_SOLIDITY_LIBRARY_PATH, 'solidity')
        parser = ts.Parser()
        parser.set_language(solidity_language)

        self.parser = parser

    def parse(self, fname: str):
        with open(fname, 'rb') as f:
            data = f.read()

        try:
            tree_sitter_tree = self.parser.parse(data)
        except Exception as e:
            raise ParsingException(f"Failed to parse {fname}, throws: {e}")

        self.fname_to_source_unit[fname] = DeclarationParser.parse_source_unit(
            fname, 
            tree_sitter_tree.root_node
        )