from enum import Enum

class DetectorClassification(Enum):
    GAS = 1
    QA = 2
    LOW = 3
    MEDIUM = 4
    HIGH = 5

class Detector:
    NAME: str = None
    CLASSIFICATION: DetectorClassification = None