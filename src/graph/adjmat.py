#!/usr/bin/env python

from __future__ import annotations

__all__ = ['MGraph']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional
from collections import deque


class MGraph:

    def __init__(self, num_vert: int, /) -> None:
        ...
    
    def __str__(self, /) -> None:
        ...

    def bfs(self, /):
        ...
    
    def dfs(self, /):
        ...

    def floyd_warshall(self, /):
        ...
    
    def insert_edge(self, v: int, w: int, weight: int, /) -> None:
        ...

def main() -> None:
    data_list = [
        (3, 4, 70), (1, 2, 1), (5, 4, 50), (2, 6, 50),
        (5, 6, 60), (1, 3, 70), (4, 6, 60), (3, 6, 80),
        (5, 1, 100), (2, 4, 60), (5, 2, 80)
    ]
    
if __name__ == '__main__':
    main()