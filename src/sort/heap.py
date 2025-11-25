#!/usr/bin/env python

from __future__ import annotations

__all__ = ['heap_sort']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional

# Define ElementType.
ElementType = Union[int]


def heap_sort(arr: list[ElementType]) -> None:
    r"""The Heap Sort Algorithm.
    
    Time complexity is :math:`O(n \log n)`.  It is **not stable**.
    """
    length = len(arr) - 1
    _heapify(arr)
    arr[0], arr[length] = arr[length], arr[0]

    # Down the a[0].
    while length > 0:
        temp = arr[0]
        parent = 0

        # Heapify the sub sequence unsorted.
        while (child := 2*parent+ 1) < length:

            # Chose the large one.
            if child != length - 1 and arr[child] < arr[child+1]:
                child += 1

            # Compare the child and the parent.
            if arr[child] > temp:
                arr[parent] = arr[child]
                parent = child
            else:
                break

        arr[parent] = temp

        # Go to the next loop.
        length -= 1
        arr[0], arr[length] = arr[length], arr[0]


def _heapify(arr: list[ElementType]) -> None:
    length = len(arr)

    # Heapify the tree.
    root = (length-2) // 2
    while root >= 0:
        parent = root
        temp = arr[parent]

        # Check the sub tree
        while (child := parent*2 + 1) < length:

            # Two steps to heapify the sub tree.
            # 1. Chose the large one.
            if child != length-1 and arr[child] < arr[child+1]:
                child += 1
            # 2. Compare the child and the parent.
            # 2a. The child is larger than parent.
            if arr[child] > temp:
                arr[parent] = arr[child]
                parent = child
            # 2b. The child is smaller than parent.
            else:
                break

        arr[parent] = temp
        root -= 1


def main() -> None:

    # Test heapify.
    arr = [random.randint(-9,99) for _ in range(random.randint(1,20))]
    _heapify(arr)
    for i in range(len(arr)):
        if 2*i + 1 < len(arr):
            assert arr[i] >= arr[2*i+1]
        if 2*i + 2 < len(arr):
            assert arr[i] >= arr[2*i+2]

    # Test heap_sort.
    arr = [random.randint(-9,99) for _ in range(random.randint(1,20))]
    heap_sort(arr)
    for i in range(len(arr)-1):
        assert arr[i] <= arr[i+1]
    

if __name__ == '__main__':
    main()
