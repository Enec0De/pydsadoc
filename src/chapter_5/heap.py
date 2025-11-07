#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Implementation of the heap with list."""

from __future__ import annotations
from typing import Optional, cast


ElementType = int

class MaxHeap:

    def __init__(self, MAXSIZE: ElementType = 10) -> None:
        """Initialize an MaxHeap."""
        # The elements index 0 is the sentinel node of the heap
        self.elements: list[Optional[int]] = [None] * (MAXSIZE+1)
        self.size: int = 0
        self.capacity: int = MAXSIZE
    
    def insert(self, item: ElementType) -> None:
        r"""The Time complexity of the insertion is :math:`O(\log N)`
        
        :param item: The item to be inserted into the heap.
        """
        # Is full

        # Insertion
        i = self.size + 1
        
        # Compare its parent
        while self.elements[i//2] < item and i > 0:               # type: ignore
            self.elements[i] = self.elements[i//2]
            i //= 2
        
        # Noew, i is the index of the 
        self.elements[i] = item

    def delete(self) -> ElementType:
        """Delete the root element from the heap.
        
        :return: The deleteted element.
        """
        # Is empty

        # substitute the root using the last element
        maxitem = cast(int, self.elements[1])
        temp = self.elements[self.size]
        self.size -= 1

        # compared with his child
        child = 2
        while child <= self.size:
            # Find the larger element
            if child != self.size:
                if self.elements[child] < self.elements[child+1]: # type: ignore
                    child += 1

            # Point to the larger element and compare its parent
            if temp < self.elements[child]:                       # type: ignore
                self.elements[child//2] = self.elements[child]

                # Go to the left child
                child *= 2
            
            # Break the loop
            else:
                break
        
        # place the temp to the last child
        self.elements[child//2] = temp
        return maxitem


    
    def makeheap_from_list(self, l: list) -> None:
        """Make heap from list. It's more quickly than insert."""
        length = len(l) 
        l = [None] + l
        start = length // 2

        while start > 0:
            # Left child
            child = start * 2
            # Make the subheap
            while child <= length:
                # Only left or right is large
                if child != length:

                    if l[child] < l[child+1]:
                        child += 1

                # Compare with large child
                if l[child // 2] < l[child]:
                    # Swap the data
                    temp = l[child]
                    l[child] = l[child // 2]
                    l[child // 2] = temp

                    # Go to the next node
                    child *= 2
                # The loop complete
                else:
                    break

            start -= 1
        
        self.elements= l + [None]*(self.size-length)
        self.size = len(self.elements) - 1

         
def main():
    a = MaxHeap(12)
    a.makeheap_from_list([79, 66, 43, 91, 72, 87, 38, 55, 83, 30, 49, 9])
    print(a.elements)
            
if __name__ == '__main__':
    main()

            


