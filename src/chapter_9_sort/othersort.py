#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Optional, Union
from collections import deque
from heapq import heapify, heappop, heappush
import weakref
import copy

ElementType = Union[int]

# -----------------------------------------------------------------------------
# Quick Sort
def median3(arr: list[ElementType], left: int, right: int) -> ElementType:
    center = (left+right) // 2
    if arr[left] > arr[center]:
        arr[left], arr[center] = arr[center], arr[left]
    if arr[left] > arr[right]:
        arr[left], arr[right] = arr[right], arr[left]
    if arr[center] > arr[right]:
        arr[center], arr[right] = arr[right], arr[center]

    arr[center], arr[right-1] = arr[right-1], arr[center]
    return arr[right-1]


def quick_sort_inner(arr: list[ElementType], left: int, right: int) -> None:
    if right - left > 1:
        pivot = median3(arr, left, right)
        i, j = left + 1, right - 2
        while True:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i, j = i + 1, j - 1 
            else:
                break

        arr[i], arr[right-1] = arr[right-1], arr[i]
        quick_sort_inner(arr, left, i-1)
        quick_sort_inner(arr, i+1, right)
    if right - left == 1 and arr[right] < arr[left]:
        arr[left], arr[right] = arr[right], arr[left]


def quick_sort(arr: list[ElementType]) -> None:
    length = len(arr)
    quick_sort_inner(arr, 0, length-1)


# ----------------------------------------------------------------------------
# The content of Table Sorting and Physical Sorting is omitted               |
# ----------------------------------------------------------------------------

def table_sort(arr) -> None:
    ...

def physcial_sort(arr)-> None:
    ...


# ----------------------------------------------------------------------------
# Bucket Sort 
# Radix Sort

def bucket_sort(arr: list) -> None:
    ...

def least_significant_digit(arr) -> None:
    ...

def most_significant_digitl(arr) -> None:
    ...

def main():
    # arr = [6, 5, 4, 3, 1, 2, 7, 8, 9, 0, -1, -4, 100, -99, 0]
    # arr_quick = copy.copy(arr)
    # quick_sort(arr_quick)
    # print(arr_quick)

    arr_test = [7, 1, 2, 8, 0]
    quick_sort(arr_test)
    print(arr_test)


if __name__ == '__main__':
    main()