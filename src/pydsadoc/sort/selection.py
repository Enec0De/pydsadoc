#!/usr/bin/env python

from __future__ import annotations

__all__ = ['selection_sort']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union

# Define ElementType.
ElementType = Union[int]


# Implementation of Selection Sort.
def selection_sort(arr: list[ElementType]) -> None:
    """Sort a list of numbers in ascending order.

    Not Stable.  Best Case: :math:`O(n^2)`.  Average Case:
    :math:`O(n^2)`.  Worse Case: :math:`O(n^2)`.
    """
    length = len(arr)
    for i in range(length-1):

        # Find minimun element in the unsorted list.
        index = i
        for j in range(i+1, length):
            if arr[index] > arr[j]:
                index = j
        else:
            arr[i], arr[index] = arr[index], arr[i]


def main() -> None:
    # Create random list.
    arr = [random.randint(-9, 99) for _ in range(random.randint(1, 10))]
    print(arr)

    # Sort array.
    selection_sort(arr)
    print(arr)

    # Assertion test.
    for i in range(len(arr)-1):
        assert arr[i] <= arr[i+1]


if __name__ == '__main__':
    main()
