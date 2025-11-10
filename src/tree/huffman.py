#!/usr/bin/env python

from __future__ import annotations

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

    def heapify(self, arr: list, /) -> None:
        """Make heap from list in a more efficient way. 
        
        It's quicker than pushing items one by one.  Time complexity is
        :math:`O()`.
        """
        ...

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

        # Palce ojbect in the crrent
        if current != self.size:
            self.obj[current] = obj
        
        # Increase self size
        self.size += 1



@total_ordering
class HNode:
    """The atomic element of the Huffman Tree."""

    def __init__(self, weight: int):
        """Initialize self."""
        self.weight = weight
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

    def __init__(self):
        """Initialize self."""
        self.head: Optional[HNode] = None

    def huffmanify(self):
        """Build Huffman Tree from an minmum heap."""
        ...


def main() -> None:

    arr = []
    heap = MinHeap()

    for i in range(random.randint(1,20)):
        arr.append(random.randint(1,20))

    for item in arr:
        node = HNode(item)
        heap.heappush(node)

    result = []
    for _ in arr:
        a = heap.heappop()
        result.append(str(a.weight))
        
    print(arr) 
    print(', '.join(result))


if __name__ == '__main__':
    main()
