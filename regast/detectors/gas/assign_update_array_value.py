from typing import List

from regast.core.expressions.array_access import ArrayAccess
from regast.core.expressions.assignment_operation import AssignmentOperation
from regast.core.expressions.binary_operation import BinaryOperation
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class AssignUpdateArrayValue(Detector):
    NAME = 'Update array values using `arr[x] += y` instead of `arr[x] = arr[x] + y' 
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        results = []

        for source_unit in self.source_units:
            assignment_operations = source_unit.get_instances_of(AssignmentOperation)

            for assignment_operation in assignment_operations:
                if (
                    str(assignment_operation.operator) == '=' and
                    isinstance(assignment_operation.left_expression, ArrayAccess) and
                    isinstance(assignment_operation.right_expression, BinaryOperation)
                ):
                    binary_operation = assignment_operation.right_expression
                    if (
                        assignment_operation.left_expression == binary_operation.right_expression and
                        str(binary_operation.operator) in ["*", "/", "%", "+", "-", "<<", ">>", ">>>", "&", "^", "|"]
                    ):
                        result = self.generate_result_from_core_object(assignment_operation)
                        results.append(result)

        return results