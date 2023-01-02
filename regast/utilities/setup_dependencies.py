import os
import sys
import subprocess
from tree_sitter import Language

from regast.utilities.definitions import ROOT_DIR

def setup_antlr4():
    solidity_grammar_path = os.path.join(ROOT_DIR, 'third_party', 'antlr', 'Solidity.g4')
    output_directory = os.path.join(ROOT_DIR, 'build', 'solidity_antlr4')

    if not os.path.exists(output_directory):
        subprocess.run(['antlr4', '-Dlanguage=Python3', solidity_grammar_path, '-o', output_directory, '-visitor'])

def setup_treesitter():
    global SOLIDITY_LANGUAGE

    if sys.platform == "win32":
        library_name = "solidity.dll"
    else:
        library_name = "solidity.so"

    library_path = os.path.join(ROOT_DIR, 'build', library_name)
    tree_sitter_solidity_path = os.path.join(ROOT_DIR, 'third_party', 'tree-sitter-solidity')

    Language.build_library(library_path, tree_sitter_solidity_path)
    SOLIDITY_LANGUAGE = Language(library_path, 'solidity')