#!/usr/bin/env python

from functools import total_ordering
from typing import Protocol


# Define the class check wether the Type can be sorted.
@total_ordering
class Comparable(Protocol):
    def __eq__(self, other: "Comparable") -> bool: ...
    def __lt__(self, other: "Comparable") -> bool: ...