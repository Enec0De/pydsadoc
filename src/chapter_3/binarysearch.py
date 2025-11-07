#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations


def binary_search(list: list[int], data: int) -> int:
    """Find data in the given ordered list.
    
    :param list: The list in which we find data.
    :param data: The data to search.
    """
    # Left and right indexes
    left: int = 0
    right: int = len(list)

    # Search until the left index larger than right
    while left <= right:
        # The middle index of left and right
        mid: int = (left + right) // 2

        # Check the data
        if data < list[mid]:
            right = mid - 1
        elif data > list[mid]:
            left = mid + 1
        else:
            return mid
    
    raise IndexError('the data not found.')
