#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Optional, Union
import copy

ElementType = Union[int]


# -----------------------------------------------------------------------------
# Two Simple Sort Algorithms
def bubble_sort(arr: list[ElementType]) -> None:
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


# -----------------------------------------------------------------------------
# The Sedgewick Sequence and Shell Sort
def sedgewick(length: int) -> list[int]:
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

        result.sort(reverse=False)
    return result

def shell_sort(arr: list[ElementType]) -> None:
    length = len(arr)
    d_list = sedgewick(length)
    for d in d_list:

        # Insert sort
        for i in range(1, length, d):
            temp = arr[i]
            j = i - d
            while j >= 0 and arr[j] > temp:
                arr[j+d] = arr[j]
                j -= d
            arr[j+d] = temp


# -----------------------------------------------------------------------------
# The Selection Sort and imporved version by using heap
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


# -----------------------------------------------------------------------------
# The Merge Sort
def merge(arr: list[ElementType], temp: list[ElementType],
          l_ptr: int, r_ptr: int, end: int) -> None:

    start = l_ptr   
    right = r_ptr

    t_ptr = l_ptr

    while l_ptr < right and r_ptr < end:
        if arr[l_ptr] < arr[r_ptr]:
            temp[t_ptr] = arr[l_ptr]
            l_ptr += 1
            t_ptr += 1
        else:
            temp[t_ptr] = arr[r_ptr]
            r_ptr += 1
            t_ptr += 1

    while l_ptr < right:
        temp[t_ptr] = arr[l_ptr]
        l_ptr += 1
        t_ptr += 1

    while r_ptr < end:
        temp[t_ptr] = arr[r_ptr]
        r_ptr += 1
        t_ptr += 1

    for i in range(start, end):
        arr[i] = temp[i]

def merge_sort(arr: list[ElementType], temp: list[ElementType],
               start: int, end: int) -> None:
    if end - start > 1:
        center = (start+end) // 2
        merge_sort(arr, temp, start, center)
        merge_sort(arr, temp, center, end)
        merge(arr, temp, start, center, end)

def merge_sort_recursion(arr: list[ElementType]) -> None:
    length = len(arr)
    temp = [-999] * length
    merge_sort(arr, temp, 0, length)

def merge_temp(arr: list[ElementType], temp: list[ElementType],
               l_ptr: int, r_ptr: int, end: int) -> None:

    t_ptr = l_ptr
    right = r_ptr
    while l_ptr < right and r_ptr < end:
        if arr[l_ptr] < arr[r_ptr]:
            temp[t_ptr] = arr[l_ptr]
            l_ptr, t_ptr = l_ptr + 1, t_ptr + 1
        else: 
            temp[t_ptr] = arr[r_ptr]
            r_ptr, t_ptr = r_ptr + 1, t_ptr + 1
    
    while l_ptr < right:
        temp[t_ptr] = arr[l_ptr]
        l_ptr, t_ptr = l_ptr + 1, t_ptr + 1

    while r_ptr < end:
        temp[t_ptr] = arr[r_ptr]
        r_ptr, t_ptr = r_ptr + 1, t_ptr + 1


def merge_sort_temp(arr: list[ElementType], temp: list[ElementType],
                    sub_len: int) -> None:
    length = len(arr)
    i = 0
    while i <= length - 2*sub_len:
        merge_temp(arr, temp, i, i+sub_len, i+2*sub_len)
        i += 2*sub_len

    if length - i > sub_len:
        merge_temp(arr, temp, i, i+sub_len, length)
    else: 
        while i < length:
            temp[i] = arr[i]
            i += 1

def merge_sort_non_recursion(arr: list[ElementType]) -> None:
    length = len(arr)
    temp = [0] * length

    sub_len = 1
    while sub_len < length:
        merge_sort_temp(arr, temp, sub_len)
        sub_len *= 2
        merge_sort_temp(temp, arr, sub_len)
        sub_len *= 2


# -----------------------------------------------------------------------------
# The entry point of the module
def main():
    arr = [6, 5, 4, 3, 1, 2, 7, 8, 9, 0, -1, -4, 100, -99, 0]
    print(arr)

    arr_buble = copy.copy(arr)
    bubble_sort(arr_buble)
    print('# -- BUBBLE SORT -------------------------------------------------')
    print(arr_buble)

    arr_insert= copy.copy(arr)
    insert_sort(arr_insert)
    print('# -- INSERT SORT -------------------------------------------------')
    print(arr_insert)

    arr_shell= copy.copy(arr)
    shell_sort(arr_shell)
    print('# -- SHELL SORT --------------------------------------------------')
    print(arr_shell)

    arr_selection= copy.copy(arr)
    selection_sort(arr_selection)
    print('# -- SELECTION SORT ----------------------------------------------')
    print(arr_selection)

    arr_heap= copy.copy(arr)
    heap_sort(arr_heap)
    print('# -- HEAP SORT ---------------------------------------------------')
    print(arr_heap)

    arr_heap_opt= copy.copy(arr)
    heap_sort_opt(arr_heap_opt)
    print('# -- HEAP OPTIMIZED SORT -----------------------------------------')
    print(arr_heap_opt)
    
    arr_merge= copy.copy(arr)
    merge_sort_recursion(arr_merge)
    print('# -- MERGE RECURSION SORT ----------------------------------------')
    print(arr_merge)

    arr_merge_n= copy.copy(arr)
    merge_sort_non_recursion(arr_merge_n)
    print('# -- MERGE NON RECURSION SORT ------------------------------------')
    print(arr_merge_n)

if __name__ == '__main__':
    main()