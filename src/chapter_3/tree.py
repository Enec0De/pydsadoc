#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""The implementation of the binary tree."""

from __future__ import annotations
from typing import Union, Optional, Literal, cast


class TreeNode:
    """The node of the binary tree.
    
    :var data: The data of the node.
    :var left: The pointer to the left child
    :var right: The pointer to the right child
    """

    def __init__(self, data: Optional[int] = None) -> None:
        self.data = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BinaryTree:
    """The binary tree impelemented with linked list.
    
    :var head: The pointer to the tree node.
    """

    def __init__(self) -> None:
        """Initialize the empty binary tree with None TreeNode."""
        self.head: Optional[TreeNode] = None

    def pre_order_traversal(
        self, node: Union[TreeNode, None, Literal['default']] = 'default'
    ) -> None:
        """The pre-order traversal impelementaiton with recursion."""
        # Node is the binary tree itself or the sub tree of the binary tree
        if node == 'default':
            bin_tree = self.head
        else:
            bin_tree = node

        # Recursion until the node is None
        if bin_tree is not None:
            data = cast(int, bin_tree.data)
            print(data)
            self.pre_order_traversal(bin_tree.left)
            self.pre_order_traversal(bin_tree.right)

    def in_order_traversal(self) -> None:
        """The in-order traversal implementation with stack."""
        # The varibale of the root node of the tree
        bin_tree = cast(TreeNode, self.head)
        stack: list[TreeNode] = [bin_tree]

        # Stack is not empty
        while stack:
            # befor pop the current node, push the left tree
            while bin_tree.left is not None:
                stack.append(bin_tree.left)
                bin_tree = bin_tree.left

            # pop the node don't have left node
            # and process the right tree
            if stack:
                t = stack.pop()
                print(t.data)
                t = t.right

        ...

    def post_order_traversal(self) -> None:
        """Not implemented."""
        ...