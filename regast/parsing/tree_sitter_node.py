from typing import Dict, List, Optional
from collections import defaultdict

from regast.core.others.comment import Comment
from regast.core.others.parse_error import ParseError


class TreeSitterNode:
    def __init__(self, node):
        self._underlying_node = node

        self._children: List[TreeSitterNode] = []
        self._children_types: List[str] = []
        self._field_to_children: Dict[str, List[TreeSitterNode]] = defaultdict(list)

        self._comments: List[Comment] = []
        self._parse_errors: List[ParseError] = []

        self.parse_underlying_node(node)
        
    @property
    def underlying_node(self):
        return self._underlying_node

    @property
    def type(self) -> str:
        return self._underlying_node.type

    @property
    def text(self) -> str:
        return self._underlying_node.text.decode()

    @property
    def children(self) -> List["TreeSitterNode"]:
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

    def child_by_field_name(self, field: str) -> Optional["TreeSitterNode"]:
        if field in self._field_to_children:
            return self._field_to_children[field][0]

    def children_by_field_name(self, field: str) -> List["TreeSitterNode"]:
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

                    child = TreeSitterNode(child_node)
                    self._children.append(child)
                    self._comments.extend(child.comments)
                    self._parse_errors.extend(child.parse_errors)

                    field_name = node.field_name_for_child(i)
                    if field_name:
                        self._field_to_children[field_name].append(child)

