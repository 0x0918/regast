from typing import List

from regast.core.types.elementary_type import ElementaryType
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class BoolStorage(Detector):
    NAME = 'Using `bool` for storage incurs overhead' 
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        # Checks for bool in a state variable's type
        def has_bool_in_type(state_variable):
            elementary_types = state_variable.type.get_instances_of(ElementaryType)
            return any(str(et) == 'bool' for et in elementary_types)

        results = []

        for source_unit in self.source_units:
            for contract in source_unit.all_contracts:
                bool_state_variables = filter(has_bool_in_type, contract.state_variables)
                results.extend(bool_state_variables)

        return self.generate_results_from_core_objects(results)