#!/usr/bin/env python

from __future__ import annotations

__all__ = ['GNode', 'LGraph']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional
from collections import deque
from heapq import heappop, heappush
from functools import total_ordering


@total_ordering
class GNode:
    """Atomic element of the adjacency list."""

    def __init__(self, vertex: int, data: float = 1,
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
        return buffer
    
    def bfs(self, start:int , /) -> list[int]:
        """The Breadth First Search."""
        # Define the variables.
        node = self.adjlist[start]
        buffer: list[int] = []
        queue: deque[GNode] = deque([node])
        visit: list[bool] = [False] * self.nv
        visit[node.vertex] = True
        buffer.append(node.vertex)

        # Visit the node poped from the queue.
        while queue:
            current = queue.popleft()

            # Push the neighbour node of current into the queue.
            node = current
            while node.next:
                node = node.next
                if not visit[node.vertex]:
                    visit[node.vertex] = True
                    queue.append(self.adjlist[node.vertex])
                    buffer.append(node.vertex)
        
        return buffer

    def dfs(self, start: int, /) -> list[int]:
        """The Depth First Search."""
        # Define the variables.
        node = self.adjlist[start]
        buffer: list[int] = []
        visit: list[bool] = [False] * self.nv


        # # Interesting.
        # stack: list[GNode] = []

        # current = node
        # while current or stack:
        #     while current:
        #         current = self.adjlist[current.vertex]
        #         stack.append(current)
        #         visit[current.vertex] = True
        #         buffer.append(current.vertex)
        #         while current and visit[current.vertex]:
        #             current = current.next

        #     current = stack.pop()
        #     temp = current
        #     while current and visit[current.vertex]:
        #         current = current.next
        #     if current is not None:
        #         stack.append(temp)


        # # Function stacks simulation.
        # stack: list[tuple[GNode, GNode]] = [(node, node)]
        # visit[node.vertex] = True
        # buffer.append(node.vertex)

        # while stack:
        #     current, ptr = stack.pop()

        #     while ptr.next:
        #         ptr = ptr.next
        #         if not visit[ptr.vertex]:
        #             visit[ptr.vertex] = True
        #             buffer.append(ptr.vertex)
        #             stack.append((current, ptr))
        #             stack.append(
        #                 (self.adjlist[ptr.vertex], self.adjlist[ptr.vertex])
        #             )
        #             break
            
        
        # Traverse children.
        stack: list[GNode] = [node]
        stack_reverse : list[GNode] = []

        # Visit the node poped from the stack.
        while stack:
            current = stack.pop()
            if visit[current.vertex]:
                continue
            
            visit[current.vertex] = True
            buffer.append(current.vertex)

            # Push all the neighbour node of the current into the stack.
            while current.next:
                current = current.next
                if not visit[current.vertex]:
                    # Stores the neighbour and visit the neighber.
                    stack_reverse.append(self.adjlist[current.vertex])
            
            # Reverse the element in the stack.
            for _ in range(len(stack_reverse)):
                stack.append(stack_reverse.pop())

        return buffer
    
    def dijkstra(self, start: int, /) -> list[list[float]]:
        r"""The Dijkstra's algorithm for finding the shortest paths.
        
        Combining with the prioprity queue, the time complexity is
        :math:`O(\vert E \vert \log \vert V \vert)`.
        """
        # The result list stores the [path, dist] of the node.
        result: list[list[float]] = [
            [-1, float('Inf')] for _ in range(self.nv)
        ]

        # The ste stores the mark of the node that is not visited.
        vert_set: set[int] = {i for i in range (self.nv)}

        # Initialize the variables.
        result[start][1] = 0
        heap: list[GNode] = [GNode(start, 0)]

        # Get minimum dist from heap.
        # Add the vertex into the set of node visited.
        for _ in range(self.nv):
            node = heappop(heap)
            vert_set -= {node.vertex}

            # Traverse the neighbour of the node and update the dist.  
            current = self.adjlist[node.vertex]
            while current.next:
                current = current.next
                if current.vertex in vert_set:
                    dist_sv = result[node.vertex][1]
                    dist_vw = current.data
                    dist_sw = result[current.vertex][1]
                    if dist_sv + dist_vw < dist_sw:
                        result[current.vertex][0] = node.vertex
                        result[current.vertex][1] = dist_sv + dist_vw
                        temp = GNode(current.vertex, result[current.vertex][1])
                        heappush(heap, temp)

        return result
    
    def insert_edge(self, v: int, w: int, weight: float = 1, /) -> None:
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
    
    def krskal(self):
        r"""The Kruskal's algorithm that finds a minumum spanning tree.
        
        Time complexity is :math:`O(\vert E \vert).`
        """
        ...


def main() -> None:
    # Create two LGraphs.
    test = LGraph(8)
    test_weighted = LGraph(8)

    # Connect the vertices of the two Lgraphs.
    edges_list = [
        # (1, 4), (1, 2), (2, 4), (2, 5), (3, 1), (3, 6),
        # (4, 3), (4, 5), (4, 6), (4, 7), (5, 7), (7, 6)
        (4, 1), (4, 2), (4, 3), (4, 5), (4, 6), (4, 7), 
    ]

    weighted_edges_list = [
        (1, 4, 1), (1, 2, 2), (2, 4, 3), (2, 5, 10), (3, 1, 4), (3, 6, 5),
        (4, 3, 2), (4, 5, 2), (4, 6, 8), (4, 7, 4), (5, 7, 6), (7, 6, 1)
    ]

    for v, w in edges_list:
        test.insert_edge(v, w)

    for v, w, weight in weighted_edges_list:
        test_weighted.insert_edge(v, w, weight)

    print(test, test_weighted)

    print(test.bfs(2), test.dfs(4))
    print(test_weighted.bfs(2), test_weighted.dfs(3))

    # Dijkstra
    print('# -- Dijkstra --')
    result = test_weighted.dijkstra(3)
    for item in result:
        print(item)

if __name__ == '__main__':
    main()
