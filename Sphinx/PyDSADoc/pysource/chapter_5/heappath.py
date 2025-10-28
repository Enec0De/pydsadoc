#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Implementation of the question: Heap Path."""

from __future__ import annotations
from typing import Union, Optional

class MinHeap:

    def __init__(self):
        """Initialize an empty MinHeap."""
        self.data: list[Optional[int]] = [None]
        self.size: int = 0

    def make_heap_from_list(self, heap_list: list[int]) -> MinHeap:
        """Return the MinHeap itself."""
        temp: list[Optional[int]] = [None] + heap_list
        size = len(heap_list)
        self.size =size

        parent_index = size // 2

        # Make every subtree MinHeap
        while parent_index > 0:

            # Compare the child, make large item lower
            child = parent_index * 2
            while child <= size:
                # Chose the smaller child
                if child != size:
                    if temp[child] > temp[child+1]: # type: ignore
                        child += 1

                # Compared with his parent
                if temp[child//2] > temp[child]: # type: ignore
                    # Swap the elment
                    temp_item = temp[child]
                    temp[child] = temp[child//2]
                    temp[child//2] = temp_item

                    # Go to the next subtree
                    child *= 2
                else:
                    # Now, the subtree is MinHeap
                    break
            # Current subtree is MinHeap
            parent_index -= 1


        # Now the temp is MinHeap
        self.data = temp
        return self

    def find_path_from_index(self, index: int)-> list[int]:
        if index > self.size:
            raise IndexError('index out of range')
        path_list: list[int] = []
        data_list: list[int] = []

        while index > 0:
            path_list.append(index)
            index //= 2

        for i in path_list:
            data_list.append(self.data[i]) # type: ignore
        
        return data_list


def build_heap(heap_list) -> MinHeap:
    heap = MinHeap()
    heap.make_heap_from_list(heap_list)
    return heap

def find_path(heap, index) -> list[int]:
    return heap.find_path_from_index(index)


def main():
    prompt = 'L (list length) and S (number of element to search):'
    l, s = input(prompt).split(' ')
    heap_list = input('-->').split(' ')

    if len(heap_list) != int(l):
        raise IndexError('list lenght illegal')

    search_list = input('-->').split(' ')
    if len(search_list) != int(s):
        raise IndexError('search list illegal')


    min_heap = build_heap(heap_list)

    for index in search_list:
        print(find_path(min_heap, int(index)))

if __name__ =='__main__':
    main()