#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional
from collections import deque
from heapq import heapify, heappop, heappush
import weakref
import copy

D = Union[list[dict[str, Union[None, bool, int]]]]

class HashTable:

    def __init__(self, tablesize: int = 15) -> None:
        # The prime of the form 4k+3 
        self.tablesize: int = tablesize
        # None means Empty
        # Non-None and False means Legitimate
        # Non-None and True means Delete
        self.head: D = [{'key': None, 'tombstone': False } for _ in range(tablesize)]

    def _hash(self, item) -> int:
        return hash(item) % self.tablesize

    def find(self, key) -> int:
        index = self._hash(key)
        collision_num = 2
        while (self.head[index]['tombstone'] 
               or self.head[index]['key'] != key):
            quadratic_probing = (-1)**collision_num * (collision_num//2)**2
            index = (index+quadratic_probing) % self.tablesize
            collision_num += 1
            if collision_num > 999:
                break

        if self.head[index]['key'] != key or self.head[index]['tombstone']:
            return -1
        else:
            return index

    def insert(self, item: int) -> None:
        index = self._hash(item)
        collision_num = 2
        while (not self.head[index]['tombstone'] 
               and self.head[index]['key'] is not None):
            quadratic_probing = (-1)**collision_num * (collision_num//2)**2
            index = (index+quadratic_probing) % self.tablesize
            collision_num += 1
        
        self.head[index]['key'] = item
        self.head[index]['tombstone'] = False 

    def delete(self, item: int) -> None:
        index = self._hash(item)
        collision_num = 2
        while self.head[index]['key'] != item:
            quadratic_probing = (-1)**collision_num * (collision_num//2)**2
            index = (index+quadratic_probing) % self.tablesize
            collision_num += 1
        
        self.head[index]['tombstone'] = True


def main() -> None:
    # -- Test Insert ----------------------------------------------------------
    arr = [61, 7, 37, 6 ,329 ,4 ,8 ,5 ,1 ,-8 ,9 ,2, 0]
    hash_table = HashTable()
    for item in arr:
        hash_table.insert(item)

    # -- Print All ------------------------------------------------------------
    i = 0
    for d in hash_table.head:
        print(f'[{i}]: ', end='')
        print(d)
        i += 1

    # -- Test Find ------------------------------------------------------------
    index = []
    for item in arr:
        index.append(hash_table.find(item))
    print(arr)
    print(index)

    # -- Test Delete ----------------------------------------------------------
    delete_table = [329, -8, 9, 2]
    for delete in delete_table:
        hash_table.delete(delete)

    # -- Print Again ----------------------------------------------------------
    i = 0
    for d in hash_table.head:
        print(f'[{i}]: ', end='')
        print(d)
        i += 1

    # -- Find Again -----------------------------------------------------------
    result = []
    for item in delete_table:
        result.append(hash_table.find(item))
    print(result)

    # -- Print Again ----------------------------------------------------------
    hash_table.insert(329)
    print(hash_table.find(329))
    i = 0
    for d in hash_table.head:
        print(f'[{i}]: ', end='')
        print(d)
        i += 1

if __name__ == '__main__':
    main()