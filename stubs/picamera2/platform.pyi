from _typeshed import Incomplete
from enum import Enum

class Platform(Enum):
    VC4 = 0
    PISP = 1

device: Incomplete
caps: Incomplete
decoded: Incomplete

def get_platform(): ...
