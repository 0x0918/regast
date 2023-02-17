from typing import Dict, List, Optional
from collections import defaultdict

import tree_sitter

from regast.core.others.comment import Comment
from regast.core.others.parse_error import ParseError


class ASTNode:
    def __init__(self, fname: str, node: tree_sitter.Node):
        self._fname: str = fname
        self._tree_sitter_node: tree_sitter.Node = node

        self._children: List[ASTNode] = []
        self._children_types: List[str] = []
        self._field_to_children: Dict[str, List[ASTNode]] = defaultdict(list)

        self._comments: List[Comment] = []
        self._parse_errors: List[ParseError] = []

        self.parse_underlying_node(node)
        
    @property
    def fname(self) -> str:
        return self._fname

    @property
    def tree_sitter_node(self) -> tree_sitter.Node:
        return self._tree_sitter_node

    @property
    def type(self) -> str:
        return self._tree_sitter_node.type

    @property
    def text(self) -> str:
        return self._tree_sitter_node.text.decode()

    @property
    def children(self) -> List["ASTNode"]:
        return list(self._children)

    @property
    def children_types(self) -> List[str]:
        return list(self._children_types)

    @property
    def comments(self) -> List[Comment]:
        return list(self._comments)

    @property
    def parse_errors(self) -> List[ParseError]:
        return list(self._parse_errors)

    def child_by_field_name(self, field: str) -> Optional["ASTNode"]:
        if field in self._field_to_children:
            return self._field_to_children[field][0]

    def children_by_field_name(self, field: str) -> List["ASTNode"]:
        return self._field_to_children[field]

    def parse_underlying_node(self, node):
        for i in range(len(node.children)):
            child_node = node.children[i]

            match child_node.type:
                case 'comment':
                    self._comments.append(Comment(child_node))
                case 'ERROR':
                    self._parse_errors.append(ParseError(child_node))
                case other:
                    self._children_types.append(other)

                    child = ASTNode(self.fname, child_node)
                    self._children.append(child)
                    self._comments.extend(child.comments)
                    self._parse_errors.extend(child.parse_errors)

                    field_name = node.field_name_for_child(i)
                    if field_name:
                        self._field_to_children[field_name].append(child)

