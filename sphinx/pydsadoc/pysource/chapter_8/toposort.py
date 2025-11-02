#!/usr/bin/env
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional
from collections import deque
from heapq import heapify, heappop, heappush
import weakref
import copy

W = Union[int, float]
INF = float('inf')

class AdjVNode:

    def __init__(self, vertex: int, weight: W = INF) -> None:
        self.vertex = vertex
        self.weight = weight
        self.next: Optional[AdjVNode] = None

        self.indegree: int = 0

class LGraph:

    def __init__(self, num_vert: int) -> None:
        self.adjlist = [AdjVNode(i+1) for i in range (num_vert)]
        self.nv = num_vert
        self.ne = 0

    def join(self,v: int, w:int ,weight: W = 1) -> None:

        temp = AdjVNode(w, weight)
        temp.next = self.adjlist[v-1].next
        self.adjlist[v-1].next = temp
        self.adjlist[w-1].indegree += 1

        self.ne += 1

    def __str__(self) -> str:
        output = ''

        for node in self.adjlist:
            output += f'[{node.vertex}]{{{node.indegree}}}'
            cur = node
            while cur.next is not None:
                cur = cur.next
                output += f' -->{cur.vertex}({cur.weight})'
            
            output += '\n'

        return output

    def aov(self) -> list:
        result = []
        queue: deque[AdjVNode] = deque([])
        for item in self.adjlist:
            if item.indegree == 0:
                queue.append(item)

        while queue:
            vertex = queue.popleft()
            result.append(vertex.vertex)
            ptr = vertex
            while ptr.next is not None:
                ptr = ptr.next
                self.adjlist[ptr.vertex-1].indegree -= 1
                if self.adjlist[ptr.vertex-1].indegree == 0:
                    queue.append(self.adjlist[ptr.vertex-1])            

        return result


class AoeNode:
    
    def __init__(self, vert: int, weight: W = INF) -> None:
        self.vertex = vert
        self.earliest = 0
        self.latest = 0

        self.weight = weight 
        self.next: Optional[AoeNode] = None


class AoEGraph:

    def __init__(self, num_vert: int) -> None:
        self.ajdlist: list[AoeNode] = [AoeNode(i) for i in range(num_vert)]
        self.nv = num_vert
        self.ne: int = 0

    def join(self, v: int, w: int, weight: int) -> None:
        temp = AoeNode(w, weight)
        temp.next = self.ajdlist[v].next
        self.ajdlist[v].next = temp 

    ...



def test_graph() -> None:
    lgraph = LGraph(15)
    edges_list = [
        (1, 3), (2, 3), (4, 5), (5, 6) ,(3, 7), (8, 9),
        (7, 10), (7, 11), (9, 11), (9, 10), (7, 12),
        (2, 13), (10, 14),(6, 15)
    ]
    for edge in edges_list:
        lgraph.join(*edge)
    
    print('# -- PRINT GRAPH -------------------------------------------------')
    print(lgraph)
    print(lgraph.aov())


def test_aoe() -> None:
    ...


def main() -> None:
    test_graph()

if __name__ == '__main__':
    main()