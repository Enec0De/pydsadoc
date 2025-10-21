#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Optional


class Node:
    
    def __init__(self, data: Optional[int]):

        self.data = data
        self.next: Optional[Node]= None


class LinkedStack:

    def __init__(self):

        self.head = None

    def push(self, element: int):

        s = Node(element)

        s.next = self.head
        self.head = s


    def pop(self):

        if self.head is not None:
            value = self.head.data
            self.head = self.head.next

        else:
            raise IndexError

        return value

    def __str__(self):

        s: str = ''

        while self.head is not None:
           s = s + ' ' + str(self.head.data) 
           self.head = self.head.next

        return s
