from typing import Dict
import tree_sitter as ts
from regast.core.declarations.comment import Comment

from regast.core.declarations.source_unit import SourceUnit
from regast.exceptions import ParsingException
from regast.parsing.declarations import DeclarationParser
from regast.parsing.tree_sitter_node import TreeSitterNode
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

    @staticmethod
    def convert_to_tree_sitter_node(node):
        tree_sitter_node = TreeSitterNode(node)
        for i in range(len(node.children)):
            child_node = node.children[i]
            if child_node.type == 'comment':
                tree_sitter_node._comments.append(Comment(child_node))
            else:
                child = Parser.convert_to_tree_sitter_node(child_node)
                tree_sitter_node.add_child(child)
                tree_sitter_node.extend_comments(child.comments)
                
        return tree_sitter_node

    def parse(self, fname: str):
        with open(fname, 'rb') as f:
            data = f.read()

        try:
            tree_sitter_tree = self.parser.parse(data)
        except Exception as e:
            raise ParsingException(f"Failed to parse {fname}, throws: {e}")

        root_node = Parser.convert_to_tree_sitter_node(tree_sitter_tree.root_node)
        self.fname_to_source_unit[fname] = DeclarationParser.parse_source_unit(root_node, fname)