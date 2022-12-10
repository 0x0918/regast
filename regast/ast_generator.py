import os
import sys
from tree_sitter import Language, Parser

from regast.utilities.definitions import ROOT_DIR

def initialize_parser():
    if sys.platform == "win32":
        executable_name = "solidity.dll"
    else:
        executable_name = "solidity.so"

    executable_path = os.path.join(ROOT_DIR, 'build', executable_name)
    tree_sitter_solidity_path = os.path.join(ROOT_DIR, 'third_party', 'tree-sitter-solidity')

    Language.build_library(executable_path, tree_sitter_solidity_path)
    SOLIDITY_LANGUAGE = Language(executable_path, 'solidity')

    parser = Parser()
    parser.setLanguage(SOLIDITY_LANGUAGE)

    return parser