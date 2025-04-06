from enum import Enum

class SinkType(Enum):
    STDOUT = "STDOUT"
    FILE = "FILE"
    DATABASE = "DATABASE"
