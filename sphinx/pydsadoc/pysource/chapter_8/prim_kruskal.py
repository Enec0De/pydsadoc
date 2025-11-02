#/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional
from collections import deque
from heapq import heapify, heappush, heappop
import weakref
import copy


INF = float('inf')
W = Union[int, float]

class UnionFind:
     
    def __init__(self, num_item) -> None:
        self.parent = [-1] * num_item

    def find(self, x: int) -> int:
        """Path compression."""
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x: int, y: int) -> None:
        """Union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.parent[root_x] < self.parent[root_y]:
            self.parent[root_x] += self.parent[root_y]
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] += self.parent[root_x]
            self.parent[root_x] = root_y
    
    def __str__(self) -> str:
        output = ''

        for i in range(len(self.parent)):
            output += f'node:[{i}] -> parent: {self.parent[i]}\n' 

        return output

class MinHeap:

    def __init__(self, item_list: Optional[list[int]] = None) -> None:
        """Initialize an minimum heap."""
        if item_list is None:
            self.heap = []
        else:
            self.heap = item_list

        self.capacity = len(self.heap)
        self._heapify()
    
    def push(self, item: int) -> None:
        self.heap.append(item)
        child = self.capacity
        self.capacity += 1

        while child > 0:
            parent = (child-1) // 2
            if item < self.heap[parent]: 
                self.heap[child] = self.heap[parent]
                child = parent
            else:
                break

        self.heap[child] = item

    def pop(self) -> int:
        retval = self.heap[0]
        self.capacity -= 1
        temp = self.heap[self.capacity]
        parent = 0
        child = 1
        while child <= self.capacity:
            parent = (child-1) // 2
            if child != self.capacity:
                if self.heap[child] > self.heap[child+1]:
                    child += 1

            if temp > self.heap[child]:
                self.heap[parent] = self.heap[child]
                child = 2*child + 1
            else:
                break

        self.heap[parent] = temp 

        return retval
        
    
    def _heapify(self) -> None:
        last_index = self.capacity - 1
        cur = (last_index-1) // 2
        while cur >= 0:

            child = 2*cur + 1
            while child <= last_index:
                parent = (child-1) // 2
                if child != last_index:
                    if self.heap[child] > self.heap[child+1]:
                        child += 1
                    
                if self.heap[parent] > self.heap[child]:
                    temp = self.heap[parent]
                    self.heap[parent] = self.heap[child]
                    self.heap[child] = temp
                    child = 2*child + 1

                else:
                    break

            cur -= 1

    def __str__(self) -> str:
        output = ''

        for i in range(self.capacity):
            output += f' [{self.heap[i]}] '
            if (i+1).bit_length() != (i+2).bit_length():
                output += '\n'

        return output

class Edge:
    """For kruskal."""

    def __init__(self, v: int, w: int, weight: W) -> None:
        self.v = v
        self.w = w
        self.weight = weight

    def __lt__(self, other: Edge) -> bool:
        return self.weight < other.weight


class AdjVNode:

    def __init__(self, vertex: int, weight: W = INF) -> None:
        self.vertex = vertex
        self.weight = weight
        self.next: Optional[AdjVNode] = None

    def __lt__(self, other: AdjVNode) -> bool:
        """Implementation of operation ``<``."""
        return self.weight < other.weight


class LGraph:
    """Adjacency list Graph."""

    def __init__(self, num_vertex: int) -> None:
        self.adjlist: list[AdjVNode] = [AdjVNode(i+1) for i in range(num_vertex)]
        self.nv = num_vertex
        self.ne: int = 0

    def join(self, v: int, w: int, weight: W = INF) -> None:
        temp_w = AdjVNode(w, weight)
        temp_w.next = self.adjlist[v-1].next
        self.adjlist[v-1].next = temp_w

        temp_v = AdjVNode(v, weight)
        temp_v.next = self.adjlist[w-1].next
        self.adjlist[w-1].next = temp_v

        self.ne += 1

    def __str__(self) -> str:
        output = ''
        for node in self.adjlist:
            current = node
            output += f'[{current.vertex}]'
            while current.next is not None:
                current = current.next
                output += f' ->{current.vertex}({current.weight})'
            output += '\n'

        return output

    def prim(self) -> list: 
        # The MST of the current LGraph.
        mst = [-1] * self.nv
        
        minheap = [self.adjlist[i] for i in range(self.nv)]
        minheap[0].weight = 0
        heapify(minheap)

        while minheap:
            # Add v into the mst
            v = heappop(minheap)
            print(f'v.vertex: {v.vertex} v.weight: {v.weight}')
            if v.weight == INF:
                raise IndexError('disjoint graph')
            # Retrieve the neighbor
            w = v
            while w.next is not None:
                w = w.next
                if (self.adjlist[w.vertex-1].weight > w.weight
                    and self.adjlist[w.vertex-1] in minheap):
                    # Updata minheap
                    self.adjlist[w.vertex-1].weight = w.weight
                    mst[w.vertex-1] = v.vertex

            heapify(minheap)

        # Reset the weight of node
        for node in self.adjlist:
            node.weight = INF

        return mst
    
    def kruskal(self): 
        # Select the smallest edge
        mst = [] 
        heap = []
        dsu = UnionFind(self.nv+1)

        for node in self.adjlist:
            cur = node
            while cur.next is not None:
                cur = cur.next
                if node.vertex < cur.vertex:
                    heap.append(Edge(node.vertex, cur.vertex, cur.weight))

        heapify(heap)
        while len(mst) < self.nv - 1 and heap:
            edge = heappop(heap)
            if dsu.find(edge.v) != dsu.find(edge.w):
                mst.append(edge)
                dsu.union(edge.v, edge.w)
        
        if len(mst) != self.nv - 1:
            raise IndexError('no such mst')

        for item in mst:
            print(f'v: {item.v} w: {item.w}, weight: {item.weight}')



def test_union_find() -> None:
    dsu = UnionFind(7)
    dsu_union = [
        (2, 4), (2, 5), (2, 3),
        (6, 1), (6, 0)
    ]

    for item in dsu_union:
        dsu.union(*item)

    print('# -- PRINT THE DSU -----------------------------------------------')
    print(dsu)
    

def test_graph() -> None:
    # Input data list: (v, w, weight)
    input_edges = [
        (1, 2, 2), (1, 4, 1), (1, 3, 4),
        (2, 4, 3), (2, 5, 10),
        (3, 4, 2), (3, 6, 5),
        (4, 5, 7), (4, 6, 8), (4, 7, 4),
        (5, 7, 6), 
        (6, 7, 1)
    ]
    graph = LGraph(7)
    for edge in input_edges:
        graph.join(*edge)

    print('# -- PRINT THE GRAPH ---------------------------------------------')
    print(graph)
    print(graph.prim())
    graph.kruskal()


def test_heap() -> None:
    item_list = [79, 66, 43, 83, 30, 87, 38, 55, 91, 72, 49, 9]
    minheap = MinHeap(item_list)
    heap_insert = MinHeap()
    for item in item_list:
        heap_insert.push(item)
    print('# -- PRINT THE HEAP ----------------------------------------------')
    print(minheap)
    print(heap_insert)
    for _ in range(len(item_list)):
        print(minheap.pop(), end=' ')
    print()
    for _ in range(len(item_list)):
        print(heap_insert.pop(), end=' ')
    print()

def main() -> None:
    # test_union_find()
    test_graph()
    # test_heap()

    
if __name__ == '__main__':
    main()
