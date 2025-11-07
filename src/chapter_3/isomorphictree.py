#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""The algorithm of isomorphic tree."""

from __future__ import annotations
from typing import Optional


class BinaryTree:
    """Build an binary tree from given datas."""

    def __init__(self) -> None:
        self.head = []
        if self.head:
            self.root:int = self._find_root()

    def _find_root(self) -> int:
        check = [False] * len(self.head)

        for i in range(0, len(self.head)):
            if self.head[i][1] != '-1':
                check[int(self.head[i][1])] = False
            if self.head[i][2] != '-1':
                check[int(self.head[i][2])] = False

        for j in range(0, len(check)):
            if check[j]:
                return j

        raise IndexError('no root of the binary tree.')

    def append(self, list: list[str]) -> None:
        self.head.append(list)



def isomorphic(bin_tree_1, bin_tree_2) -> bool:
    ...


if __name__ == '__main__':

    n = input('Input the number of the node: ')
    bin_tree_1 = BinaryTree()
    bin_tree_2 = BinaryTree()

    for i in range(0, int(n)):
        l = input('-1->').split(' ')
        bin_tree_1.append(l)

    for i in range(0, int(n)):
        l = input('-2->').split(' ')
        bin_tree_2.append(l)

    print(bin_tree_1.head)
    print(bin_tree_2.head)



    # if isomorphic(bin_tree_1, bin_tree_2):
    #     print('Yes.')    
    # else:
    #     print('No.')