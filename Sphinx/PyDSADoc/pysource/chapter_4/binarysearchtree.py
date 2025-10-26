#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""The implementation of the binary search tree (BST)."""

# Import necessary module
from __future__ import annotations
from typing import Any, Union, Optional, cast

# Define Sentinel class
class Sentinel:
    """Unique sentinel value."""
    _registry = None

    def __new__(cls):
        if cls._registry is None:
            cls._registry = super().__new__(cls)
        return cls._registry

    def __repr__(self):
        return 'Sentinel'
    
# Initialize sentinel value
_sentinel = Sentinel()

# Special type annotation
T = Union['Sentinel', 'TreeNode']

class TreeNode:
    """The atomic elements of the binary tree implemented with linked list."""

    def __init__(self, data: int) -> None:
        """Initianlize a tree node.
        
        :var data: The data of the node.
        :var left: The pointer to the left node.
        :var right: The pointer to the right node.
        """
        self.data = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class BST:
    """Binary Search Tree impletemented with linked list."""

    def __init__(self):
        """Initianlize an empty binary search tree.
        
        :var head: The pointer to the root node of the binary search tree.
        """
        # The head pointer to the root node of bst
        self.head: Optional[TreeNode] = None 

    def find(self, element: int) -> TreeNode:
        """Non-recursion version of the find operation in binary search tree.
        
        :param element: The element to find.
        :return: The target node.
        """
        # The root node of the bst
        temp = self.head

        while temp is not None and temp.data is not None:
            # Turn to the right node
            if element > temp.data:
                temp = temp.right

            # Turn to the left node
            elif element < temp.data:
                temp = temp.left

            # return the node pointer
            else:
                return temp

        raise IndexError('element not found.')

    def find_min(self) -> TreeNode:
        """Find the minimum element in the bst.
        
        :return: The minimum node.
        """
        temp = self.head

        # Empty bst
        if temp is None:
            raise IndexError('empty binary search tree.')

        # Continue until left node is None
        while temp.left is not None:
            temp = temp.left

        # Return minimun node pointer
        return temp

    def find_max(self) -> TreeNode:
        """Find the maximum element in the bst.
        
        :return: The maximum node 
        """
        temp = self.head

        # Empty bst
        if temp is None:
            raise IndexError('empty binary search tree.')

        # Continue until right node is None
        while temp.right is not None:
            temp = temp.right

        # Return maximun node pointer
        return temp

    def insert(self, element: int, bst: T = _sentinel) -> None:
        """Insert the element into the bst and ensure it remains a bst.
        
        :param element: The element to insert.
        :param bst: The bst to be inserted. Optional, defaults to self.head if 
                    not proviede.
        """
        # Create the new node stores the data
        node: TreeNode = TreeNode(element)

        # Default vaule of the parameter bst, the pointer to the BST head
        if bst is _sentinel:
            if self.head is None:
                self.head = node
            else:
                self.insert(element, self.head)
            return
        
        # bst must be a TreeNode
        else: 
            temp = cast(TreeNode, bst)

        # Insert to left
        if element < temp.data:
            # Check the left pointer
            if temp.left is None:
                temp.left = node
            else:
                self.insert(element, temp.left)

        # Insert to right
        elif element > temp.data:
            # Check the right pointer
            if temp.right is None:
                temp.right = node
            else:
                self.insert(element, temp.right)

    def delete(self):
        ...