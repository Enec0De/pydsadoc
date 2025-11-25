#!/usr/bin/env python

from __future__ import annotations

__all__ = ['selection_srot']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional

# Define ElementType.
ElementType = Union[int]

def selection_srot(arr: list[ElementType]) -> None:
    """The Selection Sort Algorithm.
    
    Time complexity is :math:`O(n^2)`.  It is **not stable**.
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
    arr = [random.randint(-9,99) for _ in range(random.randint(1,10))]
    print(arr)

    # Sort array.
    selection_srot(arr)
    print(arr)

    # Assertion test.
    for i in range(len(arr)-1):
        assert arr[i] <= arr[i+1]


if __name__ == '__main__':
    main()