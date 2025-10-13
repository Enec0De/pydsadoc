#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" The script contains 4 algorithmses."""

def algorithms1(arr: list) -> int:
    """Algorithms1: T(n)=O(), S(n)=O()
    """

    max_sum = current_sun = arr[0]

    for left_pos in arr:
        for right_pos in arr:
            pass
    return max_sum


def kadane(arr: list) -> int:
    """Kadane's Algorithm: T(n)=O(n), S(n)=O(1)

    :param arr: The array need to be caculated.
    :return: The max subsequence sum.
    """

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum