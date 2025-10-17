#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Optional


class SequentialList:

    def __init__(self, maxsize: int = 10) -> None:
        """Make empty list."""
        # Define MAXSIZE
        self.size = maxsize
        
        # Define Data[MAXSIZE]
        self.data: list[Optional[int]] = [None] * self.size 

        # Define subscript, '-1' means empty
        self.last: int = -1

    def length(self) -> int:
        """Return length of the list."""
        return self.last + 1

    def find_kth(self, i: int) -> Optional[int]:
        """Return the data at index ``i`` in the list."""
        return self.data[i]

    def find_element(self, element: int) -> int:
        """Find the element in the list and return the index of it.

        Time complexity is O(n).
        """
        # Find the index of the element
        i: int = 0
        while i <= self.last and self.data[i] != element:
            i += 1

        # Not found
        if i > self.last: 
            return -1 

        # Return the index of the element.
        else: 
            return i

    def insert(self, i: int, element: int) -> None:
        """Insert the element into the list of the index ``i``.
        
        Time complexity is O(n).
        """
        # Is full
        if self.last + 1 == self.size: 
            raise OverflowError('The list is full.')

        # Illegal index
        if i < 0 or i > self.last + 1: 
            raise IndexError('Illegal index.')

        # Insert operation
        for j in range(self.last, i - 1, -1):
            self.data[j + 1] = self.data[j]
        self.data[i] = element
        self.last += 1

    def delete(self, i: int) -> None:
        """Delete the element from the list indexed ``i``. 
        Time complexity is O(n)."""
        # Illegal index
        if i < 0 or i > self.last:
            raise IndexError('Illegal index.')

        # Delete operation
        for j in range(i, self.last):
            self.data[j] = self.data[j + 1]
        self.data[self.last] = None
        self.last -= 1


class Node:

    def __init__(self, data: Optional[int] = None) -> None:
        """Linked list node."""
        # Define Data
        self.data = data

        # Define ptr of the next Node
        self.next: Optional[Node] = None


class LinkedList:

    def __init__(self) -> None:
        """Initialize linked list with a None node."""
        self.head: Node = Node(None)

    def _length(self, node: Node) -> int:
        """Return length of the `node', 
        
        Time complexity is O(n).
        """
        # Define the variables of the length and the pointer
        l: int = 0
        ptr = node

        # Loop for counting the length
        while ptr.next is not None:
            ptr = ptr.next
            l += 1
        return l
            
    def _find_kth_ptr(self, index: int) -> Node:
        """Retrun ptr of Node. 

        Time complexity is O(n).
        """
        # Define the varibales of the index and pointer
        i: int = 0
        ptr: Optional[Node] = self.head

        # Going to the index ``index`` or the end of the linked list
        # The pre is not the last None Node!
        while ptr.next is not None and i < index + 1:
            pre = ptr
            ptr = ptr.next
            i += 1

        # Judge the legality of the ptr
        if i == index + 1 : 
            return pre
        else:
            raise IndexError('Illegal index.')

    def _find_element_ptr(self, element: int) -> Node:
        """Return ptr of Node. 
        
        Time complexity is O(n).
        """
        # Define the variable of the first Node
        ptr: Optional[Node] = self.head

        # Match the data of the Node
        while ptr.next is not None and ptr.data != element:
            ptr = ptr.next

        # Fianl check
        if ptr.data == element: 
            return ptr
        else:
            raise ValueError(f"'{element}' not found in the list.")

    def length(self) -> int:
        """Return the length of the whole list."""
        return self._length(self.head)

    def find_kth(self, index: int) -> Optional[int]:
        """Return the element of the index `index'."""
        return self._find_kth_ptr(index).data

    def find_element(self, element: int) -> int:
        """Find the element in list."""
        ptr = self._find_element_ptr(element)
        return self._length(self.head) - self._length(ptr) 
        
    def insert(self, index: int, element: int) -> None:
        """Insert the element into the list.
        
        Time complexity is O(n).
        """ 
        # Illegal index
        if index < 0 or index > self.length(): 
            raise IndexError

        # Initalize the node with data ``element``
        s = Node(element)

        # Insert into the head node
        if index == 0:
            s.next = self.head
            self.head = s
            return 

        # Insert into other node
        p = self._find_kth_ptr(index - 1)
        s.next = p.next
        p.next = s


    def delete(self, index: int) -> None:
        """Delete the elemenet from the list indexed ``i``
        
        Time complexity is O().
        """
        # Illegal index
        if index < 0 or index > self.length() - 1: 
            raise IndexError('Illegal index.')

        # Define the variable of the target Node
        s = self._find_kth_ptr(index)

        # Delete the first Node
        if index == 0 and self.head.next is not None:
            self.head = self.head.next
        
        # Delete the other Node
        else:
            p = self._find_kth_ptr(index - 1)
            p.next = s.next
