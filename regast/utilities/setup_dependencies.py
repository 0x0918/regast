import os
import subprocess
from tree_sitter import Language

from regast.utilities.definitions import ROOT_DIR, TREE_SITTER_SOLIDITY_LIBRARY_PATH

def setup_antlr4():
    solidity_grammar_path = os.path.join(ROOT_DIR, 'third_party', 'antlr', 'Solidity.g4')
    output_directory = os.path.join(ROOT_DIR, 'build', 'solidity_antlr4')

    if not os.path.exists(output_directory):
        subprocess.run(['antlr4', '-Dlanguage=Python3', solidity_grammar_path, '-o', output_directory, '-visitor'])

def setup_treesitter():
    tree_sitter_solidity_path = os.path.join(ROOT_DIR, 'third_party', 'tree-sitter-solidity')
    
    if not os.path.exists(TREE_SITTER_SOLIDITY_LIBRARY_PATH):
        Language.build_library(TREE_SITTER_SOLIDITY_LIBRARY_PATH, [tree_sitter_solidity_path])

def initialize_dependencices():
    # setup_antlr4()
    setup_treesitter()