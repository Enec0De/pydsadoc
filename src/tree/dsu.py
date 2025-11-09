#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
import random


class UnionFind:
    """Implementation of the DSU with a sequential list."""

    def __init__(self, num_vert: int, /, *args, **kwargs) -> None:
        """Initialize self."""
        self.parent: list[int] = [-1] * num_vert

    def __str__(self, /) -> str:
        """Implement built-in function ``print()``."""
        # Define variables
        string =''
        length = len(self.parent)
        count = [[] for _ in range(length)]

        # Count the child of the root
        for i in range(length):
            if self.find(i) >= 0:
                count[self.find(i)].append(i)

        # Constrct the string
        for j in range(length):
            if count[j]:
                string += f'[{j}]: ' + ', '.join(map(str, count[j]))
                string += '\n'

        # Return the string
        return string

    def find(self, x: int, /) -> int:
        """The find operation with path compression."""
        # The boundary condition for recursion
        if self.parent[x] < 0:
            return x

        # Recursively find root
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x: int, y: int, /) -> None:
        """The union operation by rank."""
        # Find the root of the two nodes
        r_x = self.find(x) 
        r_y = self.find(y)

        # Do nothing
        if r_x == r_y:
            return
        
        # Union by rank
        if self.parent[r_x] >= self.parent[r_y]:
            self.parent[r_x] += self.parent[r_y]
            self.parent[r_y] = r_x
        else:
            self.parent[r_y] += self.parent[r_x]
            self.parent[r_x] = r_y

# - Test module --------------------------------------------------------
def main() -> None:
    # Create a new DSU
    dsu = UnionFind(10)

    # Randomly union elements
    for _ in range(5):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        dsu.union(x, y)

    # Print the result
    print(dsu)

if __name__ == '__main__':
    main()