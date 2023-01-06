from typing import Dict, List, Optional

from regast.core.declarations.comment import Comment


class TreeSitterNode:
    def __init__(self, node):
        self._underlying_node = node

        self._children: List["TreeSitterNode"] = []
        self._comments: List[Comment] = []
        
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
    def comments(self) -> List[Comment]:
        return list(self._comments)

    def add_child(self, child: "TreeSitterNode"):
        self._children.append(child)

    def extend_comments(self, comments: List[Comment]):
        self._comments.extend(comments)