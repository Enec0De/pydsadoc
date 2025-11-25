#!/usr/bin/env python

from __future__ import annotations

__all__ = ['insertion_sort']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional

# Define the ElementType
ElementType = Union[int]


# Implementation of Insertion Sort.
def insertion_sort(arr: list[ElementType]) -> None:
    """Average Case: :math:`O(n^2)` and Stable.  Best Case: :math:`O(n)`.
    """
    length = len(arr)
    for i in range(1, length):
        temp = arr[i]
        j = 1

        # Insert the element into the list that has been sorted.
        while i - j >= 0 and arr[i-j] > temp:
            arr[i-j+1] = arr[i-j]
            j += 1
        else:
            arr[i-j+1] = temp


# Entry point with simple testing.
def main() -> None:
    # Create random list.
    arr = [random.randint(-9,99) for _ in range(random.randint(1,10))]
    print(arr)

    # Sort array.
    insertion_sort(arr)
    print(arr)

    # Assertion test.
    for i in range(len(arr)-1):
        assert arr[i] <= arr[i+1]


if __name__ == '__main__':
    main()
