#!/usr/bin/env python

from __future__ import annotations

__all__ = ['UnionFind']
__version__ = '0.1'
__author__ = 'Aina'

import random


class UnionFind:
    r"""Implementation of the DSU with a sequential list.
    
    It's notably that the amortized time complexity of DSU is
    :math:`O(\alpha(n))`.
    """

    def __init__(self, num_vert: int, /, *args, **kwargs) -> None:
        """Initialize self."""
        self.parent: list[int] = [-1] * num_vert

    def __str__(self, /) -> str:
        """Implement built-in function ``print()``."""
        # Define variables.
        string ='# -- Union Find: --\n'
        length = len(self.parent)
        count = [[] for _ in range(length)]

        # Count the child of the root.
        for i in range(length):
            if self.find(i) >= 0:
                count[self.find(i)].append(i)

        # Constrct the string.
        for j in range(length):
            if count[j]:
                string += f'[{j}]: ' + ', '.join(map(str, count[j]))
                string += '\n'

        # Return the string.
        return string

    def find(self, x: int, /) -> int:
        r"""The find operation with path compression.
        
        The worst-case time complexity is :math:`O(\log n)`. 
        """
        # The boundary condition for recursion.
        if self.parent[x] < 0:
            return x

        # Recursively find root.
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x: int, y: int, /) -> None:
        r"""The union operation by rank.
        
        The worst-case time complexity is :math:`O(\log n)`.
        """
        # Find the root of the two nodes.
        r_x = self.find(x) 
        r_y = self.find(y)

        # Do nothing.
        if r_x == r_y:
            return
        
        # Union by rank.
        if self.parent[r_x] >= self.parent[r_y]:
            self.parent[r_x] += self.parent[r_y]
            self.parent[r_y] = r_x
        else:
            self.parent[r_y] += self.parent[r_x]
            self.parent[r_x] = r_y

# -- Test module -------------------------------------------------------
#
def main() -> None:
    # Create a new DSU.
    random_lenght = random.randint(4, 32)
    dsu = UnionFind(random_lenght)

    # Union elements randomly.
    for _ in range(random_lenght//2):
        x = random.randint(0, random_lenght-1)
        y = random.randint(0, random_lenght-1)
        dsu.union(x, y)

    # Print the result.
    print(dsu.parent)
    print(dsu)

if __name__ == '__main__':
    main()