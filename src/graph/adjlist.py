#!/usr/bin/env python

from __future__ import annotations

__all__ = ['GNode', 'LGraph']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional
from collections import deque
from functools import total_ordering


@total_ordering
class GNode:
    """Atomic element of the adjacency list."""

    def __init__(self, vertex: int, data: Union[int, float] = 1,
                 next: Optional[GNode] = None, /) -> None:
        """Initialize self."""
        # The index of the vertex.
        self.vertex = vertex

        # The date of the vertex
        self.data = data

        # The pointer to the next vertex.
        self.next = next
    
    def __eq__(self, other: GNode, /) -> bool:
        """Return self == other."""
        return self.data == other.data

    def __lt__(self, other: GNode, /) -> bool:
        """Return self < other."""
        return self.data < other.data

class LGraph:
    """Adjacency list graph."""

    def __init__(self, num_vert: int, /) -> None:
        """Initialize self."""
        # The variables stores the number of vertices and edges.
        self.nv = num_vert
        self.ne: int = 0

        # The adjacency list.
        self.adjlist: list[GNode] = [
            GNode(i, float('Nan')) for i in range(num_vert)
        ]
    
    def __str__(self, /) -> str:
        """Display the Adjacency List Graph."""
        # Form each line one by one in loop.
        buffer = 'Adjacency List Graph: \n'
        for node in self.adjlist:
            # Begin of the line.
            begin = f'[{node.vertex}]'

            # The body of the line.
            body = ''
            while node.next:
                node = node.next
                body += f' -> {node.vertex}({node.data})'

            # Conbination of the elements of the line.
            buffer += begin + body + '\n'
        return buffer.removesuffix('\n')
    
    def bfs(self, node: GNode, /):
        """The Breadth First Search."""
        buffer: list[int] = []
        queue: deque[GNode] = deque([node])
        visit: list[bool] = [False] * self.nv

        current = queue.popleft()
        while node.next:
            node = node.next
            queue.append(node)

        ...

    def dfs(self, /):
        """The Depth First Search."""
        ...
    
    def dijkstra(self, /):
        ...
    
    def insert_edge(self, v: int, w: int, weight: int = 1, /) -> None:
        """Insert the edge connect v and w into the graph."""
        # Pointer to the current node.
        node = self.adjlist[v]

        # Check the exsitence of the edge.
        while node.next:
            node = node.next
            if node.vertex == w:
                raise IndexError('edge exsit.')

        # Insert the edge.
        temp = GNode(w, weight)
        temp.next = node.next
        node.next = temp

        # Directed Graph.
        node = self.adjlist[w]
        temp = GNode(v, weight)
        temp.next = node.next
        node.next = temp
        
        # Number of edges increases.
        self.ne += 1

def main() -> None:
    edges_list = [
        (1, 4), (1, 2), (2, 4), (2, 5), (3, 1), (3, 6),
        (4, 3), (4, 5), (4, 6), (4, 7), (5, 7), (7, 6)
    ]

    weighted_edges_list = [
        (1, 4, 1), (1, 2, 2), (2, 4, 3), (2, 5, 10), (3, 1, 4), (3, 6, 5),
        (4, 3, 2), (4, 5, 2), (4, 6, 8), (4, 7, 4), (5, 7, 6), (7, 6, 1)
    ]

    test = LGraph(8)
    for v, w in edges_list:
        test.insert_edge(v, w)
    print(test)

    test_weighted = LGraph(8)
    for v, w, weight in weighted_edges_list:
        test_weighted.insert_edge(v, w, weight)
    print(test_weighted)

if __name__ == '__main__':
    main()
