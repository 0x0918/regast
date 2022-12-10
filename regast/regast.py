from typing import Dict, List
from tree_sitter import Tree

from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result
from regast.parsing.parser import Parser

class Regast:
    def __init__(
        self, 
        fnames: List[str], 
        files_in_scope: List[str],
        fname_to_ast: Dict[str, Tree]
    ):
        self.fnames: List[str] = fnames
        self.files_in_scope: List[str] = files_in_scope
        self.fname_to_ast: Dict[str, Tree] = fname_to_ast

        self._detectors: List[Detector] = []

        self.parser: Parser = Parser()
        for fname, tree in self.fname_to_ast.items():
            self.parser.parse_ast(fname, tree)

    def register_detector(self, detector_class: Detector):
        instance = detector_class(self)
        self._detectors.append(instance)

    def run_detectors(self) -> Dict[DetectorClassification, Dict[Detector, List[Result]]]:
        classification_to_detector_to_results = {c: {} for c in DetectorClassification}
        for detector in self._detectors:
            results = detector.detect()
            if results:
                classification_to_detector_to_results[detector.CLASSIFICATION][detector] = results

        return classification_to_detector_to_results
