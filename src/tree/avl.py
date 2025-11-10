#!/usr/bin/env python

from __future__ import annotations

from typing import Union, Optional


# Define the constant
ElementType = Union[None, int]


class AVLNode:
    """The atomic element of the AVL tree."""

    def __init__(self, data: ElementType, /, *args, **kwargs) -> None:
        # The data of the node.
        self.data = data

        # The child of the node.
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None

        # Attribute stores the height.
        self.balance_factors: int = 0


class AVL:
    """The AVL tree impelemented with linked list."""

    def __init__(self, /, *args, **kwargs) -> None:
        """Initialize self."""
        self.head: Optional[AVLNode] = None

    def __getitem__(self, key: ElementType) -> AVLNode:
        """Return self[key].  Implementation of the search operation."""
        ...

    def insert(self):
        ...

    def remove(self):
        ...

    def get_max(self):
        ...

    def get_min(self):
        ...

    def get_height(self):
        ...

    def pre_order(self) -> None:
        ...

    def in_order(self) -> None:
        ...

    def post_order(self) -> None:
        ...
