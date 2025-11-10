#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations

from typing import Union, Optional


# Define the constant
ElementType = Union[int]


class MinHeap:
    """Implementation of the minimum heap with sequential list."""

    def __init__(self) -> None:
        """Initialize self."""
        self.obj: list[ElementType] = []
        ...

    def heapify(self, arr: list) -> None:
        """Make heap from list in a more efficient way. 
        
        It's quicker than pushing items one by one.  Time complexity is
        :math:`O()`.
        """
        ...

    def heappop(self) -> None:
        """Remove and return smallest item from the heap.

        Time complexity is :math:`O()`.
        """
        ...

    def heappush(self) -> None:
        """Push object into the heap, maintaining the heap invariant.
        
        Time complexity is :math:`O()`.
        """
        ...


class HNode:
    """The atomic element of the Huffman Tree."""

    def __init__(self):
        """Initialize self."""
        self.weight = 0
        self.left = None
        self.right = None