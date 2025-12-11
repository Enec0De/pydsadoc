#!/usr/bin/env python

from functools import total_ordering
from typing import Protocol, Any


# Define the class check wether the Type can be sorted.
@total_ordering
class Comparable(Protocol):
    def __eq__(self, other: Any, /) -> bool: ...
    def __lt__(self, other: Any, /) -> bool: ...