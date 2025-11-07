#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional
from collections import deque
from heapq import heapify, heappop, heappush
from math import isqrt

import copy
import weakref

class Node:

    def __init__(self, phone: str = '') -> None:
        self.phone = phone 
        self.count: int = 1
        self.next: Optional[Node] = None

class HashTable:

    def __init__(self, MAXSIZE: int = 15) -> None:
        """Build an empty hash table."""
        next_prime = self._next_prime(MAXSIZE)
        self.maxsize = next_prime
        self.buckets: list[Node] = [Node() for _ in range(next_prime)]

    def _hash(self, item: str) -> int:
        return hash(item) % self.maxsize
    
    def _next_prime(self, size: int) -> int:
        p = size

        while True:
            for i in range(isqrt(p), 1, -1):
                if p % i == 0 :
                    break

            # p is prime
            if i == 2:
                break
            # p is not prime
            else:
                p += 2

        return p

    def __str__(self) -> str:
        OUTPUT = 'Result: '
        MAXCOUNT: int = 0
        PHONENUM: str = ''
        P_COUNT: int = 0

        for node in self.buckets:
            ptr: Optional[Node] = node.next
            while ptr is not None:
                if ptr.count > MAXCOUNT:
                    MAXCOUNT = ptr.count
                    PHONENUM = ptr.phone
                    P_COUNT = 1
                elif ptr.count == MAXCOUNT:
                    P_COUNT += 1
                    if int(ptr.phone) < int(PHONENUM):
                        PHONENUM = ptr.phone
                ptr = ptr.next

        OUTPUT += f'Phone: {PHONENUM} MaxCount: {MAXCOUNT}'
        if P_COUNT > 1:
            OUTPUT += f'\nOther_Phone_Count: {P_COUNT}' 

        return OUTPUT
    
    def printer(self) -> None:
        output = ''
        i = 0

        for node in self.buckets:
            output += f'({i}) '
            p = node.next
            while p is not None:
                output += f'->[P: {p.phone}'
                output += f' C: {p.count}]'
                p = p.next
            output += '\n'
            i += 1

        print(output)

    def find(self, item: str) -> Optional[Node]:
        index = self._hash(item)

        # Find that node
        p = self.buckets[index].next
        while p is not None:
            if p.phone == item:
                break
            p = p.next

        return p

    def insert(self, item: str) -> None:
        p = self.find(item)
        index = self._hash(item)
        if not p:
            temp = Node(item)
            temp.next = self.buckets[index].next
            self.buckets[index].next = temp
        else:
            p.count += 1



def main() -> None:

    # N = int(input('Input N: '))
    N = int('4')

    input_num = [
        '13005711862 13588625832',
        '13505711862 13088625832',
        '13588625832 18087925832',
        '15005713862 13588625832'
    ]

    hash_table = HashTable()
    for i in range(N):
        # phone_num = input('-->').split(' ')
        phone_num = input_num[i].split(' ')

        # Insert
        for p in phone_num:
            hash_table.insert(p)


    hash_table.printer()
    print(hash_table)


if __name__ == '__main__':
    main()


