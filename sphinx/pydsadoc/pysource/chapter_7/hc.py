#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Not implement."""

from __future__ import annotations
from typing import Union, Optional
from collections import deque
from heapq import heappop, heappush, heapify
import weakref


class HuffmanNode:

    def __init__(self, string: str, frequence: int) -> None:
        self.string = string
        self.frequence = frequence
        self.left: Optional[HuffmanNode]= None
        self.right: Optional[HuffmanNode] = None

    def __lt__(self, other: HuffmanNode) -> bool:
        return self.frequence < other.frequence

def build_huffman(data_input: str)-> HuffmanNode:

    heap: list[HuffmanNode] = []

    for item in set(data_input):
        fre = data_input.count(item) 
        heappush(heap, HuffmanNode(item, fre))
    length = len(heap)

    for _ in range(0, length-1):
        node_l = heappop(heap)
        node_r = heappop(heap)
        node_p = HuffmanNode('', node_l.frequence+node_r.frequence)
        node_p.left = node_l
        node_p.right = node_r
        heappush(heap, node_p)

    return heappop(heap)

def calculate_wpl(huffman) -> int:
    ...

def main():
    data_input = input('Inputh your string to encode: ')
    huffman = build_huffman(data_input)
    # wpl = calculate_wpl(huffman)
    # print(wpl)

if __name__ == "__main__":
    main()