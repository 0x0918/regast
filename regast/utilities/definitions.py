import os
import sys

# Package paths
PACKAGE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
ROOT_DIR = os.path.abspath(os.path.join(PACKAGE_DIR, '..'))

# Tree sitter path
TREE_SITTER_SOLIDITY_LIBRARY_PATH = os.path.join(
    ROOT_DIR, 
    'build', 
    'solidity.dll' if sys.platform == 'win32' else 'solidity.so'
)