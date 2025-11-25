#!/usr/bin/env python

from __future__ import annotations

__all__ = ['quick_sort']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional

# Define ElementType
ElementType = Union[int]


# Implementation of Quick Sort.
def quick_sort(arr: list[ElementType]) -> None:
    r"""Sort a list of numbers in ascending order.
    
    Not Stable.  Best Case: :math:`O(n \log n)`.  Average Case:
    :math:`O(n \log n)`.  Worst Case: :math:`O(n^2)`.
    
    Space complexity is :math:`O(\log n)`.
    """
    length = len(arr)
    _partition(arr, 0, length)


# Method for finding pivot.
def _median_of_three(arr: list[ElementType], start: int, end: int) -> None:
    # Do nothing with list that has only one eleement or is empty.
    if end - start <= 1:
        return

    # Now arr[start] <= arr[end].
    # The '-1' enables the _median_of_three to sort the list
    # with only two elements.
    mid = (start+end-1) // 2
    if arr[start] > arr[end-1]:
        arr[start], arr[end-1] = arr[end-1], arr[start]

    # Rerange the order of three element.
    # The low, med, high elements are in the position
    # start, end-2, end-1 respectively.
    if arr[mid] < arr[start]:
        arr[mid], arr[start] = arr[start], arr[mid]
    elif arr[mid] > arr[end-1]:
        arr[mid], arr[end-1] = arr[end-1], arr[mid]
    arr[mid], arr[end-2] = arr[end-2], arr[mid]


# Hoare's Partition Scheme.
def _partition(arr: list[ElementType], start: int, end: int) -> None:

    _median_of_three(arr, start, end)

    # Operation after _median_of_three.
    if end - start >= 3:
        # Initialize the left and right pointer.
        pivot = arr[end-2]
        low = start + 1
        high = end - 3

        # Insert the pivot into the correct position.
        # When the element equals to the pivot, the pointers
        # low and high should swap the them.
        while True:
            while low <= end - 3 and arr[low] < pivot:
                low += 1
            while high >= start + 1 and arr[high] > pivot:
                high -= 1
            if low < high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low+1, high-1
            else:
                break
        
        # Process the sorting recursively.
        arr[low], arr[end-2] = arr[end-2], arr[low]
        _partition(arr, start, low)
        _partition(arr, low+1, end)

    # Do not process the sorting.
    else:
        return


def main() -> None:
    # Create random list.
    arr_2 = [random.randint(-9,99) for _ in range(2)]
    arr_3 = [random.randint(-9,99) for _ in range(3)]

    # Test _median_of_three.
    _median_of_three(arr_2, 0, 2)
    _median_of_three(arr_3, 0, 3)
    assert arr_2[0] <= arr_2[1]
    assert arr_3[0] <= arr_3[1] <= arr_3[2]

    # Create random list.
    arr = [random.randint(-9,99) for _ in range(random.randint(1,20))]

    # Quick Sort.
    quick_sort(arr)
    for i in range(len(arr)-1):
        assert arr[i] <= arr[i+1]


if __name__ == '__main__':
    main()
