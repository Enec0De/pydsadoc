#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional

ElementType = Union[int]


class MinHeap:

    def __init__(self) -> None:
        self.obj: list[ElementType] = []
        ...

    def heapify(self) -> None:
        ...

    def heappop(self) -> None:
        ...

    def heappush(self) -> None:
        ...


class HNode:
    """The atomic element of the Huffman Tree."""

    def __init__(self):
        """Initialize self."""
        self.weight = 0
        self.left = None
        self.right = None