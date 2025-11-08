#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional

ElementType = Union[int, None]
MAXSIZE = 2**63 - 1

class Node:
    """The atomic element of the linked list."""

    def __init__(self, 
                 object: ElementType = None,
                 next: Optional[Node] = None,
                 /, *args, **kwargs) -> None:
        """Initialize self."""
        # Stores the data of the node
        self.object = object 

        # Stores the pointer to the next node
        self.next = next

class LinkdList:
    """Linear list implemented with linked list."""

    def __getitem__(self, key: int, /) -> ElementType:
        ...

    def __init__(self, /, *args, **kwargs) -> None:
        """Initailize self."""
        # Initial a linked list with an sentinel node
        self.head = Node()

    def __str__(self, /) -> str:
        """Implement print method."""
        ...

    def append(self, object: ElementType, /) -> None:
        """Append object to the end of the list.
        
        Time comlexity is :math:`O().` 
        """
        ...

    def index(self, 
              value: ElementType, 
              start: int = 0, 
              stop: int = MAXSIZE, /) -> int:
        """Return first index of the value.
        
        Time complexity is :math:`O()`.
        """
        ...

    def insert(self, index: int, objcet: ElementType, /) -> None:
        """Insert objcet before index."""
        ...

    def pop(self, index: int = -1, /) -> ElementType:
        """Remove and return item at index (default last)."""
        ...

    def popleft(self):
        ...

    def remove(self):
        ...
    

