from enum import Enum
from functools import total_ordering

'''
    Enumeration for detection levels
'''


@total_ordering
class DetectionLevel(Enum):
    NONE = 0
    LOW = 1
    HIGH = 2

    '''
        implements comparison between DetectionLevels according to its value
    '''
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented
