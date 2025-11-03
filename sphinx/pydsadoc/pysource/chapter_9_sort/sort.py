#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Optional, Union


ElementType = Union[int]


def buble_sort(arr: list[ElementType]) -> None:
    length = len(arr)
    for _ in range(length-2):
        flag = 0
        for i in range(length-1):
            if arr[i] > arr[i+1]:
                # Swap the element
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

                # Set the flag
                flag = 1
        # It's an ordered list
        if flag == 0:
            break


def main():
    arr = [6, 5, 4, 3, 1, 2]
    buble_sort(arr)
    print(arr)

if __name__ == '__main__':
    main()