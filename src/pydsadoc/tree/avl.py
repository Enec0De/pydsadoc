#!/usr/bin/env python
"""The AVL tree data structure."""

__all__ = ['AVLNode', 'AVL']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional, cast
from collections import deque
from collections.abc import Iterator

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
        if self.root is None:
            raise IndexError('empty tree.')

        # The Iterator of the tree.
        level = self._level_order_traversal()

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
            if i == h - 1:
                break
            string += '\n'
            fill = space * (2**(h-i)-2)

        # Return the string.
        return string

    def _adjust(self, node: AVLNode, /) -> AVLNode:
        """Adjust the tree after removing or inserting."""
        # Process the rotaiton.
        if self._get_balance(node) > 1:
            if self._get_balance(node.left) >= 0:
                # Case LL.
                return self._rotation_right(node)
            else:
                # Case LR.
                node.left = self._rotation_left(cast(AVLNode, node.left))
                return self._rotation_right(node)
        elif self._get_balance(node) < -1:
            if self._get_balance(node.left) <= 0:
                # Case RR.
                return self._rotation_left(node)
            else:
                # Case RL.
                node.right = self._rotation_right(cast(AVLNode, node.right))
                return self._rotation_left(node)
        else:
            return node

    def _level_order_traversal(self, /) -> Iterator[str]:
        """Define the generator function for level traveling."""
        queue: deque[Union[AVLNode, None]] = deque([self.root])
        # Level traversal of all nodes, including None.
        while True:
            node = queue.popleft()
            queue.extend([node.left, node.right] if node else [None, None])
            yield str(node.data) if node else '  '

    def _get_balance(self, node: Optional[AVLNode], /) -> int:
        """Return the balance factor of the node."""
        if node:
            return self._get_height(node.left) - self._get_height(node.right)
        else:
            return 0

    def _get_height(self, node: Optional[AVLNode], /) -> int:
        """Return the height of the node."""
        if node:
            left_height = node.left.height if node.left else 0
            right_height = node.right.height if node.right else 0
            return 1 + max(left_height, right_height)
        else:
            return 0

    def _get_min(self, node: AVLNode, /) -> AVLNode:
        r"""Return the minimum element in the tree.

        Time complexity is :math:`O(\log n)`.
        """
        # Traverse the left node.
        current = node
        while current.left:
            current = current.left
        return current

    def _insert_recursion(self, node: AVLNode, value: int,
                          /) -> Optional[AVLNode]:
        """Define the function of inserting recursively.

        Return the node of the sub tree after inserting the value.
        """
        # Insert in the left sub tree recursively.
        if value < node.data:
            if node.left:
                node.left = self._insert_recursion(node.left, value)
            else:
                node.left = AVLNode(value)
        # Insert in the right sub tree recursively.
        elif value > node.data:
            if node.right:
                node.right = self._insert_recursion(node.right, value)
            else:
                node.right = AVLNode(value)
        # Value exist.
        else:
            raise IndexError('value exist.')

        # Update the height.
        node.height = self._get_height(node)

        # Return the node after the rotation.
        return self._adjust(node)

    def _remove_recursion(self, node: Optional[AVLNode], value: int,
                          /) -> Optional[AVLNode]:
        """Define the function of removing recursively.

        Return the node of the sub tree after removing the value.
        """
        # Empty sub tree.
        if node is None:
            return None

        # Remove in the left sub tree recursively.
        if value < node.data:
            node.left = self._remove_recursion(node.left, value)
        # Remove in the right sub tree recursively.
        elif value > node.data:
            node.right = self._remove_recursion(node.right, value)
        # Process the current node in two cases.
        else:
            # The node has two children.
            if node.left and node.right:
                temp_node = self._get_min(node.right)
                node.data = temp_node.data
                node.right = self._remove_recursion(node.right, temp_node.data)
            # The node has at most one child.
            else:
                return node.left if node.left else node.right

        # After the recursion, update node height and
        node.height = self._get_height(node)

        # Return the node after the rotaion.
        return self._adjust(node)

    def _rotation_left(self, node: AVLNode, /) -> AVLNode:
        """The left rotaion of the tree."""
        # The new root to be return.  The right node must exist.
        new_root = cast(AVLNode, node.right)

        # Process the left rotation.
        node.right = new_root.left
        new_root.left = node

        # Update the height.
        node.height = self._get_height(node)
        new_root.height = self._get_height(new_root)

        # Return the new root after the rotation.
        return new_root

    def _rotation_right(self, node: AVLNode, /) -> AVLNode:
        """The right rotaiton of the tree."""
        # The new root to be return.  The left node must exist.
        new_root = cast(AVLNode, node.left)

        # Process the right rotation.
        node.left = new_root.right
        new_root.right = node

        # Update the height.
        node.height = self._get_height(node)
        new_root.height = self._get_height(new_root)

        # Return the new root after the rotation.
        return new_root

    @property
    def height(self, /) -> int:
        """Return the height of the tree."""
        return self._get_height(self.root)

    def insert(self, value: int, /) -> None:
        """Insert value to the AVL Tree."""
        # The pointer to the head node.
        if self.root:
            self.root = self._insert_recursion(self.root, value)
        else:
            self.root = AVLNode(value)

    def remove(self, value: int, /) -> None:
        """Remove value in the AVL Tree."""
        # Process the removing from root node.
        self.root = self._remove_recursion(self.root, value)

    def pre_order(self, /) -> None:
        """Implementation of pre-order traversal with stack."""
        # Empty tree.
        if self.root is None:
            return

        # Define the stack and the buffer.
        stack: list[AVLNode] = [self.root]
        buffer: list[ElementType] = []

        # Traverse all of the nodes.
        while stack:
            current = stack.pop()
            buffer.append(current.data)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

        # Print the result.
        print(buffer)

    def in_order(self, /) -> None:
        """Implementation of in-order traversal with stack."""
        # Empty tree.
        if self.root is None:
            return

        # Define the stack and the buffer.
        stack: list[AVLNode] = []
        buffer: list[ElementType] = []

        current = self.root
        while current or stack:
            # Push the node if it has left node.
            while current:
                stack.append(current)
                current = current.left

            # Pop node which has no left node, and push its right node.
            current = stack.pop()
            buffer.append(current.data)
            current = current.right

        # Print the result.
        print(buffer)

    def post_order(self, /):
        """Implementation of post-order traversal with stacks."""
        # Empty tree.
        if self.root is None:
            return

        # stack: list[tuple[int, AVLNode]]
        stack: list[AVLNode] = []
        buffer: list[int] = []

        current = self.root
        while current or stack:
            # Push the node if it has right node.
            while current:
                stack.append(current)
                buffer.append(current.data)
                current = current.right

            # Pop node which has no right node, and push its right node.
            current = stack.pop()
            current = current.left

        # stack.append(current)
        # while stack:
        #     current = stack.pop()
        #     buffer.append(current.data)
        #     if current.left:
        #         stack.append(current.left)
        #     if current.right:
        #         stack.append(current.right)

        # Print the buffer.
        buffer.reverse()
        print(buffer)


def main() -> None:
    # Test array with no reapet elemtn.
    arr = [random.randint(-9, 99) for _ in range(random.randint(16, 47))]
    arr_shuffle = list(set(arr))
    random.shuffle(arr_shuffle)

    # Prepare for insert.
    print(f'# -- Array: {arr_shuffle} '.ljust(170, '-'))
    test = AVL()

    # Insert element one by one.
    for item in arr_shuffle:
        test.insert(item)
    print(test)
    print(f'[Height: {test.height}]')

    # Remove a random item in the arr.
    random_item = random.choice(arr)

    print(f'# -- Remove: [{random_item}] '.ljust(170, '-'))
    test.remove(random_item)
    print(test)
    print(f'[Height: {test.height}]')

    print('# -- Pre Order Traversal. '.ljust(170, '-'))
    test.pre_order()

    print('# -- In Order Traversal. '.ljust(170, '-'))
    test.in_order()

    print('# -- Post Order Traversal. '.ljust(170, '-'))
    test.post_order()


if __name__ == '__main__':
    main()
