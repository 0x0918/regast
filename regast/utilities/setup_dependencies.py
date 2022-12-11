import os
import subprocess

from regast.utilities.definitions import ROOT_DIR, PACKAGE_DIR

def setup_antlr4():
    solidity_grammar_path = os.path.join(ROOT_DIR, 'third_party', 'antlr', 'Solidity.g4')
    output_directory = os.path.join(PACKAGE_DIR, 'parsing', 'solidity_antlr4')

    if not os.path.exists(output_directory):
        subprocess.run(['antlr4', '-Dlanguage=Python3', solidity_grammar_path, '-o', output_directory, '-visitor'])
        open(os.path.join(output_directory, '__init__.py'), 'w')