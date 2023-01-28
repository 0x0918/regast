
from typing import List, Optional, Tuple
from regast.core.expressions.expression import Expression
from regast.core.expressions.struct_expression import StructArguments
from regast.exceptions import ParsingException
from regast.parsing.expressions import ExpressionParser
from regast.parsing.tree_sitter_node import TreeSitterNode

def extract_call_arguments(node_list: List[TreeSitterNode]) -> Tuple[List[Expression], Optional[StructArguments]]:
    """
    Iterates through `node_list` and parses regular and struct arguments.
    Returns `node_list` without `_call_arguments`

    This relies on finding the index of characters "(" and ")" to determine when the 
    call arguments start and end.
    """
    arguments: List[Expression] = []
    struct_arguments: Optional[StructArguments] = None

    open_bracket_index = close_bracket_index = len(node_list)
    for i in range(len(node_list)):
        node = node_list[i]
        match node.type:
            case 'call_argument':
                call_argument = ExpressionParser.parse_call_argument(node) 
                if isinstance(call_argument, Expression):
                    arguments.append(call_argument)
                elif isinstance(call_argument, StructArguments):
                    assert not struct_arguments 
                    struct_arguments = call_argument
                # else:
                #     raise ParsingException(f'Unknown resulting argument from call_argument: {node.text}')

                #TODO Implement expression parser and uncomment the exception above

            case '(':
                open_bracket_index = i
            
            case ')':
                close_bracket_index = i

            case ',':
                pass

            case other if open_bracket_index != len(node_list):
                raise ParsingException(f'Unknown tree-sitter node type for call_arguments: {other}')

    return node_list[:open_bracket_index] + node_list[close_bracket_index+1:], arguments, struct_arguments