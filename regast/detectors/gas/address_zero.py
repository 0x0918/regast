from typing import List
from regast.core.expressions.member_access import MemberAccess
from regast.core.expressions.type_cast_expression import TypeCastExpression
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result

# TODO: This implementation is wrong, also check that all instances of type_cast_expression is actually found

class AddressZero(Detector):
    NAME = 'Use assembly to check for `address(0)`'
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        results = []

        for source_unit in self.source_units:
            type_cast_instances = source_unit.get_instances_of(TypeCastExpression)

            for type_cast_expression in type_cast_instances:
                if str(type_cast_expression.type) == 'address': # and str(type_cast_expression.casted_expression) == '0':
                    result = self.generate_result_from_core_object(type_cast_expression)
                    results.append(result)


        return results