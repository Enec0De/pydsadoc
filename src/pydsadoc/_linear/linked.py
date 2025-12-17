#!/usr/bin/env python
"""Linked List."""

import sys
from enum import Enum, auto
from functools import total_ordering
from typing import Any, Generic, Optional, TypeVar, Union, cast

from pydsadoc._abc_and_protocol import Comparable, Node_ABC

# Define the constant
T = TypeVar("T", bound=Comparable)
MAXSIZE = sys.maxsize


# Define the Sentinel type.
class Sentinel(Enum):
    """The sentinel node object."""

    node = auto()


@total_ordering
class Node(Node_ABC, Generic[T]):
    """The atomic element of the linked list."""

    def __init__(self, obj: Union[T, Sentinel], /, *args: Any, **kwargs: Any) -> None:
        """Initialize self."""
        # Store the data of the node.
        self._obj = obj

        # Store the pointer to the next node.
        self.next: Optional[Node[T]] = None

    def __eq__(self, other: object, /) -> bool:
        """Return the result of self.obj == other.obj."""
        if isinstance(other, type(self)):
            return self.obj == other.obj
        else:
            return NotImplemented

    def __lt__(self, other: "Node[T]", /) -> bool:
        """Return the result of self.obj < other.obj."""
        return self.obj < other.obj

    @property
    def obj(self, /) -> T:
        """Return value if the node is not sentinel."""
        if self._obj is not Sentinel.node:
            return self._obj
        else:
            raise AttributeError


class LinkedList(Generic[T]):
    """Linear list implemented with linked list."""

    def __init__(self, /, *args: Any, **kwargs: Any) -> None:
        """Initailize self."""
        # Initial a linked list with an sentinel node.
        self.head: Node[T] = Node(Sentinel.node)

        # The number of element
        self.size = 0

    def __getitem__(self, index: int, /) -> T:
        """Return self[index]."""
        # Check the index range, and set default value of index.
        if index < -self.size or self.size - 1 < index:
            raise IndexError("index out of range.")
        else:
            index += self.size if index < 0 else 0

        # Define the variables for representing ptr[i]
        # Initialize the default value to the ptr[-1]
        ptr: Optional[Node[T]] = self.head
        i = -1

        # Move the variables ptr[i] point to the last node of the list.
        # Or end at the value ptr[index].
        while ptr.next is not None and i < index:
            ptr = ptr.next
            i += 1

        # Return the value if found.
        if i == index and ptr.obj is not Sentinel.node:
            return ptr.obj
        else:
            raise IndexError("index out of range.")

    def __len__(self, /) -> int:
        """Implement built-in function ``len()``."""
        return self.size

    def __str__(self, /) -> str:
        """Implement built-in function ``print()``.

        Treaverse the linked list.  The time complexity is :math:`O(n)`.
        """
        # Define the variables stores the data and pointer to the node.
        ptr = self.head.next

        # Treaverse the linked list.
        arr: list[str] = []
        while ptr is not None:
            arr.append(str(ptr.obj))
            ptr = ptr.next

        # Format the output.
        return "[" + ", ".join(arr) + "]"

    def append(self, obj: T, /) -> None:
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

    def index(self, value: T, start: int = 0, stop: int = MAXSIZE, /) -> int:
        """Return first index of the value.

        At or after index start and before index stop.  Time complexity
        is :math:`O(n)`.
        """
        # Define the variables.
        i: int = -1
        ptr: Optional[Node[T]] = self.head

        # The variables represent the node ptr[i].
        while ptr is not None and i < stop:
            if i >= start and ptr.obj == value:
                return i
            i += 1
            ptr = ptr.next

        # Not found.
        return -1

    def insert(self, index: int, obj: T, /) -> None:
        """Insert object before index.

        Time complexity is :math:`O(n)`.
        """
        # Define the variables.
        i: int = -1
        ptr: Optional[Node[T]] = self.head
        temp = Node(obj)

        # Treaverse to the node before the given index.
        while ptr.next is not None and i < index - 1:
            i += 1
            ptr = ptr.next

        # Insertion.
        temp.next = ptr.next
        ptr.next = temp
        self.size += 1

    def pop(self, index: int = -1, /) -> Node[T]:
        """Remove and return node at index (default last).

        Time complexity is :math:`O(n)`.
        """
        # Check the index range, and set default value of index.
        if index < -self.size or self.size - 1 < index:
            raise IndexError("index out of range.")
        else:
            index += self.size if index < 0 else 0

        # Define variables.
        ptr: Optional[Node[T]] = self.head
        i: int = -1

        # Treaverse to the node before the given index.
        # The ptr.next must be an available Node, not None.
        while ptr.next is not None and i < index - 1:
            ptr = ptr.next
            i += 1

        # Get the target node and remove it from the linked list.
        temp = cast(Node[T], ptr.next)
        ptr.next = temp.next
        temp.next = None
        self.size -= 1

        # Return the node.
        return temp

    def remove(self, value: T, /) -> None:
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
        raise IndexError("not found.")
