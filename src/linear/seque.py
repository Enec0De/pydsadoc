#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union
import random

ElementType = Union[None, int]
MAXSIZE = 2**63 - 1

class SeqList:
    """Implement a linear list sequentially."""

    def __getitem__(self, key: int, /) -> ElementType:
        """Return self[key]"""
        if key < 0 or key > self.size - 1:
            raise IndexError('index out of range.')
        return self.data[key]

    def __init__(self, maxsize: int = 16, /, *args, **kwargs) -> None:
        """Initialize self."""
        # Maxsize of the SeqList
        self.maxsize = maxsize

        # The number of element
        self.size = 0

        # The list stores the data
        self.data: list[ElementType] = [None] * self.maxsize

    def __str__(self, /) -> str:
        """Implement print method."""
        return '[' + ', '.join(map(str, self.data[:self.size])) + ']'
    
    def append(self, object: ElementType, /) -> None:
        """Append object to the end of the list.
        
        Time complexity is :math:`O(1)`.
        """
        # Appending
        self.data[self.size] = object
        self.size += 1

        # Atuo extend
        if self.size > self.maxsize -1:
            self.data += [None] * self.maxsize
            self.maxsize *= 2

    def index(self, 
              value: ElementType, 
              start: int = 0, 
              stop: int = MAXSIZE, /) -> int:
        """Retrun first index of the value.
        
        Time complexity is :math:`O(n)`.
        """
        # Adjust range of index
        if stop > self.size:
            stop = self.size
            
        # Retrieve for value
        for i in range(start, stop):
            if self.data[i] == value:
                return i

        # Not found
        return -1

    def insert(self, index: int, object: ElementType, /) -> None:
        """Insert object before index."""
        ...
    
    def pop(self, index: int = -1, /) -> ElementType:
        """Remove and return item at index (deafult last).
        
        Time complexity is :math:`O(n)`.
        """
        # Raise empty list error
        if self.size < 1:
            raise IndexError('empty list.')

        # Default value of index
        if index == -1:
            index += self.size

        # Firstly, the item to be poped
        item, self.data[index] = self.data[index], None

        # Secondly, move backward all elements after index
        for i in range(index, self.size-1):
            self.data[i] = self.data[i+1]

        # Thirdly, size minus 1 and delete the last element
        self.size -= 1
        self.data[self.size] = None
        
        # Finally, Return the item
        return item

    def remove(self, value: ElementType, /) -> None:
        """Remove first occurrence of value.
        
        Time complexity is :math:`O(n)`.
        """
        # Find the value
        i = 0
        while self.data[i] != value and i <= self.size-1:
            i += 1

        # Delete the value
        if i <= self.size-1:
            for j in range(i, self.size-1):
                self.data[j] = self.data[j+1]
            self.size -= 1
            self.data[self.size] = None
        else:
            raise IndexError('not found.')
    

        

# - Test module -----------------------------------------------------------
def check_equal(arr: list[int], other: SeqList) -> None:
    assert len(arr) == other.size
    for i in range(len(arr)):
        assert arr[i] == other[i]

def main() -> None:
    # - Initialize the test data ------------------------------------------ 
    arr = [1, 5, 8, 4, 0, 33, 2, 5, 3, 7, 9, 6, 11, 13, 17, 22, 17]
    seqlist = SeqList()
    sample = list()

    # - Test append method ------------------------------------------------
    for item in arr:
        seqlist.append(item)
        sample.append(item)
    check_equal(sample, seqlist)

    # - Test auto extend --------------------------------------------------
    assert seqlist.maxsize <= seqlist.size * 2

    # - Test index method -------------------------------------------------
    index_sample = random.choice(sample)
    assert seqlist.index(index_sample) == sample.index(index_sample)

    # - Test pop method ---------------------------------------------------
    random_loops = random.randint(1, len(sample)//2)
    for _ in range(random_loops):
        assert seqlist.pop() == sample.pop()

    # - Test remove method ------------------------------------------------
    remove_sample = random.choice(sample)
    seqlist.remove(remove_sample)
    sample.remove(remove_sample)
    check_equal(sample, seqlist)

    print('All test OK!')

if __name__ == '__main__':
    main()