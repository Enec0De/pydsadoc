#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Implementation of the Disjoint-Set Union (DSU), also called Union-Find."""

from __future__ import annotations
from typing import Optional, Union


ElementType = Union[int]


class SetNode:
    """The atomic element of the class UnionFind."""

    def __init__(self, data: ElementType, parent: int = -1) -> None:
        self._data: Optional[ElementType] = data
        self.parent: int = parent

    @property
    def data(self) -> ElementType:
        if isinstance(self._data, ElementType):
            return self._data
        else:
            raise ValueError('data not set')

    @data.setter
    def data(self, data: Optional[ElementType]) -> None:
        self._data = data

    def __eq__(self, other: ElementType) -> bool:
        return self.data == other
    

class UnionFind:
    """Implementation of DSU with list."""

    def __init__(self) -> None:
        """Initialize the UnionFind."""
        self.element: list[SetNode] = []
        self.length: int = len(self.element)

    def insert(self, node: SetNode) -> None:
        self.element.append(node)

    def find(self, item: ElementType) -> int:
        # Find the item index in the DSU
        try: 
            i = self.element.index(item)  # type: ignore
        except ValueError:
            raise ValueError('item not found')

        while self.element[i].parent != -1:
            # Variable i point to the father of the node
            i = self.element[i].parent

        # Loop finish, i point to the root of the set
        return i

    def union(self, x: ElementType, y: ElementType) -> None:
        id_x = self.find(x)
        id_y = self.find(y)

        # Disjoint set, union them
        if id_x != id_y:
            self.element[id_y].parent = id_x

        
def main():
    list_node = [(1, -1), (2, 0), (3, -1), (4, 0), (5, 2),
                 (6, -1), (7, 0), (8, 2), (9, 5), (10, 5)]
    s = UnionFind()
    for x, y in list_node:
        s.insert(SetNode(x, y))

    print(s.find(2))
    print(s.find(5))

    s.union(2, 5)
    print(s.find(2))
    print(s.find(5))
    print(s.length)



if __name__ == '__main__':
    main()