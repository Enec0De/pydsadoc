#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union
import random

ElementType = Union[None, int]
MAXSIZE = 2**63 - 1

class SeqList:
    """Implement a linear list sequentially."""

    def __init__(self, maxsize: int = 16, /, *args, **kwargs) -> None:
        """Initialize self."""
        # Maxsize of the SeqList
        self.maxsize = maxsize

        # The number of element
        self.size = 0

        # The list stores the data
        self.data: list[ElementType] = [None] * self.maxsize

    def __getitem__(self, index: int, /) -> ElementType:
        """Return self[key]"""
        # Chcek the legitimate of the index
        if index < 0 or self.size - 1 < index:
            raise IndexError('index out of range.')
        return self.data[index]

    def __len__(self, /) -> int:
        """Implement built-in function ``len()``."""
        # Return the attribute size
        return self.size

    def __str__(self, /) -> str:
        """Implement built-in function ``print()``.
        
        Treaverse the linked list. The time complexity is :math:`O(n)`. 
        """
        # Format the output
        return '[' + ', '.join(map(str, self.data[:self.size])) + ']'
    
    def append(self, object: ElementType, /) -> None:
        """Append object to the end of the list.
        
        Time complexity is :math:`O(1)`.
        """
        # Appending
        self.data[self.size] = object
        self.size += 1

        # Atuo extend
        if self.size > self.maxsize - 1:
            self.data += [None] * self.maxsize
            self.maxsize *= 2

    def index(self, 
              value: ElementType, 
              start: int = 0, 
              stop: int = MAXSIZE, /) -> int:
        """Return first index of the value.
        
        At or after index start and before index stop. Time complexity 
        is :math:`O(n)`.
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
        """Insert object before index.
        
        Time complexity is :math:`O(n)`.
        """
        # Adjust range of inde, delegatea to the append method
        if index > self.size -1:
            self.append(object)
            return

        # Insertion
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = object
        self.size += 1

        # Auto extend
        if self.size > self.maxsize - 1:
            self.data += [None] * self.maxsize
            self.maxsize *= 2
    
    def pop(self, index: int = -1, /) -> ElementType:
        """Remove and return item at index (deafult last).
        
        Time complexity is :math:`O(n)`.
        """
        # Raise empty list error
        if self.size < 1:
            raise IndexError('empty list.')

        # Check the index range, and set default value of index
        if index < -1 or self.size-1 < index:
            raise IndexError('index out of range.')
        elif index == -1:
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
        # Or not found
        else:
            raise IndexError('not found.')
    

# - Test module --------------------------------------------------------
def check_equal(arr: list[int], other: SeqList) -> None:
    # Check the size of the sequential list
    assert len(arr) == other.size, 'len(sample) != seqlist.size'

    # Check the element of the sequential list
    for i in range(len(arr)):
        assert arr[i] == other[i], f'arr[{i}] != other[{i}]'

def test_append(arr: list[int], other: SeqList) -> None:
    # Fill the sequential list by using append method
    print('Begin Append ...')
    for item in arr:
        other.append(item)

    assert other.maxsize <= other.size * 2, \
           f'\nseqlist: {other}\nsize: {other.size}\nmaxsize: {other.maxsize}'

    # Check wether the two lists are equal
    check_equal(arr, other)
    print('Append OK!')

def test_index(arr: list[int], other: SeqList) -> None:
    # Select a random element in arr
    print('Begin Index ...')
    for _ in range(100):
        random_item= random.choice(arr)
        assert arr.index(random_item) == other.index(random_item), \
               'Index failed'

    # Test OK!
    print('Index OK!')

def test_pop(arr: list[int], other: SeqList) -> None:
    # Pop some item from two list
    print('Begin Pop ...')
    random_loop = random.randint(1, len(arr)//2)
    for _ in range(random_loop):
        assert arr.pop() == other.pop(), 'Pop failed'

    # Check wether the two lists are equal
    check_equal(arr, other)
    print('Pop OK!')

def test_insert_remove(arr: list[int], other: SeqList) -> None:
    print('Begin Insert and Remove ...')
    # Test Insert
    for i in range(100):
        random_index = random.randint(1, len(arr)-1)
        arr.insert(random_index, random_index)
        other.insert(random_index, random_index)
        check_equal(arr, other)

        # Test Remove
        random_item = random.choice(arr)
        arr.remove(random_item)
        other.remove(random_item)
        check_equal(arr, other)

    # Check wether the two lists are equal
    print('Insert and Remove OK!')

# - Main emtry point of module -----------------------------------------
def main() -> None:
    # Initialize the test data 
    sample = [
        1, 5, 8, 4, 0, 33, 2, 5, 3, 7, 9, 6, 11, 13, 17, 22, 17
    ]
    seqlist = SeqList()

    # Test append method
    test_append(sample, seqlist)

    # Test index method 
    test_index(sample, seqlist)

    # Test pop method
    test_pop(sample, seqlist)

    # Test insert and remove method 
    test_insert_remove(sample,seqlist)

    # All test finish
    print('All test OK!')
    output = f'sample: {sample}\nseqlist: {seqlist}'
    print(output)

if __name__ == '__main__':
    main()