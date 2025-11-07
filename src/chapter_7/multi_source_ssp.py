#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional
from collections import deque
from heapq import heapify, heappush, heappop
import weakref, copy

A = list[list[Union[int, float]]]
inf = float('inf')

class MGraph:

    def __init__(self, num_vert) -> None:
        self.adjmatrix: A = [[inf]*num_vert for _ in range(num_vert)]
        self.nv = num_vert
        self.ne = 0

    def connect(self, v: int ,w: int, weight: int) -> None:
        if v != w:
            self.adjmatrix[v-1][w-1] = weight
            self.adjmatrix[w-1][v-1] = weight

        else:
            raise ValueError('v must not equal w')

    def floyd(self) -> list:
        result = []
        # Define the D matrix
        D = copy.deepcopy(self.adjmatrix)
        for k in range(self.nv):
            for i in range(self.nv):
                for j in range(self.nv):
                    if i != j and D[i][j] > D[i][k] + D[k][j]:
                        D[i][j] = D[i][k] + D[k][j]

        result = [[max(D[l])] for l in range(self.nv)]

        return D

def main():
    nv, ne= 6, 11
    lgraph = MGraph(int(nv))

    data_list = [
        (3, 4, 70),
        (1, 2, 1),
        (5, 4, 50),
        (2, 6, 50),
        (5, 6, 60),
        (1, 3, 70),
        (4, 6, 60),
        (3, 6, 80),
        (5, 1, 100),
        (2, 4, 60),
        (5, 2, 80)
    ]

    for v, w, weight in data_list:
        lgraph.connect(int(v), int(w), int(weight))

    for line in lgraph.floyd(): 
        print(line)

if __name__ == '__main__':
    main()