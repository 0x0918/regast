from typing import List

from regast.core.expressions.member_access import MemberAccess
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class AddressBalance(Detector):
    NAME = 'Use `selfbalance()` instead of `address(this).balance`'
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        results = []

        for source_unit in self.source_units:
            member_access_instances = source_unit.get_instances_of(MemberAccess)

            for member_access in member_access_instances:
                if str(member_access.object) == 'address(this)' and str(member_access.member) == 'balance':
                    result = self.generate_result_from_core_object(member_access)
                    results.append(result)

        return results