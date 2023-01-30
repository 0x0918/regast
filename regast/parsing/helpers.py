
from typing import Callable, List, Optional, Tuple
from regast.core.expressions.expression import Expression
from regast.core.expressions.struct_expression import StructArguments
from regast.core.variables.parameter import Parameter
from regast.exceptions import ParsingException
from regast.parsing.expressions import ExpressionParser
from regast.parsing.tree_sitter_node import TreeSitterNode
from regast.parsing.variables import VariableParser

def extract_typed_nodes_between_brackets(
    node: TreeSitterNode,
    node_type: str,
    open_bracket: str,
    close_bracket: str,
    comma_separated: bool = True,
    parsing_function: Callable = lambda node: node,
) -> Tuple[List[TreeSitterNode], List[TreeSitterNode]]:
    """
    Iterates through child nodes of `node` and parses child nodes of `node_type` between `open_bracket` and `close_bracket`.
    """
    try:
        open_bracket_index = node.children_types.index(open_bracket)
        close_bracket_index = node.children_types.index(close_bracket)
    except ValueError:
        return [], node.children

    between_nodes = node.children[open_bracket_index:close_bracket_index+1]
    remaining_nodes = node.children[:open_bracket_index] + node.children[close_bracket_index+1:]

    parsed_nodes = []
    for child_node in between_nodes:
        if child_node.type == node_type:
            parsed_nodes.append(parsing_function(child_node))
        elif not (
            child_node.type in [open_bracket, close_bracket] or 
            (comma_separated and child_node.type == ',')
        ):
            raise ParsingException(f'Unknown tree-sitter node type while parsing {node.type}: {child_node.type}')

    return parsed_nodes, remaining_nodes

def extract_call_arguments(node: TreeSitterNode) -> Tuple[List[TreeSitterNode], List[Expression], Optional[StructArguments]]:
    call_argument_nodes, remaining_nodes = extract_typed_nodes_between_brackets(
        node, 'call_argument', '(', ')'
    )

    arguments = []
    struct_arguments = None

    for node in call_argument_nodes:
        call_argument = ExpressionParser.parse_call_argument(node)
        
        match call_argument:
            case Expression():
                arguments.append(call_argument)
            case StructArguments():
                assert not struct_arguments
                struct_arguments = call_argument
            # case _:
            #     raise ParsingException(f'Unknown resulting argument from call_argument: {node.text}')

        #TODO Implement expression parser and uncomment the exception above

    return arguments, struct_arguments, remaining_nodes

def extract_parameters(node: TreeSitterNode) -> Tuple[List[TreeSitterNode], List[Parameter]]:
    return extract_typed_nodes_between_brackets(
        node, 'parameter', '(', ')',
        parsing_function=VariableParser.parse_parameter
    )