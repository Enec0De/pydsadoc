#!/urs/bin/evn python
# -*- coding: UTF-8 -*-
"""Implement algorithms of BFS, dijkstra and xxxx in adjacency list graph. """

from __future__ import annotations
from typing import Union, Optional, cast
from collections import deque
from heapq import heapify, heappop, heappush
import weakref

# Define infinity distance symbol
inf = float('inf')

# Weight
W = Union[int, float]

class GNode:
    """Atomic element of the adjacency linked list."""

    def __init__(self, vertex: int, weight: W = inf) -> None:
        # Define the variables for next vertex and weight
        self.vertex = vertex
        self.weight = weight
        self.next: Optional[GNode] = None


class AdjNode:
    """Atomic element of the adjacency list."""

    def __init__(self, vertex: int) -> None:
        # Define the pointer to the adjacency vertex
        self.vertex = vertex
        self.next: Optional[GNode] = None

        # Used by self.dijkstra()
        self._dist: Union[int, float]= inf

    def __lt__(self, other: AdjNode) -> bool:
        return self._dist < other._dist


class LGraph:
    """Adjacency list graph"""

    def __init__(self, num_vert: int) -> None:
        # The adjacency list of the LGraph
        self.adjlist: list[AdjNode] = [AdjNode(i) for i in range(1, num_vert+1)]

        # Stores the number of the vertices and edges
        self.nv = num_vert
        self.ne: int = 0

    def __str__(self) -> str:
        """Display the status of the LGraph."""
        output = ''

        for i in range(1, self.nv+1):
            output += f'[{i}] '
            ptr = self.adjlist[i-1]
            while ptr.next is not None:
                ptr = ptr.next
                output += f'->{ptr.vertex}({ptr.weight}) '
            output += '\n'
        
        return output

    def connect(self, v: int, w: int, weight: int = 1) -> None:
        """Connect the spcified vertex."""
        # Create a new GNode
        temp = GNode(w, weight)

        # Insert the temp GNode into the adjacency linked list
        # The AdjNode[v-1] stand for the node v
        temp.next = self.adjlist[v-1].next
        self.adjlist[v-1].next = temp

    def bfs(self, begin: int) -> list:
        """Unweight single source shortest path algorithms.
        
        :param begin: The source vertex.
        """
        # Map begin to index of list
        index = begin - 1
        # Initialize the list stores the result
        result: list[dict[str, W]] = [
            {'dist': -1,'path': -1} for i in range(0, self.nv)
        ]

        # Queue for BFS
        queue: deque[AdjNode] = deque([])
        queue.append(self.adjlist[index])

        # Initialize the begin node
        result[index]['dist'] = 0

        while queue:
            v = queue.popleft()
            # Map vertex to he index of the node
            v_index = v.vertex - 1
            w = v
            while w.next is not None:
                w = w.next
                # Map vertex to the index of the node
                w_index = w.vertex - 1

                # The node have not been touched
                if result[w_index]['dist'] == -1:
                    # Distance
                    result[w_index]['dist'] = result[v_index]['dist'] + 1 
                    # Path from
                    result[w_index]['path'] = v.vertex
                    # Append it into queue
                    queue.append(self.adjlist[w_index])

        return result

    def dijkstra(self, begin: int) -> list:
        # Create the result list
        result = [
            {'dist': inf, 'path': -1} for i in range(0, self.nv)
        ]

        # Map begin to index of list
        index = begin - 1

        # Initialize the source node
        result[index]['dist'] = 0
        self.adjlist[index]._dist = 0

        # Create the [Node] minheap
        minheap: list[AdjNode] = [self.adjlist[i] for i in range(self.nv)]
        heapify(minheap)

        # The set of all nodes not have been considered
        S = set(self.adjlist)

        # Select the nodes in S
        while S:
            # First, select the minimum dist node
            current = heappop(minheap)
            S -= {current}
            v = current

            # Update the dist for all neighbor nodes of v in set S
            # Treaverse the neighbor vertex of the v
            v_index = v.vertex - 1 
            w = v
            while w.next is not None:
                w = w.next
                # Map the vertex to the index of the node
                w_index = w.vertex - 1
                if (self.adjlist[w_index] in S,
                    result[w_index]['dist']
                    > result[v_index]['dist'] + w.weight):
                    # Handel the result
                    result[w_index]['dist'] = result[v_index]['dist'] + w.weight 
                    result[w_index]['path'] = v.vertex

                    # Modify the data in heap
                    self.adjlist[w_index]._dist = result[w_index]['dist']

            # Handle the heap
            heapify(minheap)

        # Reset the valeu of the _dist attribute
        for node in self.adjlist:
            node._dist = inf

        return result


def main() -> None:
    # Initial lize the unweight graph
    edges_list = [
        (1, 4), (1, 2), (2, 4), (2, 5), (3, 1), (3, 6),
        (4, 3), (4, 5), (4, 6), (4, 7), (5, 7), (7, 6)
    ]
    unweight_graph = LGraph(7)
    for edges in edges_list:
        v, w = edges
        unweight_graph.connect(v, w)

    # Print the resutl
    print('\n''# '+'-'*2+' Unweight Graph '+'-'*55)
    print(unweight_graph)
    for item in unweight_graph.bfs(3):
        print(item)
    print()

    # Initial lize the weight graph
    w_edges_list = [
        (1, 4, 1), (1, 2, 2), (2, 4, 3), (2, 5, 10), (3, 1, 4), (3, 6, 5),
        (4, 3, 2), (4, 5, 2), (4, 6, 8), (4, 7, 4), (5, 7, 6), (7, 6, 1)
    ]
    weight_graph = LGraph(7)
    for w_edges in w_edges_list:
        v, w, weight = w_edges
        weight_graph.connect(v, w, weight)

    # Print the resutl
    print('\n''# '+'-'*2+' Weight Graph '+'-'*58)
    print(weight_graph)
    for item in weight_graph.dijkstra(1):
        print(item)


if __name__ == '__main__':
    main()






