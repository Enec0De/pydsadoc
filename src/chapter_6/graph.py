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

        # Weight of the edges, or adjacency matrix.
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

        for _ in range(0, user_input):
            edge_input = input("Input 'V W': ").split(' ')
            v = int(edge_input[0])
            w = int(edge_input[1])
            # weight = int(edge_input[2])
            self.insert_edge(Edge(v, w))

    def __str__(self) -> str:

        output = '   '
        for k in range(0, self.nv):
            output += f'[{k}]'
        output += '\n'

        for j in range(0, self.nv):
            output += f'[{j}]'
            for i in range(0, self.nv):
                output = output + ' ' + str(self.edge[i][j]) + ' '
            output += '\n'

        return output



class EdgeNode:
    """The head of the Adjacency List."""

    def __init__(self, vertex: int, weight: int = 1) -> None:
        # The index of the vertex which is the adjacency point of the sentinel
        self.vertex = vertex

        # Weight of the edge
        self.weight = weight

        # The next node
        self.next: Optional[EdgeNode] = None 

class AdjItem:
    """The node of the Adjacency List, or the sentinel node of linked list."""

    def __init__(self) -> None:
        # The Adjacency point of the vertex represented by sentinel node
        self.next: Optional[EdgeNode] = None

        # Data of the vertex
        self.data: Optional[DataType] = None


class LGraph:
    """Implement with Adjacency List."""

    def __init__(self, vertex_num: int) -> None:
        """Create and return an empty Graph with given number of the vertices.
        
        :param vertex_num: The number of the vertices in the graph.
        """
        # Adjacency list, comprised of linked list
        # Data of the vertex is stored in the sentinel node of the linked list
        # Weight of the edege is stored in the data node of the linked list
        self.adjlist: list[AdjItem] = [AdjItem() for _ in range(0, vertex_num)]

        # Number of vertices 
        self.nv: int = vertex_num
        
        # Number of edges
        self.ne: int = 0
    

    def insert_edge(self, edge: Edge) -> None:
        """Insert edge :math:`e` in to the LGraph."""
        # Create the EdgeNode
        temp_v = EdgeNode(edge.v, edge.weight)
        temp_w = EdgeNode(edge.w, edge.weight)
        vertex_v = self.adjlist[edge.v]
        vertex_w = self.adjlist[edge.w]

        # Insert the temp right after the corresponding vertex
        temp_w.next = vertex_v.next 
        vertex_v.next = temp_w

        # Vice versa
        temp_v.next = vertex_w.next
        vertex_w.next = temp_v

        # Insert the number count of the edges
        self.ne += 1

    def build_graph(self) -> None:
        """Build the graph in an interactive way."""
        # Input the number of edges you want to add
        user_input = int(input("Input 'ne': "))

        # Insert all edges
        for _ in range(0, user_input):
            edge_input = input("input 'V M': ").split(' ')
            v, w = int(edge_input[0]), int(edge_input[1])
            self.insert_edge(Edge(v, w))
        
    def __str__(self) -> str:

        output = ''
        index = 0
        for i in self.adjlist:
            # Create pointer to the AdjItem
            ptr = i
            output += f'[{index}] '
            while ptr.next is not None:

                # Treaverse to the next node
                ptr = ptr.next
                
                # Stores the node of the index
                output = output + '-> '+ str(ptr.vertex) + ' '

            # New line
            index += 1
            output += '\n'
        
        return output



def main():
    g = LGraph(10)
    g.build_graph()
    print(g)

if __name__ == '__main__':
    main()