#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class SequentialList:

    def __init__(self, size: int = 0) -> None:
        """Equivilent make empty list."""
        self.size = size
        self.data: list[object] = [None] * self.size

    def find_element(self, element: int) -> int:
        """Find an element in list"""
        for i in range(0, self.size):
            if element == self.data[i]:
                return i
        return -1

    def insert(self, index: int, element: int) -> None:
        """Insert"""
        if index < 0 or index > self.size:
            raise IndexError

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = element
        self.size += 1

    def delete(self, index: int) -> None:
        """Delete"""
        if index < 0 or index > self.size:
            raise IndexError

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        del self.data[self.size - 1]
        self.size -= 1

class Node:

    def __init__(self, data: object = None):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def make_empty(self):
        pass

    def find_kth(self):
        pass

    def find_element(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

    def lenth(self):
        pass