#!/usr/bin/env python

from __future__ import annotations

__all__ = ['MinHeap', 'Huffman']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional
from functools import total_ordering

# Define the constant
ElementType = Union['HNode']


class MinHeap:
    """Implementation of the minimum heap with sequential list."""

    def __init__(self, /, *args, **kwargs) -> None:
        """Initialize self."""
        self.obj: list[ElementType] = []
        self.size: int = 0

    def heapify(self, arr: list[ElementType], /) -> None:
        """Make heap from list in a more efficient way. 
        
        It's also called Floyd Algorithm, which is quicker than pushing
        items one by one.  Time complexity is :math:`O(n)`.
        """
        # Uptate self size.
        self.obj = arr
        self.size = len(arr)

        # Compare within the subheap
        current = (self.size-2) // 2       
        while current >= 0:
            parent = current
            temp = self.obj[current]
            while (child := parent*2 + 1) <= self.size - 1:
                # Choose the smaller element.
                if (child != self.size -1 
                    and self.obj[child] > self.obj[child+1]):
                    # child now point to the smaller one.
                    child += 1
                
                # child node is smaller than the parent node.
                if self.obj[child] < temp:
                    self.obj[parent] = self.obj[child]
                    parent = child
                
                # parent is the palce where node should be.
                else:
                    break

            # Place the node
            if parent != current:
                self.obj[parent] = temp

            # Go to next loop
            current -= 1

    def heappop(self, /) -> ElementType:
        r"""Remove and return smallest item from the heap.

        Time complexity is :math:`O(\log n)`.
        """
        # Check boundary
        if self.size < 1:
            raise IndexError('empty heap.')
        self.size -= 1

        # Store the node to be returned.
        retnode = self.obj[0]

        # Compare cuurent and its child
        current: int = 0
        while (child := current*2 + 1) <= self.size - 1:
            if child != self.size - 1 and self.obj[child] > self.obj[child+1]:
                child += 1

            # child node is smaller than the last node.
            if self.obj[child] < self.obj[self.size]:
                self.obj[current] = self.obj[child]
                current = child

            # current is the palce where node should be.
            else:
                break

        # Place the node.
        self.obj[current] = self.obj[self.size]
        del self.obj[self.size]

        # Return the first node.
        return retnode
        

    def heappush(self, obj: ElementType, /) -> None:
        r"""Push object into the heap, maintaining the heap invariant.
        
        Time complexity is :math:`O(\log n)`.
        """
        # Place object in the last position of the list.
        self.obj.append(obj)

        # Point to the last node.
        current = self.size
        while current > 0:
            parent: int = (current-1) // 2

            # Parent larger than child.
            if obj < self.obj[parent]:
                self.obj[current] = self.obj[parent]
                current = parent
            
            # current is the place where object should be.
            else:
                break

        # Palce ojbect in the crrent.
        if current != self.size:
            self.obj[current] = obj
        
        # Increase self size.
        self.size += 1


@total_ordering
class HNode:
    """The atomic element of the Huffman Tree."""

    def __init__(self, weight: int, char: str = '', /):
        """Initialize self."""
        self.weight = weight
        self.char = char
        self.left = None
        self.right = None

    def __eq__(self, other: HNode, /) -> bool:
        """Return self == other"""
        return self.weight == other.weight

    def __lt__(self, other: HNode, /) -> bool:
        """Return self < other"""
        return self.weight < other.weight


class Huffman:
    """The implementation of the Huffman Tree."""

    def __init__(self, freq: dict[str, int], /) -> None:
        """Initialize self."""
        self.head: HNode = self._build(freq)

    def _build(self, freq: dict[str, int], /) -> HNode:
        """Build Huffman Tree by using minmum heap."""

        
        ...

    def encode(self) -> dict[str,bytes]:
        ...

    @property
    def wpl(self):
        ...


# -- Test Module ------------------------------------------------------- 
#
def test_heap() -> None:
    # Generate new random list.
    arr = [random.randint(1, 20) for _ in range(random.randint(1, 29))]

    # Build heap_a.
    # Push item into heap_a one by one.
    heap_a = MinHeap()
    for item in arr:
        node = HNode(item)
        heap_a.heappush(node)

    # Build heap_b.
    # Make heap_b from list arr.
    heap_b = MinHeap()
    arr_node = [HNode(x) for x in arr]
    heap_b.heapify(arr_node)
    
    # assert check
    assert heap_a.size == len(arr)
    assert heap_b.size == len(arr)

    # Store result of heap_a
    result_a: list[str] = []
    result_b: list[str] = []
    for _ in arr:
        a, b = heap_a.heappop(), heap_b.heappop()
        result_a.append(str(a.weight))
        result_b.append(str(b.weight))
        assert a.weight == b.weight
        
    assert result_a == result_b
    # Print the result_a and result_b
    # print(', '.join(result_a))
    # print(', '.join(result_b))

def main() -> None:
    # Test MinHeap
    test_heap()


if __name__ == '__main__':
    main()
