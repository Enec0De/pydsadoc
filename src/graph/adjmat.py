#!/usr/bin/env python

from __future__ import annotations

__all__ = ['MGraph']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional
from collections import deque


class MGraph:

    def __init__(self, num_vert: int, /) -> None:
        """Initialize self."""
        # The variables stores the number of the vertices and edges.
        self.nv = num_vert
        self.ne: int = 0

        # The matrix stores the weight between nodes.
        self.adjmat: list[list[float]] = [
            [float('Inf')] * num_vert for _ in range(num_vert)
        ]

        for i in range(num_vert):
            self.adjmat[i][i] = 0
    
    def __str__(self, /) -> str:
        """Display the Adjacency Matrix Graph."""
        buffer: str = '[\\] '

        # First line.
        for i in range(self.nv):
            buffer += f'[{i}] '
        buffer += '\n'

        # The rest lines.
        for j in range(self.nv):
            buffer += f'[{j}] '
            line = [str(self.adjmat[j][k]).rjust(3) for k in range(self.nv)]
            buffer += ' '.join(line) + '\n'

        return buffer

    def bfs(self, v: int, /) -> list[int]:
        """The Breadth First Search."""
        # Define the variables.
        buffer: list[int] = []
        queue: deque[int] = deque([v])
        visit: list[bool] = [False] * self.nv
        visit[v] = True
        buffer.append(v)

        # Traverse by using queue.
        while queue:
            current = queue.popleft()
            for i in range(self.nv):
                if not visit[i] and 0 < self.adjmat[current][i] < float('inf'):
                    visit[i] = True
                    queue.append(i)
                    buffer.append(i)

        # Return the result.
        return buffer
    
    def dfs(self, v: int, /) -> list[int]:
        """The Depth First Search."""
        # Define the variables.
        buffer: list[int] = []
        stack: list[int] = [v]
        visit: list[bool] = [False] * self.nv

        # Traverse by using stack.
        while stack:
            current = stack.pop()
            if visit[current]:
                continue
            visit[current] = True
            buffer.append(current)
            for i in range(self.nv-1, -1, -1):
                if not visit[i] and 0 < self.adjmat[current][i] < float('Inf'):
                    stack.append(i)

        # Return the result.
        return buffer

    def floyd_warshall(self, /):
        ...
    
    def insert_edge(self, v: int, w: int, weight: float = 1, /) -> None:
        """Insert the edge that connect the node v and node w."""
        # Check wether the edge exsits.
        if self.adjmat[v][w] != float('Inf'):
            raise IndexError('edge exsits.')

        # Insertion of the edge.
        self.adjmat[v][w] = weight
        self.adjmat[w][v] = weight
        self.ne += 1


def main() -> None:
    data_list = [
        (3, 4, 70), (1, 2, 1), (5, 4, 50), (2, 6, 50),
        (5, 6, 60), (1, 3, 70), (4, 6, 60), (3, 6, 80),
        (5, 1, 100), (2, 4, 60), (5, 2, 80)
    ]
    test = MGraph(7)
    for edge in data_list:
        test.insert_edge(*edge)
    print(test) 
    print(test.bfs(4))
    print(test.dfs(5))
    

if __name__ == '__main__':
    main()