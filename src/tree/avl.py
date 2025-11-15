#!/usr/bin/env python

from __future__ import annotations

__all__ = ['AVL']
__version__ = '0.1'
__author__ = 'Aina'

from typing import Union, Optional
from collections import deque
import random

# Define the constant
ElementType = Union[int, float]


class AVLNode:
    """The atomic element of the AVL tree."""

    def __init__(self, data: ElementType, /, *args, **kwargs) -> None:
        # The data of the node.
        self.data = data

        # The child of the node.
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None

        # Attribute stores the height.
        self.height: int = 0


class AVL:
    """The AVL tree impelemented with linked list."""

    def __init__(self, /, *args, **kwargs) -> None:
        """Initialize self."""
        self.head: AVLNode = AVLNode(float('inf'))
        self.height: int = 0

    def __getitem__(self, key: ElementType) -> AVLNode:
        """Return self[key].  Implementation of the search operation."""
        ...

    def __str__(self, /) -> str:
        # Level order traversal
        if self.head.left:
            queue: deque[Union[AVLNode, None]] = deque([self.head.left])
        else:
            raise IndexError('empty tree.')
        
        # Define the generator function for traveling and create it.
        def traversal():
            nonlocal queue
            while True:
                node = queue.popleft()
                queue.extend(
                    [node.left, node.right] if node else [None, None]
                    )
                yield str(node.data) if node else '  '
        level = traversal()
            
        # Prepare for the basic variables
        h = self.height
        string = ''
        fill = ' ' * (2**h-2)

        # Generate the string.
        for i in range(h):
            # The first item in this depth.
            string += ' ' * (2**(h-i)-1) + next(level).zfill(2)
            
            # The rest item in this depth.
            for _ in range(2**i-1):
                # Continue append item.
                string += fill + next(level).zfill(2)
            
            # Do not prcess the rest code.
            if i == h - 1: break

            # The fill space for the next depth and end this line.
            string += '\n'
            fill = ' ' * (2**(h-i)-2)
        
        # Return the string.
        return string


    def insert(self, value: int, /) -> None:
        """Insert value to the AVL Tree."""
        # The pointer to the head node.
        current = self.head

        while True:
            # Value exist.
            if value == current.data:
                raise ValueError('value exist.')

            # Store small value to the left.
            elif value < current.data:
                if current.left is not None:
                    current = current.left
                else:
                    current.left = AVLNode(value)
                    current.left.height = current.height + 1
                    self.height = max(self.height, current.left.height) 
                    break
            
            # Store large value to the right.
            elif value > current.data:
                if current.right is not None:
                    current = current.right
                else:
                    current.right = AVLNode(value)
                    current.right.height = current.height + 1
                    self.height = max(self.height, current.right.height) 
                    break
        
        # Insert successfully.

    def remove(self, value: int, /) -> None:
        """Remove value in the AVL Tree."""
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


def main() -> None:
    arr = [random.randint(-9, 20) for _ in range(random.randint(4, 7))]
    print(set(arr))
    test = AVL()
    for item in set(arr):
        test.insert(item)
    print(test)
    print(test.height)


if __name__ == '__main__':
    main()