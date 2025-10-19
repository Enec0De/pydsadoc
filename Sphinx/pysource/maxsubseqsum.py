#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def brute_force_enumeration(arr: list[int]) -> int:
    """The brute force enumeration method.
    
    Time complexity is :math:`O(n^3)`. Space complexity is :math:`O(1)`.

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


def optimized_enumeration(arr: list[int]) -> int:
    """Optimizes the way of sum from brute force enumeration.
    
    Time complexity is :math:`O(n^2)`. Space complexity is :math:`O(1)`.
    
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


def divide_and_conquer(arr: list[int]) -> int:
    r"""The Divide and Conquer algorithm.
     
    Time complexity is :math:`O(n \log n)`. Space complexity is 
    :math:`O(\log n)`.

    :param arr: The array need to be caculated.
    :return: The max subsequence sum.
    """
    n = len(arr)

    # Directly retrun the element.
    if n == 1:
        return arr[0]

    # Left and right subsequence
    center = n // 2
    left = divide_and_conquer(arr[:center])
    right = divide_and_conquer(arr[center:])

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


def dynamic_programming(arr: list[int]) -> int:
    """The Kadane's Algorithm (Dynamic Programming).
     
    Time complexity is :math:`O(n)`. Space complexity is :math:`O(1)`.

    :param arr: The array need to be caculated.
    :return: The max subsequence sum.
    """
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum