#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Implementation of the huffman tree with min heap."""

from __future__ import annotations
from typing import Union, Optional, cast 



ElementType = Union['TreeNode']

class MinHeap:
    """MinHeap implemented with sequential list."""
    def __init__(self):
        """Initialize a empty MinHeap begin with a sentinel node."""
        # Stores the data in the list
        self.data: list[Optional[ElementType]] = [None]

        # Stores the length of the MinHeap
        self.size: int = 0

    def insert(self, item: ElementType) -> None:
        # The index to be insert
        self.size += 1
        i = self.size

        # Scale the list
        self.data += [None]

        # Compare with the parent node
        while i > 1: 
            # The item is smaller than parent
            if self.data[i//2].weight > item.weight: # type: ignore
            # Parent node larger, place it down
                self.data[i] = self.data[i//2]

            # Go to next parent
                i //= 2

            # The parent is smaller
            else:
                break
        
        # Now self.data[i//2] <= item or i point to the root, no parent
        self.data[i] = item

    def delete(self) -> ElementType:
        # The min value to be return
        min_value = cast(ElementType, self.data[1])

        # The last node of the MinHeap
        temp = self.data[self.size]
        self.size -= 1

        # Begin from the top of the heap
        i = 1

        # Variable i point to the left child
        i *= 2
        while i <= self.size:
            # Variable i point to the min element of the two child
            if i != self.size:
                if self.data[i].weight > self.data[i+1].weight: # type: ignore
                    i += 1

            # If temp is larger than child, swap two element
            if temp.weight > self.data[i].weight: # type: ignore
                self.data[i//2] = self.data[i]

                # Variable i go to the left child of current node
                i *= 2
            
            # Temp is smaller than child
            else:
                break
        
        # Now temp is smaller than child
        self.data[i//2] = temp
        del self.data[self.size+1]

        # Return the min element of the heap
        return min_value 

class TreeNode:
    """Implementation of the huffman tree with MinHeap."""

    def __init__(self, data: Optional[int] = None) -> None:
        """Initialize an empty TreeNode."""
        self.weight = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None

    @staticmethod
    def huffman(heap: MinHeap) -> TreeNode:
        """Create an huffman tree from an MinHeap.
        
        :return: Rrturn the root node of huffman tree.
        """
        # Get two min element from MinHeap
        for i in range(0, heap.size-1):
            # Merge once
            temp = TreeNode()
            temp.left = heap.delete()
            temp.right = heap.delete()
            temp.weight = temp.left.weight + temp.right.weight # type: ignore
            heap.insert(temp)

        
        # Return the node of the Huffman Tree
        return heap.delete()

def main():
    heaplist = [1, 2, 3, 4, 5]
    minh = MinHeap()
    for item in heaplist:
        minh.insert(TreeNode(item))

    # Result is the root node of the huffman tree
    result = TreeNode.huffman(minh)
    print(result.weight)




if __name__ == '__main__':
    main()

            



