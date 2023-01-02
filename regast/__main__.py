#!/usr/bin/env python3

import inspect
from typing import Dict, List

from regast.utilities.setup_dependencies import setup_antlr4, setup_treesitter
from regast.utilities.command_line import handle_arguments
from regast.detectors import all_detectors
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result
from regast.regast import Regast
from regast.utilities.output import output_to_stdout

def get_results_from_ast(
    detectors: List[Detector], 
    contract_fnames: List[str], 
    files_in_scope: List[str]
) -> Dict[DetectorClassification, Dict[Detector, List[Result]]]:
    # Initialize regast class, which parses ast
    regast = Regast(contract_fnames, files_in_scope)

    # Run detectors and filter results
    for detector in detectors:
        regast.register_detector(detector)

    results = regast.run_detectors()
    return results

def get_detectors():
    return [x[1] for x in inspect.getmembers(all_detectors, inspect.isclass) if issubclass[x[1], Detector]]

def main():
    # Parse arguments from command line
    contract_fnames, files_in_scope, remappings = handle_arguments()

    # Get detectors and run them to get results
    detectors = get_detectors()
    results = get_results_from_ast(detectors, contract_fnames, files_in_scope)

    # Output results to stdout
    output_to_stdout(results)

if __name__ == '__main__':
    setup_treesitter()
    # main()