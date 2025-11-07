#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional
from collections import deque
from heapq import heapify, heappush, heappop
import weakref
import copy


W = Union[int, float]
INF = float('inf')

class GNode:
    """Atomic element of the adjacency matrix."""

    def __init__(self, weight: W = INF, cost: W = INF):
        self.weight = weight
        self.cost = cost


class MGraph:

    def __init__(self, num_vert: int) -> None:
        self.adjmatrix = [
            [GNode() for i in range(num_vert)] for j in range(num_vert)
        ]
        self.nv = num_vert
        self.ne: int = 0

    def __str__(self) -> str:
        output = ''
        for node in self.adjmatrix:
            for i in range(self.nv):
                gnode = node[i]
                output += f'[w: {gnode.weight} c: {gnode.cost}] '
            output += '\n'


        return output

    def join(self, v: int, w: int, weight: W, cost: W):
        self.adjmatrix[v][w].weight = weight
        self.adjmatrix[v][w].cost = cost 

        self.adjmatrix[w][v].weight = weight
        self.adjmatrix[w][v].cost = cost
        self.ne += 1

    def dijkstra(self, begin: int) -> dict:
        result: dict[str, list[W]] = {
            'dist': [INF] * self.nv,
            'path': [-1] * self.nv,
            'cost': [INF] * self.nv
        }
        check: set[int] = set(i for i in range(self.nv))

        result['dist'][begin] = 0
        result['cost'][begin] = 0

        minheap = [(result['dist'][begin], begin)]

        while minheap:
            d, v = heappop(minheap)
            if not v in check:
                continue
            check -= {v}
            for w in check:
                if self.adjmatrix[v][w].weight < INF:
                    dist = d + self.adjmatrix[v][w].weight
                    cost = result['cost'][v] + self.adjmatrix[v][w].cost
                    if result['dist'][w] > dist:
                        result['dist'][w] = dist
                        result['path'][w] = v
                        result['cost'][w] = cost
                        heappush(minheap, (dist, w))
                    elif result['dist'][w] == dist and result['cost'][w] > cost:
                        result['path'][w] = v
                        result['cost'][w] = cost
                    
        return result


def main() -> None:
    # Sample input: (v, w, dist, cost)
    sample_imput = [
        (0, 1, 1, 20),
        (1, 3, 2, 30),
        (0, 3, 4, 10),
        (0 ,2, 2, 20),
        (2, 3, 1, 20)
    ]
    mgraph = MGraph(4)
    for item in sample_imput:
        mgraph.join(*item)

    dj = mgraph.dijkstra(0)
    print (mgraph)
    print(f"dist: {dj['dist']}")
    print(f"path: {dj['path']}")
    print(f"cost: {dj['cost']}")

if __name__ == '__main__':
    main()