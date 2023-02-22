from typing import List

from regast.core.expressions.update_operation import UpdateOperation
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class PostIncrement(Detector):
    NAME = '`++i` costs less gas than `i++`, especially when used in `for`-loops (`--i`/`i--` too)' 
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        results = []

        for source_unit in self.source_units:
            update_operations = source_unit.get_instances_of(UpdateOperation)
            postfix_update_operations = [uo for uo in update_operations if not uo.is_prefix]
            results.extend(postfix_update_operations)

        return self.generate_results_from_core_objects(postfix_update_operations)