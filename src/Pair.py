from typing import TypeVar, Generic

_T1 = TypeVar('T1')
_T2 = TypeVar('T2')


class pair(Generic[_T1, _T2]):

    def __init__(self, t1: _T1, t2: _T2):
        self.first = t1
        self.second = t2
