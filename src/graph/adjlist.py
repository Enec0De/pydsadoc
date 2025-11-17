#!/usr/bin/env python

from __future__ import annotations

__all__ = ['GNode', 'LGraph']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional
from collections import deque
from functools import total_ordering


@total_ordering
class GNode:

    def __init__(self, /) -> None:
        ...
    
    def __eq__(self, other: GNode, /) -> bool:
        ...

    def __lt__(self, other: GNode, /) -> bool:
        ...

class LGraph:
    ...

    def __init__(self, /) -> None:
        ...
    
    def bfs(self, /):
        ...

    def dfs(self, /):
        ...
    
    def dijkstra(self, /):
        ...
    
    def insert_edge(self, /):
        ...
