#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Optional, Union
import copy

ElementType = Union[int]


def buble_sort(arr: list[ElementType]) -> None:
    length = len(arr)
    for p in range(length, 1, -1):
        flag = 0
        for i in range(p-1):
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


def insert_sort(arr: list[ElementType]) -> None:
    length = len(arr)
    for i in range(1, length):
        temp = arr[i]
        for j in range(i, 0, -1):
            if temp < arr[j-1]:
                arr[j] = arr[j-1]
            else:
                j += 1
                break
        arr[j-1] = temp



def main():
    arr = [6, 5, 4, 3, 1, 2, 7, 8, 9, 0, -1, -4, 100, -99, 0]
    print(arr)

    arr_buble = copy.copy(arr)
    buble_sort(arr_buble)
    print(arr_buble)

    arr_insert= copy.copy(arr)
    insert_sort(arr_insert)
    print(arr_insert)

if __name__ == '__main__':
    main()