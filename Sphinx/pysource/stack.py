#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Optional


class SequentialStack:
    """Stack implemented with sequential list. """

    def __init__(self, MAXSIZE: int = 10) -> None:
        """Initialize an empty sequential stack.

        :param MAXSIZE: The max size of the sequential stack. Optional, defaults
                        to 10 if not provided.

        :var data: A list stores all of the data.
        :var top: The pointer to the top of the stack.
        """
        # Check the legality of MAXSIZE
        if MAXSIZE <= 1:
            raise ValueError("'MAXSIZE' must be positive.")

        # Define a variable for the max size of the sequential stack
        self.maxsize = MAXSIZE

        # Define a list stores the data
        self.data: list[Optional[int]]= [None] * self.maxsize

        # Define the pointer to the top of the stack
        self.top = -1

    def push(self, item: int) -> None:
        """Push the given item into the stack.
        
        :param item: Specify the item to be pushed.
        """ 
        # Check whether the stack is full
        if self.top == self.maxsize - 1:
            raise IndexError('stack is full')

        # Push the item and increase the top pointer
        self.top += 1
        self.data[self.top] = item

    def pop(self) -> int:
        """Pop the item from the top of the stack.
        
        :return: The item to be poped.
        """
        # Check whether the stack is empty
        if self.top == -1:
            raise IndexError('stack is empty.')
        
        # Stores the item to be poped
        item = self.data[self.top]

        # Check the itme type
        # Delete the item poped and decrease the top pointer
        if isinstance(item, int):
            self.data[self.top] = None
            self.top -= 1
            return item
        else:
            raise TypeError('item type is not int.')


class SequentialDualStack:
    """Dual stack implemented with sequential list."""

    def __init__(self, MAXSIZE: int = 10) -> None:
        """Initialize an empty sequential double stack.
        
        :param MAXSIZE: 
        :var data: A list stores all of the data.
        :var top_0: The pointer to the top of the stack 0.
        :var top_1: The pointer to the top of the stack 1.
        """
        # Check the legality of the MAXSIZE
        if MAXSIZE <=0:
            raise ValueError("'MAXSIZE' must be positive.")

        # Define a variable for the max size of the sequential double stack
        self.maxsize = MAXSIZE

        # Define a list stores the data
        self.data: list[Optional[int]] = [None] * self.maxsize
        
        # Define varialbes for the pointer to the stack top 
        self.top_0: int= -1
        self.top_1: int = self.maxsize

    def push(self, item: int, tag: int = 0) -> None:
        """Push the given item into the stack.
        
        :param item: Specify the item to be pushed
        :param tag: Indicate the stack into which the item will be pushed
        """
        # Check whether the stack if full
        if self.top_0 + 1 == self.top_1:
            raise IndexError('stack is full')
        
        # Push the item to the stack 0
        if tag == 0:
            self.top_0 += 1
            self.data[self.top_0] = item

        # Push the item to the stack 1
        else:
            self.top_1 -= 1
            self.data[self.top_1] = item

    def pop(self, tag: int = 0) -> int:
        """Pop the item from the stack top.
        
        :param tag: Indicate the stack into which the item will be poped
        """
        # Manipulate the stack 0
        if tag == 0: 

            # Check whether the stack 0 is empty
            if self.top_0 == -1:
                raise IndexError('stack 0 is empty')

            # Pop the item from the stack 0
            item = self.data[self.top_0]

            # Delete the item and decrease the top pointer of the stack 0 
            if isinstance(item, int):
                self.data[self.top_0] = None
                self.top_0 -= 1
                return item

            # Check the item type
            raise TypeError('item type is not int.')
            
        # Manipulate the stack 1
        else:

            # Check whether the stack 1 is empty
            if self.top_1 == self.maxsize:
                raise IndexError('stack 1 is empty')

            # Pop the item from the stack 0
            item = self.data[self.top_1]

            # Delete the item and decrease the top pointer of the stack 0
            if isinstance(item, int):
                self.data[self.top_1] = None
                self.top_1 +=1
                return item

            # The item type is not int
            raise TypeError('item type is not int.')


class Node:
    """Automic element of the :py:class:`LinkedStack` class."""

    def __init__(self, data: Optional[int] = None):
        """Initialize the node of the linked stack.
        
        :var data: Stores the data of the :py:class:`Node`. It is None only when
                   it is *Sentinel Node* or *Dummy Node*.

        :var next: The pointer to the next node 
        """ 
        # Define data
        self.data = data

        # Define pointer to the next node
        self.next: Optional[Node] = None


class LinkedStack:
    """Stack implemented with linked list."""

    def __init__(self) -> None:
        """Initialize an empty linked stack.
        
        :var head: The pointer to the sentinel node.
        """
        # pointer to the sentinel node
        self.head: Node = Node(None)

    def push(self, item: int) -> None:
        """Push the given item to the top of the linked stack.
        
        :var item: The specified item to be pushd.
        """
        # The node to be inserted into linked stack 
        s = Node(item)
        p = self.head

        # The process of the insertion
        s.next = p.next
        p.next = s

    def pop(self) -> int:
        """Pop the item from the top of the linked stack.
        
        :return: The item at the top of the linked stack.
        """
        # Check wether the linked stack is empty
        if self.head.next == None:
            raise IndexError('stack is empty')
        
        # The node stores the item to be poped
        p = self.head
        s = self.head.next
        item = s.data

        # Check the item type to be poped and delete the node s
        if isinstance(item, int):
            p.next = s.next
            return item
        
        # The item type is not int
        raise TypeError('item type is not int.')

        

        