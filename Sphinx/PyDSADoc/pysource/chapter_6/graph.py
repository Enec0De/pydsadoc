#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Composed with Non-empty set of Vertex and the set of the Edge."""

from __future__ import annotations
from typing import Union, Optional
from collections import deque
import weakref

WeightType = Union[int]
DataType = Union[int]


class Edge:
    """The edge of two given vertices."""

    def __init__(self, v: int, w: int, weight: WeightType = 1) -> None:
        """Initialize an edge of two given vertices.
        
        :param v: The vertex :math:`v`.
        :param w: The vertex :math:`w`.
        :param weight: The weight of two vertices. Optional, defaults to 1 if
                       not provided.
        """
        if v == w:
            raise ValueError('self connected')
        self.v = v
        self.w = w
        self.weight = weight

class MGraph:
    "Implement with Adjacency Matrix."

    def __init__(self, vertex_num: int) -> None:
        """Create and return an empty Graph with given number of the vertices.
        
        :param vertex_num: The number of the vertices in the graph.
        :var data: The data list of the vertex.
        :var edge: The weight lists of the edges.
        :var nv: The number of the vertices.
        :var ne: The number of the edges.
        """
        # Data of the vertex
        self.data: list[Optional[DataType]] = [None] * vertex_num

        # Weight of the edges
        self.edge: list[list[WeightType]] = [
            ([0]*vertex_num) for i in range(0, vertex_num)
        ]

        # Number of vertices
        self.nv: int = vertex_num

        # Number of edges
        self.ne: int = 0


    def insert_vertex(self, vertex) -> MGraph:
        """Insert vertex :math:`v` into the Graph."""
        ...

    def insert_edge(self, edge: Edge) -> None:
        """Insert edge :math:`e` into the Graph."""
        self.edge[edge.v][edge.w] = edge.weight
        self.edge[edge.w][edge.v] = edge.weight
        self.ne += 1
        ...

    def dfs(self, vertex) -> None:
        """The algorithm of Depth First Search, DFS."""
        # Visit the current vertex

        # For every vertex untouched, recursively visit it
        # for neibor in (neibor of v):
        #     if (untouched):
        #         self.dfs(neibor)

        ...

    def bfs(self, graph, vertex) -> None:
        """The algorithm of Breadth First Search, BFS."""
        # Visit the vertex and addqueue the current vertex
        # Dequeue from the queue
        # Visit the vertex pop from the queue and push the vertex untouched

        # visit(current_vertex)
        # queue.append(current_vertex)
        # while queue:
        #     current_vertex = queue.popleft()
        #     for neibor in (neibor of v):
        #         if (untouched):
        #             visit neibor
        #             queue.append(neibor)

        ...

    def shortest_path(self, vertex, list) -> None:
        """Calculate the shortest path from vert :math:`v` to the others."""
        ...

    def mst(self) -> None:
        """Calculate the MST."""
        ...
    
    def build_graph(self) -> None:
        """Build the graph in an interactive way."""
        user_input =  int(input("Input 'ne': "))

        for i in range(0, user_input):
            edge_input = input("Input 'V W': ").split(' ')
            v = int(edge_input[0])
            w = int(edge_input[1])
            # weight = int(edge_input[2])
            self.insert_edge(Edge(v, w))

    def __str__(self) -> str:

        output = ''
        for j in range(0, self.nv):
            for i in range(0, self.nv):
                output = output + str(self.edge[i][j]) + ' '
            output += '\n'

        return output


class LGraph:
    ...


def main():
    g = MGraph(10)
    g.build_graph()
    print(g)

if __name__ == '__main__':
    main()