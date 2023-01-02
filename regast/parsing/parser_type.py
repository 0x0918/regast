from enum import Enum
from regast.exceptions import RegastException

from regast.parsing.parser import Parser
from regast.parsing.tree_sitter.tree_sitter_parser import TreeSitterParser

class ParserType(str, Enum):
    TREE_SITTER = "treesitter"
    ANTLR = "antlr"

    @staticmethod
    def get_parser_from_type(parser_type) -> Parser:
        if parser_type == ParserType.TREE_SITTER:
            return TreeSitterParser()
        elif parser_type == ParserType.ANTLR:
            raise NotImplementedError("antlr parser not implemented.")

        raise RegastException(f'Unable to find parser for {parser_type.value}')
