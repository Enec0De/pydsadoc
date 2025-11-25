#!/usr/bin/env python

from __future__ import annotations

__all__ = ['bubble_sort']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional

# Define the ElementType
ElementType = Union[int]


# Implementation of Bubble Sort.
def bubble_sort(arr: list[ElementType]) -> None:
    """Average Case: :math:`O(n^2)` and Stable.  Best Case: :math:`O(n)`.
    """
    length = len(arr)
    for j in range(length-1, 0, -1):
        swapped = False
        for i in range(j):

            # Swap the elements.
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break


# Entry point with simple testing.
def main() -> None:
    # Create random list.
    arr = [random.randint(-9, 99) for _ in range(random.randint(1,10))]
    print(arr)

    # Sort the array by using bubble_sort.
    bubble_sort(arr)
    print(arr)

    # Assertion test.
    for i in range(len(arr)-1):
        assert arr[i] <= arr[i+1]


if __name__ == '__main__':
    main()