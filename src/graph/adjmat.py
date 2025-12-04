#!/usr/bin/env python
"""The Graph data structure."""

__all__ = ['MGraph']
__version__ = '0.1'
__author__ = 'Aina'

from collections import deque
from heapq import heappop, heappush


class MGraph:
    """Adjacency matrix graph."""

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

    def bfs(self, start: int, /) -> list[int]:
        """The Breadth First Search."""
        # Define the variables.
        buffer: list[int] = []
        queue: deque[int] = deque([start])
        visit: list[bool] = [False] * self.nv
        visit[start] = True
        buffer.append(start)

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

    def dfs(self, start: int, /) -> list[int]:
        """The Depth First Search."""
        # Define the variables.
        buffer: list[int] = []
        stack: list[int] = [start]
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

    def floyd_warshall(self, /) -> tuple[list[list[float]], list[list[float]]]:
        r"""The Floyd-Warshall algorithm for finding shortest paths.

        Time complexity is :math:`O(\vert V \vert ^3)`.
        """
        dist: list[list[float]] = self.adjmat.copy()
        path: list[list[float]] = [[-1] * self.nv for _ in range(self.nv)]

        # Add node k into path.
        for k in range(self.nv):
            # Operation between every nodes.
            for i in range(self.nv):
                for j in range(self.nv):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        path[i][j] = k

        return dist, path

    def insert_edge(self, v: int, w: int, weight: float = 1, /) -> None:
        """Insert the edge that connect the node v and node w."""
        # Check wether the edge exsits.
        if self.adjmat[v][w] != float('Inf'):
            raise IndexError('edge exsits.')

        # Insertion of the edge.
        self.adjmat[v][w] = weight
        self.adjmat[w][v] = weight
        self.ne += 1

    def prim(self, start: int = 1, /) -> 'MGraph':
        r"""The Prim's algorithm that finds a minumum spanning tree.

        Time complexity is :math:`O(\vert V \vert ^2)`.
        """
        result = MGraph(self.nv)
        vert_set = {i for i in range(self.nv)}
        # Special handling.
        vert_set -= {0}

        # The minimun heap stores (dist, from, target).
        heap: list[tuple[float, int, int]] = [(0, start, start)]
        while vert_set:
            # Get minimun edge.
            current = heappop(heap)

            # Insert the edge.
            if current[2] in vert_set:
                if current[1] != current[2]:
                    result.insert_edge(current[1], current[2], current[0])
            else:
                continue
            vert_set -= {current[2]}

            # Update the dist heap.
            for vertex in vert_set:
                if (dist := self.adjmat[current[2]][vertex]) < float('Inf'):
                    heappush(heap, (dist, current[2], vertex))

        return result


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

    # Floyd Warshall
    print('# -- Floyd Warshall --')
    dist, path = test.floyd_warshall()
    for line in dist:
        out = [item.rjust(3) for item in map(str, line)]
        print(out)
    print()
    for line in path:
        out = [item.rjust(2) for item in map(str, line)]
        print(out)

    # Prim's Algorithm
    print("# -- Prim's Algorithm --")
    prim = test.prim()
    print(prim)


if __name__ == '__main__':
    main()
