#!/urs/bin/env python

from typing import TypeVar
from pydsadoc.sort._iscomparable import Comparable

import sys

print(sys.path)
# Define the element type of the list to be sorted 
# and the minimum run length.
T = TypeVar("T", bound=Comparable)
MINRUN: int = 32


# Calculate the suitable MINRUN for the arr.
# The function just like the math function ceil, for example:
# ceil(100.1) = 101 for binary.
def _calc_minrun(length: int) -> int:
    remainder = 0
    while length >= MINRUN:
        remainder |= length & 1
        length >>= 1
    return length + remainder


def _find_runs(arr: list[T], start: int) -> int:
    lenght = len(arr)
    end = start + 1

    # Check wether the arr is ascending or not.
    if end < lenght and arr[start] > arr[end]:
        # Descending
        while end < lenght and arr[end - 1] > arr[end]:
            end += 1
        arr[start : end] = reversed(arr[start : end])
    else:
        # Ascending.
        while end < lenght and arr[end - 1] <= arr[end]:
            end += 1

    # Go to the end of the run.
    return end


def _insertion(arr: list[T], left: int, right: int): ...
def _merge(arr: list[T], left: int, mid: int, right: int): ...


def tim_sort(arr: list[T]) -> None:
    """Sort a list of numbers in ascending order."""
    ...
