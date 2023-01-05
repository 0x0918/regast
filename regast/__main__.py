#!/usr/bin/env python3

import inspect
from typing import Dict, List

from regast.detectors import all_detectors
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result
from regast.regast import Regast
from regast.utilities.command_line import handle_arguments
from regast.utilities.output import output_to_stdout
from regast.utilities.setup_dependencies import initialize_dependencices


def get_detectors():
    return [x[1] for x in inspect.getmembers(all_detectors, inspect.isclass) if issubclass[x[1], Detector]]

def get_results_from_ast(
    source_fnames: List[str], 
    files_in_scope: List[str],
    remaps: Dict[str, str],
) -> Dict[DetectorClassification, Dict[Detector, List[Result]]]:
    # Initialize regast class, which parses ast
    regast = Regast(source_fnames, files_in_scope, remaps)

    # Run detectors and filter results
    for detector in get_detectors():
        regast.register_detector(detector)

    results = regast.run_detectors()
    return results

def main():
    # Parse arguments from command line
    args = handle_arguments()

    # Run detectors
    results = get_results_from_ast(args.contract, args.scope, args.remap)

    # Output results to stdout
    output_to_stdout(results)

if __name__ == '__main__':
    initialize_dependencices()
    main()