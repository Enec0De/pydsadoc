#!/usr/bin/env python

from __future__ import annotations

__all__ = ['AVL']
__version__ = '0.1'
__author__ = 'Aina'

from typing import Union, Optional
from collections import deque
import random

# Define the constant
ElementType = Union[int]


class AVLNode:
    """The atomic element of the AVL tree."""

    def __init__(self, data: ElementType, /, *args, **kwargs) -> None:
        # The data of the node.
        self.data = data

        # The child of the node.
        self.left: Optional[AVLNode] = None
        self.right: Optional[AVLNode] = None

        # Attribute stores the height.
        self.height: int = 1


class AVL:
    """The AVL tree impelemented with linked list."""

    def __init__(self, /, *args, **kwargs) -> None:
        """Initialize self."""
        self.root: Optional[AVLNode] = None
        self.height: int = 0

    def __getitem__(self, key: ElementType) -> AVLNode:
        """Return self[key].  Implementation of the search operation."""
        ...

    def __str__(self, /) -> str:
        """Print the AVL in a visual way."""
        # Level order traversal
        if self.root:
            queue: deque[Union[AVLNode, None]] = deque([self.root])
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
        if self.root:
            current: AVLNode = self.root
        else:
            self.root = AVLNode(value)
            return

        while True:
            # Store small value to the left.
            if value < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = AVLNode(value)
                    current.left.height = current.height + 1
                    self.height = max(self.height, current.left.height)
                    break
            
            # Store large value to the right.
            elif value > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = AVLNode(value)
                    current.right.height = current.height + 1
                    self.height = max(self.height, current.right.height)
                    break

            # Value exist.
            else: 
                raise ValueError('value exist.')

    def remove(self, value: int, /) -> None:
        """Remove value in the AVL Tree."""
        def rm_recursion(node: AVLNode, /) -> Optional[AVLNode]:
            if node.left and node.right:
                # Find the left leaf of the right sub tree and remove it
                # recursively.
                if node.right.left is None:
                    node.data = node.right.data
                    node.right = rm_recursion(node.right)
                else:
                    # current point to the left node of the right tree.
                    current = node.right
                    while current.left:
                        cur_pre = current
                        current = current.left

                    # Change the node data and delete the current node.
                    node.data = current.data
                    cur_pre.left = rm_recursion(current)

                # Current node has two childs.  Do not remove it. 
                return node
            else:
                # Remove the current node.
                return node.left if node.left else node.right

        # Check the bondary.
        if self.root:
            current = self.root
        else:
            raise IndexError('empty tree.')
        
        # Delete the root without childs.
        if value == self.root.data:
            self.root = rm_recursion(self.root)
            return

        while current:
            if value < current.data:
                if current.left and value == current.left.data:
                    current.left = rm_recursion(current.left)
                    return
                else:
                    current = current.left

            elif value > current.data:
                if current.right and value == current.right.data:
                    current.right = rm_recursion(current.right)
                    return
                else:
                    current = current.right
        else:
            raise IndexError('value nof found.')

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
    arr_shuffle = list(set(arr))
    random.shuffle(arr_shuffle)
    print(f'# -- set: {set(arr)} '.ljust(40, '-'))
    test = AVL()

    for item in arr_shuffle:
        test.insert(item)
    print(test)

    a = random.choice(arr)
    print(f'# -- remove {a}: '.ljust(40, '-'))
    test.remove(a)
    print(test)


if __name__ == '__main__':
    main()