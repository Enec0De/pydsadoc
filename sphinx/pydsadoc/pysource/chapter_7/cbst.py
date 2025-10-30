#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional
from collections import deque
import weakref
from math import log, floor



def complete_binary_search_tree(data_list: list[int]) -> list:
    """Build bst from data_list."""

    data_list.sort()
    queue = deque()
    queue.append(data_list)
    result = []

    while queue:
        current_list = queue.popleft()

        # Judge the number of the nodes of the root
        n = len(current_list)

        # Only one element
        if n == 1:
            result.append(current_list[0])
            continue
            
        # Judge the index of element to be append
        k = n.bit_length() - 1
        if n < 2**k + 2**(k-1):
            index: int = n - 2**(k-1)
        else:
            index: int  = 2**k - 1

        # Stores the root data into the result
        result.append(current_list[index])

        # Process the left sub tree 
        if current_list[:index]:
            queue.append(current_list[:index])

        # Process the right sub tree
        if current_list[index+1:]:
            queue.append(current_list[index+1:])

    return result

    








def main():
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    result = complete_binary_search_tree(input_list)
    output_list = [6, 3, 8, 1, 5, 7, 9, 0, 2, 4]
    print(result)
    print(output_list)

if __name__ == '__main__':
    main()