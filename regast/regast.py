from typing import Dict, List

from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result
from regast.parsing.parser import Parser

class Regast:
    def __init__(
        self, 
        fnames: List[str], 
        files_in_scope: List[str],
        remaps: Dict[str, str],
    ):
        self.fnames: List[str] = fnames
        self.files_in_scope: List[str] = files_in_scope

        self._detectors: List[Detector] = []

        self.parser = Parser()
        for fname in self.fnames:
            self.parser.parse(fname)
        
    def register_detector(self, detector_class: Detector):
        instance = detector_class(self.parser)
        self._detectors.append(instance)

    def run_detectors(self) -> Dict[DetectorClassification, Dict[Detector, Dict[str, List[Result]]]]:
        organized_results = {}
        
        for detector in self._detectors:
            results = detector.detect()
            
            for result in results:
                if detector.CLASSIFICATION not in organized_results:
                    organized_results[detector.CLASSIFICATION] = {}
                if detector not in organized_results[detector.CLASSIFICATION]:
                    organized_results[detector.CLASSIFICATION][detector] = {}
                if result.fname not in organized_results[detector.CLASSIFICATION][detector]:
                    organized_results[detector.CLASSIFICATION][detector][result.fname] = []
                organized_results[detector.CLASSIFICATION][detector][result.fname].append(result)

        return organized_results
        
