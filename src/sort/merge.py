#!/usr/bin/env python

from __future__ import annotations

__all__ = ['merge_sort']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional

# Define ElementType
ElementType = Union[int]


# Implementation of Merge Sort.
def merge_sort(arr: list[ElementType]) -> None:
    r"""Sort a list of numbers in ascending order.
        
    Stable.  Best Case: :math:`O(n \log n)`.  Average Case:
    :math:`O(n \log n)`.  Worst Case: :math:`O(n \log n)`.
    
    Space complexity is :math:`O(n)`.
    """
    length = len(arr)
    temp = [0] * length
    _merge_divide(arr, temp, 0, length)


# Divide the array into two parts and merge them.
def _merge_divide(arr: list[ElementType], temp: list[ElementType],
           start: int, end: int) -> None:
    length = end - start

    # Divide the array if the list length large than 1.
    # The array whose length less than or equal 1 is sorted well.
    if length > 1:
        mid = start + length//2
        _merge_divide(arr, temp, start, mid)
        _merge_divide(arr, temp, mid, end)
        _merge_conquer(arr, temp, start, mid, end)


# Comquer and Merge the two given lists IN PLACE.
def _merge_conquer(arr: list[ElementType], temp: list[ElementType],
                   left: int, right: int, end: int) -> None:
    ptr_l, ptr_r, ptr_t = left, right, left

    # Merge the two lists until one of them is empty.
    while ptr_l < right and ptr_r < end:
        if arr[ptr_l] <= arr[ptr_r]:
            temp[ptr_t] = arr[ptr_l]
            ptr_t, ptr_l = ptr_t+1, ptr_l+1
        else:
            temp[ptr_t] = arr[ptr_r]
            ptr_t, ptr_r = ptr_t+1, ptr_r+1

    # Add the rest element into the temp.
    while ptr_l < right:
        temp[ptr_t] = arr[ptr_l]
        ptr_t, ptr_l = ptr_t+1, ptr_l+1
    while ptr_r < end:
        temp[ptr_t] = arr[ptr_r]
        ptr_t, ptr_r = ptr_t+1, ptr_r+1

    # Write back to the array.
    for i in range(left, end):
        arr[i] = temp[i]


# Entry point with simple testing.
def main() -> None:
    # Create random list.
    arr = [random.randint(-9,99) for _ in range(random.randint(1,20))]
    print(arr)

    # Merge Sort.
    merge_sort(arr)
    print(arr)

    # Assertion test.
    for i in range(len(arr)-1):
        assert arr[i] <= arr[i+1]


if __name__ == '__main__':
    main()