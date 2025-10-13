#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""" The script contains 4 algorithmses."""


def algorithms1(arr: list[int]) -> int:
    """Algorithms1: T(n) = O(n^3), S(n) = O(1).

    :param arr: The array need to be caculated.
    :return: The max subsequence sum.
    """
    max_sum = arr[0]
    n = len(arr)

    for left_pos in range(0, n):
        for right_pos in range(left_pos, n):
            current_sum = sum(arr[left_pos:right_pos + 1])
            max_sum = max(max_sum, current_sum)

    return max_sum


def algorithms2(arr: list[int]) -> int:
    """Algorithms2: T(n) = O(n^2), S(n) = O(1).
    
    :param arr: The array need to be caculated.
    :return: The max subsequence sum.
    """
    max_sum = arr[0]
    n = len(arr)

    for left_pos in range(0, n):
        current_sum = 0
        for right_pos in range(left_pos, n):
            # Substitute `sum' to add one item.
            current_sum += arr[right_pos]
            max_sum = max(max_sum, current_sum)

    return max_sum


def algorithms3(arr: list[int]) -> int:
    """Algorithms3 (Divide and Conquer): T(n) = O(n log n), S(n) = O(log n).

    :param arr: The array need to be caculated.
    :return: The max subsequence sum.
    """
    n = len(arr)

    # Directly retrun the element.
    if n == 1:
        return arr[0]

    # Left and right subsequence
    center = n // 2
    left = algorithms3(arr[:center])
    right = algorithms3(arr[center:])

    # Border subsequence
    left_current_sum = 0
    left_max_sum = arr[center - 1]
    for i in range(center, 0, -1):
        left_current_sum += arr[i - 1]
        left_max_sum = max(left_max_sum, left_current_sum)

    right_current_sum = 0
    right_max_sum = arr[center]
    for j in range(center, n):
        right_current_sum += arr[j]
        right_max_sum = max(right_max_sum, right_current_sum)

    boder= left_max_sum + right_max_sum
    max_sum = max(left, right, boder)

    return max_sum


def kadane(arr: list[int]) -> int:
    """Kadane's Algorithm (Dynamic Programming): T(n) = O(n), S(n) = O(1).

    :param arr: The array need to be caculated.
    :return: The max subsequence sum.
    """
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum