#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Optional, Union
import copy

ElementType = Union[int]


def buble_sort(arr: list[ElementType]) -> None:
    length = len(arr)
    for p in range(length, 1, -1):
        flag = False
        for i in range(p-1):
            if arr[i] > arr[i+1]:
                # Swap the element
                arr[i], arr[i+1] = arr[i+1], arr[i]

                # Set the flag
                flag = True
        # It's an ordered list
        if flag == False:
            break


def insert_sort(arr: list[ElementType]) -> None:
    length = len(arr)
    for i in range(1, length):
        temp = arr[i]
        j = i - 1
        while j >= 0 and temp < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp


def shell_sort(arr: list[ElementType]) -> None:
    length = len(arr)
    d = length // 2
    while d > 0:

        # Insert sort
        for i in range(1, length, d):
            temp = arr[i]
            j = i - d
            while j >= 0 and arr[j] > temp:
                arr[j+d] = arr[j]
                j -= d
            arr[j+d] = temp

        d //= 2


def sedgewicka(length: int) -> list[int]:
    result = []
    for i in range(length):
        gap_m = 9*4**i - 9*2**i + 1
        gap_a = 4**i - 3*2**i + 1
        if 0 < gap_m < length:
            result.append(gap_m)
        if 0 < gap_a < length:
            result.append(gap_a)
        
        if gap_a >= length and gap_m >= length:
            break

        result.sort()
    return result


def selection_sort(arr: list[ElementType]) -> None:
    length = len(arr)
    for i in range(length-1):
        min_index = arr.index(min(arr[i:]), i)
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


def heapify(arr: list[ElementType], length: Optional[int] = None) -> None:
    if length == None:
        length = len(arr)
    parent = (length-2) // 2
    while parent >= 0:
        temp = arr[parent]
        child = parent*2 + 1
        while child < length:
            if child != length - 1:
                if arr[child] > arr[child+1]:
                    child += 1 
                
            if temp > arr[child]:
                arr[(child-1)//2] = arr[child]
                # arr[(child-1)//2], arr[child] = arr[child], arr[(child-1)//2]

                child = child*2 + 1
            else:
                break

        arr[(child-1)//2] = temp
        parent -= 1

def heappop(arr: list[ElementType]) -> ElementType: 
    retval = arr[0]
    length = len(arr) - 1
    temp = arr[length]
    child = 1
    while child < length:
        if child != length - 1:
            if arr[child] > arr[child+1]:
                child += 1
        
        if temp > arr[child]:
            arr[(child-1)//2] = arr[child] 
            child = child*2 + 1
        else:
            break
    arr[(child-1)//2] = temp

    del arr[length]
    return retval

def heap_sort(arr: list[ElementType]) -> None: 
    length = len(arr)
    arr_heap = copy.copy(arr)
    heapify(arr_heap)
    for i in range(length):
        arr[i] = heappop(arr_heap)

def heap_sort_opt(arr: list[ElementType]) -> None:
    length = len(arr)
    heapify(arr)
    for i in range(length-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i)
    arr.reverse()



def main():
    arr = [6, 5, 4, 3, 1, 2, 7, 8, 9, 0, -1, -4, 100, -99, 0]
    print(arr)

    arr_buble = copy.copy(arr)
    buble_sort(arr_buble)
    print(arr_buble)

    arr_insert= copy.copy(arr)
    insert_sort(arr_insert)
    print(arr_insert)

    arr_shell= copy.copy(arr)
    print(sedgewicka(10000))
    shell_sort(arr_shell)
    print(arr_shell)

    arr_selection= copy.copy(arr)
    selection_sort(arr_selection)
    print(arr_selection)

    arr_heap= copy.copy(arr)
    heap_sort(arr_heap)
    print(arr_heap)

    arr_heap_opt= copy.copy(arr)
    heap_sort_opt(arr_heap_opt)
    print(arr_heap_opt)

if __name__ == '__main__':
    main()