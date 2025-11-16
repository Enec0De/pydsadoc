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
        string, space = '', ' '
        fill = space * (2**h-2)

        # Generate the string.
        for i in range(h):
            # The item in this depth.
            string += space * (2**(h-i)-1) + next(level).zfill(2)
            for _ in range(2**i-1):
                string += fill + next(level).zfill(2)
            
            # Prepare for next loop.
            if i == h - 1: break
            string += '\n'
            fill = space * (2**(h-i)-2)
        
        # Return the string.
        return string

    def _get_height(self, node: AVLNode, /) -> int:
        """Return the height of the node."""
        left_height = self._get_height(node.left) if node.left else 0
        right_height = self._get_height(node.right) if node.right else 0
        node.height = 1 + max(left_height, right_height)
        return node.height

    def _get_min(self, node: AVLNode, /) -> AVLNode:
        r"""Return the minimum element in the tree.

        Time complexity is :math:`O(\log n)`.
        """
        # Traverse the left node.
        current = node
        while current.left:
            current = current.left
        return current

    @property
    def height(self, /) -> int:
        """Return the height of the tree."""
        return self._get_height(self.root) if self.root else 0

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
                    break
            # Store large value to the right.
            elif value > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = AVLNode(value)
                    current.right.height = current.height + 1
                    break

            # Value exist.
            else: 
                raise ValueError('value exist.')

    def remove(self, value: int, /) -> None:
        """Remove value in the AVL Tree."""
        # Define the function of removing. Return the node of the
        # sub tree after removing the value.
        def rm_recursion(node: Optional[AVLNode],
                         value: int, /) -> Optional[AVLNode]:
            # Empty sub tree.
            if node is None: return None

            # Remove in the left sub tree recursively.
            if value < node.data:
                node.left = rm_recursion(node.left, value)
            # Remove in the right sub tree recursively.
            elif value > node.data:
                node.right = rm_recursion(node.right, value)
            # Process the current node in two cases.
            else: 
                # The node has two children.
                if node.left and node.right:
                    temp = self._get_min(node.right)
                    node.data = temp.data
                    node.right = rm_recursion(node.right, temp.data)
                # The node has at most one child.
                else:
                    return node.left if node.left else node.right

            # After the recursion, return the current node.
            return node

        # Process the removing from root node.
        self.root = rm_recursion(self.root, value)

    def pre_order(self) -> None:
        ...

    def in_order(self) -> None:
        ...

    def post_order(self) -> None:
        ...


def main() -> None:
    # Test array with no reapet elemtn.
    arr = [random.randint(-9, 20) for _ in range(random.randint(4, 7))]
    arr_shuffle = list(set(arr))
    random.shuffle(arr_shuffle)

    # Temp 
    ...

    # Prepare for insert.
    print(f'# -- Array: {arr_shuffle} '.ljust(40, '-'))
    test = AVL()


    # Insert element one by one.
    for item in arr_shuffle:
        test.insert(item)
    print(test)

    # Remove a random item in the arr.
    random_item = random.choice(arr)

    # Temp
    ...

    print(f'# -- Remove: [{random_item}] '.ljust(40, '-'))
    test.remove(random_item)
    print(test)


if __name__ == '__main__':
    main()