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
        if self.head.left is not None:
            queue: deque[Union[AVLNode, None]] = deque([self.head.left])
        else:
            raise IndexError('empty tree.')

        # Prepare for the basic variables
        string = ''
        height = self.height
        fill = ' ' * (2**height-2)
        
        # The generator function of the level traversal.
        def traversal():
            nonlocal queue
            while True:
                avl_node = queue.popleft()
                if avl_node is not None:
                    if avl_node.left is not None:
                        queue.append(avl_node.left)
                    else:
                        queue.append(None)
                    if avl_node.right is not None:
                        queue.append(avl_node.right)
                    else:
                        queue.append(None)
                    yield str(avl_node.data)
                else: 
                    queue.append(None)
                    queue.append(None)
                    yield '  '
            
        # Create the generator
        level = traversal()

        # Generate the string.
        for i in range(height):
            # The first item in this depth.
            avl_data = next(level)
            string += ' ' * (2**(height-i)-1) + avl_data.zfill(2)
            
            # The rest item in this depth.
            for _ in range(2**i-1):
                # Get he next item.
                avl_data = next(level)

                # Continue append item.
                string += fill
                string += avl_data.zfill(2)
            
            # Break this for loop.
            if i == height - 1:
                break

            # The fill space for the next depth.
            fill = ' ' * (2**(height-i)-2)

            # End this line.
            string += '\n'
        
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