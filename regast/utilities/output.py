from typing import Dict, List

from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result

def format_fname_to_results(fname_to_results: Dict[str, List[Result]]) -> str:
    formatted_fname_results = []
    for fname, results in fname_to_results.items():
        s = f'{fname}:\n'

        sorted_results = sorted(results, key=lambda r: r.start_line)
        s += '\n'.join(r.code for r in sorted_results)

        formatted_fname_results.append(s)

    return '\n'.join(formatted_fname_results)

def output_to_stdout(results: Dict[DetectorClassification, Dict[Detector, Dict[str, List[Result]]]]):
    formatted_classification_results = []
    for classification, detector_to_results in results.items():
        classification_str = '-'*20 + ' '
        classification_str += str(classification).split('.')[1]
        classification_str += ' ' + '-'*20 + '\n'

        formatted_detector_results = []
        for detector, fname_to_results in detector_to_results.items():
            result_count = sum([len(r) for r in fname_to_results.values()])
            detector_str = f'{detector.NAME} ({result_count})\n'
            detector_str += format_fname_to_results(fname_to_results)
            
            formatted_detector_results.append(detector_str)
        
        classification_str += '\n'.join(formatted_detector_results)
        formatted_classification_results.append(classification_str)

    print('\n'.join(formatted_classification_results))
            
def output_to_markdown(result: Dict[str, List[Result]]):
    pass