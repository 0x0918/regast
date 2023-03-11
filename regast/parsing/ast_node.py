from typing import List, Optional

import tree_sitter


class ASTNode:
    def __init__(self, fname: str):
        self._fname: str = fname
        self._tree_sitter_node: Optional[tree_sitter.Node] = None
        
        self._children: List[ASTNode] = []
        self._children_types: List[str] = []

    @staticmethod
    def from_tree_sitter_node(fname: str, node: tree_sitter.Node) -> 'ASTNode':
        ast_node = ASTNode(fname)
        ast_node._tree_sitter_node = node
        
        for child_node in node.children:
            if child_node.type not in ['comment', 'ERROR']:
                ast_node._children_types.append(child_node.type)

                child_ast_node = ASTNode.from_tree_sitter_node(fname, child_node)
                ast_node._children.append(child_ast_node)
        
        return ast_node

    @property
    def fname(self) -> str:
        return self._fname

    @property
    def tree_sitter_node(self) -> Optional[tree_sitter.Node]:
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
    
    def is_ancestor_of(self, child: tree_sitter.Node) -> bool:
        """
        Check if this node is an ancestor of child  
        """
        start_point_is_before = (
            self.tree_sitter_node.start_point[0] < child.tree_sitter_node.start_point[0] or
            self.tree_sitter_node.start_point[0] == child.tree_sitter_node.start_point[0] and
            self.tree_sitter_node.start_point[1] <= child.tree_sitter_node.start_point[1]
        )
        
        end_point_is_after = (
            self.tree_sitter_node.end_point[0] > child.tree_sitter_node.end_point[0] or
            self.tree_sitter_node.end_point[0] == child.tree_sitter_node.end_point[0] and
            self.tree_sitter_node.end_point[1] >= child.tree_sitter_node.end_point[1]
        )

        return start_point_is_before and end_point_is_after
    
    def is_descendant_of(self, parent: tree_sitter.Node) -> bool:
        """
        Check if this node is a descendant of parent 
        """
        return parent.is_ancestor_of(self)