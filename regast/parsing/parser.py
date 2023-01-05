import tree_sitter as ts

from regast.exceptions import ParsingException
from regast.parsing.declarations import TreeSitterDeclarations
from regast.utilities.definitions import TREE_SITTER_SOLIDITY_LIBRARY_PATH


class Parser:
    def __init__(self):
        super().__init__()

        # Initialize parser
        solidity_language = ts.Language(TREE_SITTER_SOLIDITY_LIBRARY_PATH, 'solidity')
        parser = ts.Parser()
        parser.set_language(solidity_language)

        self.parser = parser

    def parse_source_file(self, fname: str):
        with open(fname, 'rb') as f:
            data = f.read()

        try:
            tree_sitter_tree = self.parser.parse(data)
        except Exception as e:
            raise ParsingException(f"Failed to parse {fname}, throws: {e}")

        self.fname_to_source_unit[fname] = TreeSitterDeclarations.parse_source_unit(tree_sitter_tree)