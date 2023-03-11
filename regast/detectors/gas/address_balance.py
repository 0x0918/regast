from typing import List

from regast.core.expressions.call_expression import CallExpression
from regast.core.expressions.member_access import MemberAccess
from regast.detectors.detector import Detector, DetectorClassification
from regast.detectors.result import Result


class AddressBalance(Detector):
    NAME = 'Use `selfbalance()` instead of `address(this).balance`'
    CLASSIFICATION = DetectorClassification.GAS
    DESCRIPTION = "Use assembly when getting a contract's balance of ETH.\n\nYou can use `selfbalance()` instead of `address(this).balance` when getting your contract's balance of ETH to save gas.\nAdditionally, you can use `balance(address)` instead of `address.balance()` when getting an external contract's balance of ETH.\n\n*Saves 15 gas when checking internal balance, 6 for external*"

    def detect(self) -> List[Result]:
        # Checks if member access is address(...).balance
        def is_address_balance(member_access):
            return (
                str(member_access.member) == 'balance' and
                isinstance(call_expresion := member_access.object, CallExpression) and 
                str(call_expresion.function_name) == 'address'
            )

        results = []

        for source_unit in self.source_units:
            member_accesses = source_unit.get_instances_of(MemberAccess)
            member_accesses = filter(is_address_balance, member_accesses)
            results.extend(member_accesses)

        return self.generate_results_from_core_objects(results)