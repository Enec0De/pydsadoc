#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Optional, Union


T = Union[None, 'SentinelNode', 'TreeNode']
B = Union[None, 'Sentinel', 'TreeNode']
R = Union['SentinelNode', 'TreeNode']

class Sentinel:

    _registry = None

    def __new__(cls):
        if cls._registry is None:
            cls._registry = super().__new__(cls)
        return cls._registry

    def __repr__(self):
        return 'Sentinel'

_sentinel = Sentinel()

class SentinelNode:

    def __init__(self) -> None:
        self.next: Optional[TreeNode] = None

class TreeNode:
    
    def __init__(self, data: int) -> None:
        self.data = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.flag: bool = False


class BST:

    def __init__(self) -> None:
        # Sentinel node, point to the first node or None
        self.head: SentinelNode = SentinelNode()

    def insert(self, element: int, bst: B = _sentinel) -> TreeNode:
        """ Recursively insert.
        
        :param element: The element to be inserted.
        :param bst: The subtree to insert, TreeNode or None.
        :return: The root node of the current tree. But it first return 
                 SentinelNode.
        """
        # Define the variables
        # Temp should be None or TreeNode. But head is SentinelNode
        if isinstance(bst, Sentinel):
            temp: T = self.head
        else:
            temp =  bst
            
        # Subtree is not empty, and point to the TreeNode
        if temp is not None and not isinstance(temp, SentinelNode):
            # Traverse to the left to insert        
            if element < temp.data:
                temp.left = self.insert(element, temp.left)

            # Traverse to the right to insert
            elif element > temp.data:
                temp.right = self.insert(element, temp.right)

            # Equal element
            else:
                raise ValueError('element exsit.')
                
        # Temp point to the sentinel node
        elif isinstance(temp, SentinelNode):
            temp.next = self.insert(element, temp.next)
        # Empty subtree, substitute the root node
        else:
            temp = TreeNode(element)

        # New root node of the current tree 
        return temp # type: ignore


    

def build_tree(l: list) -> BST:
    bst = BST()
    for i in range(0, len(l)):
        bst.insert(l[i])
    return bst

def check(node: TreeNode, i: int) -> bool:
    if node.flag is True:
        if i < node.data and node.left is not None:
            return check(node.left, i)
        elif i > node.data and node.right is not None:
            return check(node.right, i)
        else:
            return False

    else:
        if i == node.data:
            node.flag = True
            return True
        else:
            return False
        

def judge(bst: BST, list: list[int]) -> bool:
    if bst.head.next is not None:
        node = bst.head.next
        for i in range(0, len(list)):
            if not check(node, list[i]):
                return False
        return True

    else:
        raise IndexError('judge empty bst.')


def reset(treenode: Optional[TreeNode]) -> None:
    if treenode is not None:
        treenode.flag = False 
        if treenode.left is not None:
            reset(treenode.left)
        if treenode.right is not None:
            reset(treenode.right)


def main():
    # Input N and L
    N = input('Input N (number of sequences to be input): ')
    while bool(int(N)):
        a = []
        for i in range(0, int(N)):
            a.append(input('-->').split(' '))

        # Build tree from a[0]
        bst = build_tree(a[0])

        # Compare other list and bst
        for j in range(1, int(N)):
            if judge(bst,a[j]):
                print('Yes.')
            else:
                print('No.')
            
            reset(bst.head.next)

        # Next lopp
        N = input('Input N: ')


if __name__ == '__main__':
    main()