from typing import List

from regast.core.common import Visibility
from regast.core.variables.state_variable import StateVariableMutability
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class PrivateConstant(Detector):
    NAME = 'Declare constants as `private` instead of non-public to save gas' 
    CLASSIFICATION = DetectorClassification.GAS

    def detect(self) -> List[Result]:
        # Checks for non-private state variables that are constants
        def is_non_private_constant(state_variable):
            return (
                state_variable.mutability == StateVariableMutability.CONSTANT and
                state_variable.visibility != Visibility.PRIVATE
            )
        
        results = []

        for source_unit in self.source_units:
            for contract in source_unit.all_contracts:
                non_constant_state_variables = filter(
                    is_non_private_constant, 
                    contract.state_variables
                )
                results.extend(non_constant_state_variables)

        return self.generate_results_from_core_objects(results)