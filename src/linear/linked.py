#!/usr/bin/env python
"""Linked list."""

__all__ = ['Node', 'LinkedList']
__version__ = '0.1'
__author__ = 'Aina'

import sys
import random
from typing import Union, Optional, cast

# Define the constant
ElementType = Union[int, None]
MAXSIZE = sys.maxsize


class Node:
    """The atomic element of the linked list."""

    def __init__(self, obj: ElementType = None, /,
                 *args, **kwargs) -> None:
        """Initialize self."""
        # Store the data of the node.
        self.obj = obj

        # Store the pointer to the next node.
        self.next: Optional[Node] = None


class LinkedList:
    """Linear list implemented with linked list."""

    def __init__(self, /, *args, **kwargs) -> None:
        """Initailize self."""
        # Initial a linked list with an sentinel node.
        self.head = Node()

        # The number of element
        self.size = 0

    def __getitem__(self, index: int, /) -> ElementType:
        """Return self[index]."""
        # Define the variables: ptr[i]
        i: int = -1
        ptr: Optional[Node] = self.head

        # The variable ptr point to the node index i, nameliy list[i].
        while ptr is not None and i < index:
            i += 1
            ptr = ptr.next

        # Find the element or not found.
        if i == index and isinstance(ptr, Node):
            return ptr.obj
        else:
            raise IndexError('index out of range.')

    def __len__(self, /) -> int:
        """Implement built-in function ``len()``."""
        return self.size

    def __str__(self, /) -> str:
        """Implement built-in function ``print()``.

        Treaverse the linked list.  The time complexity is :math:`O(n)`.
        """
        # Define the variables stores the data and pointer to the node.
        arr = []
        ptr = self.head.next

        # Treaverse the linked list.
        while ptr is not None:
            arr.append(ptr.obj)
            ptr = ptr.next

        # Format the output.
        return '[' + ', '.join(map(str, arr)) + ']'

    def append(self, obj: ElementType, /) -> None:
        """Append object to the end of the list.

        Time complexity is :math:`O(n).`
        """
        # Define the variables.
        temp = Node(obj)
        ptr = self.head

        # Treaverse to the end of the linked list.
        while ptr.next is not None:
            ptr = ptr.next

        # Append the temp to the end of the linked list.
        ptr.next = temp
        self.size += 1

    def index(self,
              value: ElementType,
              start: int = 0,
              stop: int = MAXSIZE, /) -> int:
        """Return first index of the value.

        At or after index start and before index stop.  Time complexity
        is :math:`O(n)`.
        """
        # Define the variables.
        i: int = -1
        ptr: Optional[Node] = self.head

        # The variables represent the node ptr[i].
        while ptr is not None and i < stop:
            if i >= start and ptr.obj == value:
                return i
            i += 1
            ptr = ptr.next

        # Not found.
        return -1

    def insert(self, index: int, obj: ElementType, /) -> None:
        """Insert object before index.

        Time complexity is :math:`O(n)`.
        """
        # Define the variables.
        i: int = -1
        ptr: Optional[Node] = self.head
        temp = Node(obj)

        # Treaverse to the node before the given index.
        while ptr.next is not None and i < index - 1:
            i += 1
            ptr = ptr.next

        # Insertion.
        temp.next = ptr.next
        ptr.next = temp
        self.size += 1

    def pop(self, index: int = -1, /) -> Node:
        """Remove and return node at index (default last).

        Time complexity is :math:`O(n)`.
        """
        # Check the index range, and set default value of index.
        if index < -1 or self.size - 1 < index:
            raise IndexError('index out of range.')
        elif index == -1:
            index += self.size

        # Define variables.
        i: int = -1
        ptr: Optional[Node] = self.head

        # Treaverse to the node before the given index.
        while ptr.next is not None and i < index - 1:
            i += 1
            ptr = ptr.next

        # Get the target node and remove it from the linked list.
        temp = cast(Node, ptr.next)
        ptr.next = temp.next
        temp.next = None
        self.size -= 1

        # Return the node.
        return temp

    def remove(self, value: ElementType, /) -> None:
        """Remove first occurrence of value.

        Time complexity is :math:`O(n)`.
        """
        # Define the variables.
        ptr = self.head

        # Finde the node have the value.
        while ptr.next is not None:
            if ptr.next.obj == value:
                ptr.next = ptr.next.next
                self.size -= 1
                return
            ptr = ptr.next

        # Nof found.
        raise IndexError('not found.')


# -- Test module -------------------------------------------------------
#
def check_equal(arr: list[int], other: LinkedList) -> None:
    # Check the size of the sequential list.
    assert len(arr) == other.size, 'The method len() failed'

    # Check the element of the sequential list.
    for i in range(len(arr)):
        assert arr[i] == other[i], f'arr[{i}] != other[{i}]'


def test_append(arr: list[int], other: LinkedList) -> None:
    # Fill the sequential list by using append method.
    print('Begin Append ...')
    for item in arr:
        other.append(item)

    # Check wether the two lists are equal.
    check_equal(arr, other)
    print('Append OK!')


def test_index(arr: list[int], other: LinkedList) -> None:
    # Select a random element in arr.
    print('Begin Index ...')
    for _ in range(100):
        random_item = random.choice(arr)
        assert arr.index(random_item) == other.index(random_item), \
               'Index failed'

    # Test OK!
    print('Index OK!')


def test_pop(arr: list[int], other: LinkedList) -> None:
    # Pop some item from two list.
    print('Begin Pop ...')
    random_loop = random.randint(1, len(arr)//2)
    for _ in range(random_loop):
        assert arr.pop() == other.pop().obj, \
               f'Pop failed: {arr.pop()} == {other.pop().obj}'

    # Check wether the two lists are equal.
    check_equal(arr, other)
    print('Pop OK!')


def test_insert_remove(arr: list[int], other: LinkedList) -> None:
    print('Begin Insert and Remove ...')
    # Test Insert.
    for i in range(100):
        random_index = random.randint(1, len(arr)-1)
        arr.insert(random_index, random_index)
        other.insert(random_index, random_index)
        check_equal(arr, other)

        # Test Remove.
        random_item = random.choice(arr)
        arr.remove(random_item)
        other.remove(random_item)
        check_equal(arr, other)

    # Check wether the two lists are equal.
    print('Insert and Remove OK!')


# -- Main entry point of module ----------------------------------------
#
def main() -> None:
    # Initialize the test data.
    sample = [
        1, 5, 8, 4, 0, 33, 2, 5, 3, 7, 9, 6, 11, 13, 17, 22, 17
    ]
    seqlist = LinkedList()

    # Test append method.
    test_append(sample, seqlist)

    # Test index method.
    test_index(sample, seqlist)

    # Test pop method.
    test_pop(sample, seqlist)

    # Test insert and remove method.
    test_insert_remove(sample, seqlist)

    # All test finish.
    print('All test OK!')
    output = f'sample: {sample}\nseqlist: {seqlist}'
    print(output)


if __name__ == '__main__':
    main()
