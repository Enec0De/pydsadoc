#!/usr/bin/env python
"""Sequence List."""

import sys
import random
from typing import TypeVar, Any, Generic, Optional

from pydsadoc._abc_and_protocol import Comparable

# Define the constant
T = TypeVar("T", bound=Comparable)
MAXSIZE = sys.maxsize


class SequenList(Generic[T]):
    """Implement a sequence list."""

    def __init__(self, /, *args: Any, maxsize: int = 16, **kwargs: Any) -> None:
        """Initialize self."""
        # Maxsize of the SeqList.
        self.maxsize = maxsize

        # The number of element.
        self.size = 0

        # The list stores the data.
        self.data: list[Optional[T]] = [None] * self.maxsize

    def __getitem__(self, index: int, /) -> T:
        """Return self[key]."""
        # Chcek the legitimate of the index.
        index = self._check_index(index)
        return self.data[index]  # type: ignore

    def __len__(self, /) -> int:
        """Implement built-in function ``len()``."""
        # Return the size.
        return self.size

    def __str__(self, /) -> str:
        """Implement built-in function ``print()``.

        Treaverse the linked list.  The time complexity is :math:`O(n)`.
        """
        # Format the output.
        return '[' + ', '.join(map(str, self.data[:self.size])) + ']'

    def _auto_extend(self, /) -> None:
        if self.size > self.maxsize - 1:
            self.data += [None] * self.maxsize
            self.maxsize *= 2

    def _check_index(self, index: int) -> int:
        if index < -self.size or self.size - 1 < index:
            raise IndexError("index out of range.")
        else:
            index += self.size if index < 0 else 0
        return index

    def append(self, obj: T, /) -> None:
        """Append object to the end of the list.

        Time complexity is :math:`O(1)`.
        """
        # Append.
        self.data[self.size] = obj
        self.size += 1

        # Atuo extend.
        self._auto_extend()

    def index(self, value: T, start: int = 0, stop: int = MAXSIZE, /) -> int:
        """Return first index of the value.

        At or after index start and before index stop.  Time complexity
        is :math:`O(n)`.
        """
        # Adjust range of index.
        stop = min(self.size, stop)

        # Retrieve for value.
        for i in range(start, stop):
            if self.data[i] == value:
                return i

        # Not found.
        raise IndexError("index out of range.")

    def insert(self, index: int, obj: T, /) -> None:
        """Insert object before index.

        Time complexity is :math:`O(n)`.
        """
        if index < -self.size:
            raise IndexError("index out of range.")
        elif index < 0:
            index += self.size
            self.data[index] = obj
        else:
            index = min(self.size, index)

        # Insertion.
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = obj
        self.size += 1

        # Auto extend.
        self._auto_extend()

    def pop(self, index: int = -1, /) -> T:
        """Remove and return item at index (deafult last).

        Time complexity is :math:`O(n)`.
        """
        # Raise empty list error.
        if self.size < 1:
            raise IndexError('empty list.')

        # Check the index range, and set default value of index.
        if index < -1 or self.size-1 < index:
            raise IndexError('index out of range.')
        elif index == -1:
            index += self.size

        # Firstly, the item to be poped.
        temp = self.data[index]
        self.data[index] = None

        # Secondly, move backward all elements after index.
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i+1]

        # Thirdly, size minus 1 and delete the last element.
        self.size -= 1
        self.data[self.size] = None

        # Finally, Return the item.
        return temp # type: ignore

    def remove(self, value: T, /) -> None:
        """Remove first occurrence of value.

        Time complexity is :math:`O(n)`.
        """
        # Find the value.
        i = 0
        while self.data[i] != value and i <= self.size-1:
            i += 1

        # Delete the value.
        if i <= self.size - 1:
            for j in range(i, self.size-1):
                self.data[j] = self.data[j+1]
            self.size -= 1
            self.data[self.size] = None
        # Or not found.
        else:
            raise IndexError('value not found.')


# -- Test module -------------------------------------------------------
#
def check_equal(arr: list[int], other: SequenList[int]) -> None:
    # Check the size of the sequential list.
    assert len(arr) == other.size, 'len(sample) != seqlist.size'

    # Check the element of the sequential list.
    for i in range(len(arr)):
        assert arr[i] == other[i], f'arr[{i}] != other[{i}]'


def test_append(arr: list[int], other: SequenList[int]) -> None:
    # Fill the sequential list by using append method.
    print('Begin Append ...')
    for item in arr:
        print(other.size, other.maxsize)
        other.append(item)

    assert other.maxsize >= other.size + 10, \
           f'\nseqlist: {other}\nsize: {other.size}\nmaxsize: {other.maxsize}'

    # Check wether the two lists are equal.
    check_equal(arr, other)
    print('Append OK!')


def test_index(arr: list[int], other: SequenList[int]) -> None:
    # Select a random element in arr.
    print('Begin Index ...')
    for _ in range(100):
        random_item = random.choice(arr)
        assert arr.index(random_item) == other.index(random_item), \
               'Index failed'

    # Test OK!
    print('Index OK!')


def test_pop(arr: list[int], other: SequenList[int]) -> None:
    # Pop some item from two list.
    print('Begin Pop ...')
    random_loop = random.randint(1, len(arr)//2)
    for _ in range(random_loop):
        assert arr.pop() == other.pop(), 'Pop failed'

    # Check wether the two lists are equal.
    check_equal(arr, other)
    print('Pop OK!')


def test_insert_remove(arr: list[int], other: SequenList[int]) -> None:
    print('Begin Insert and Remove ...')
    # Test Insert.
    for _ in range(100):
        random_index = random.randint(1, len(arr)-1)
        arr.insert(random_index, random_index)
        other.insert(random_index, random_index)
        check_equal(arr, other)

        # Test Remove
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
        1, 5, 8, 4, 0, 33, 2, 5, 3, 7, 9, 6, 11, 13, 17, 22, 17,
        1, 5, 8, 4, 0, 33, 2, 5, 3, 7, 9, 6, 11, 13, 17, 22, 17
    ]
    seqlist: SequenList[int] = SequenList()

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
