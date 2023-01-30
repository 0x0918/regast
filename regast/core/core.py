from typing import List, Union

from regast.parsing.ast_node import ASTNode


class Core:
    def __init__(self, node: ASTNode):
        self._ast_node: ASTNode = node 

    @property
    def ast_node(self) -> ASTNode:
        return self._ast_node

    @property
    def children(self) -> List:
        return []

    def get_instances_of(self, *core_types: List[Union[str, type]]) -> Union[List, List[List]]:
        """
        TODO
        We can optimize this further by introducing memoization. The function below allows us to get the
        parent classes of an object, which we can then store in a Dict[type, List[object]]. When
        get_instances_of() is called for the first time, we iterate through all children and create this dict.
        Future calls will then just reference this dict.

        This method will return nested types, such as an expression in an expression, is this a pro/con?

        Pros:
        - O(1) for subsequent runs

        Cons:
        - Uses a lot of memory, each core object will have to store its own dict. Unless we find a way to store only
          one copy of this dict and all objects to reference that one dict.
        - Will be initially slower for shallow calls, such as querying for statements in a function.

        def unwrap_classes(c): # where c is a type, such as LocalVariable
            return [c.__name__] + unwrap_classes(c.__bases__[0]) if c != Core else []
        """

        """
        Returns all child instances of core types specified
        - Each core type can either be a class or str (LocalVariable, "LocalVariable")
        - If only 1 core type is provided, returns a single list
        - If multiple core types are provided, returns a list of lists in the same order

        Examples:
        local_variables = a.get_instances_of(LocalVariable)
        local_variables, state_variables = a.get_instances_of(LocalVariable, "StateVariable")
        """
        instances = [[] for _ in range(len(core_types))]
        
        for child in self.children:
            # Check if child matches any of the core types
            for i in range(len(core_types)):
                core_type = core_types[i]
                if child.__class__.__name__ == str(core_type) or isinstance(child, core_type):
                    instances[i].append(child)
            
            # Recursively do this for children too, and add the results to our current ones
            child_instances = child.get_instances_of(*core_types)
            if len(core_types) == 1:            
                child_instances = [child_instances]
            instances = [instances[x] + child_instances[x] for x in range(len(core_types))]
        
        # Remove duplicates
        instances = [list(set(x)) for x in instances]         

        # Return a single list if only one core type is specified
        return instances[0] if len(core_types) == 1 else instances

    def __hash__(self):
        return hash(self.ast_node)