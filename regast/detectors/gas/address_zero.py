from typing import List

from regast.core.expressions.binary_operation import BinaryOperation
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class AddressZero(Detector):
    NAME = 'Use assembly to check for `address(0)`'
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        results = []

        # Iterate through all source units
        for source_unit in self.source_units:
            # Find all instances binary operations
            binary_operations = source_unit.get_instances_of(BinaryOperation)

            for binary_operation in binary_operations:
                # Filter binary operations with '==" or "!=" and have "address(0)" on either side
                if (
                    str(binary_operation.operator) in ['==', '!='] and
                    'address(0)' in [str(binary_operation.left_expression), str(binary_operation.right_expression)]
                ):
                    result = self.generate_result_from_core_object(binary_operation)
                    results.append(result)

        return results