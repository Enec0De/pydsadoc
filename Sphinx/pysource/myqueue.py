#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""A linear list follows the First-In-First-Out (FIFO) principle."""

from __future__ import annotations
from typing import Optional


class SequentialQueue:
    """Queue implemented with sequential storage."""

    def __init__(self, MAXSIZE: int = 10) -> None:
        """Initialize an empty queue.
        
        :param MAXSIZE: The max size of the queue.
        :var data: A list stroes all of the data.
        :var fromt: The pointer to the front of the queue.
        :var rear: The pointer to the rear of the queue.
        """
        # Define the max size of the queue
        self.maxsize = MAXSIZE

        # Define the list stores the data
        self.data: list[Optional[int]] = [None] * self.maxsize

        # Define the pointers
        self.front = self.maxsize - 1
        self.rear = self.maxsize - 1

    def add(self, item: int) -> None:
        """Add the specifed item into the queue.

        :param item: The item to be added into queue.
        """
        # Check whether the queue is full
        if (self.rear + 1) % self.maxsize == self.front:
            raise IndexError('queue is full')
        
        # The process of addition
        self.rear = (self.rear + 1) % self.maxsize
        self.data[self.rear] = item

    def delete(self) -> int:
        """Delete the item from the queue.
        
        :return: The item to be deleted from the queue.
        """
        # Check whether the queue is empty
        if self.front == self.rear:
            raise IndexError('queue is empty.')
        
        # The process of deletion
        self.front = (self.front + 1) % self.maxsize
        item = self.data[self.front] 

        # Check the value type
        if isinstance(item, int):
            return item
        else:
            raise TypeError('item type is not int.')


class Node:
    """Atomic element of the :py:class:`LinkedQueue`."""
    
    def __init__(self, data: Optional[int] = None):
        """Initialize a node of the linked queue.

        :var data: Stores the data of the node.
        :var next: Pointer to the next node.
        """
        # Define the variable for storing the data
        self.data = data

        # Define the pointer to the next node
        self.next: Optional[Node] = None


class LinkedQueue:
    """Queue implemented with linked list."""

    def __init__(self) -> None:
        """Initialize an empty queue.
        
        :var front: Pointer to the front of the queue.
        :var rear: Pointer to the rear of the queue.
        """
        # Define the variables for pointers to the front and the rear.
        self.front: Optional[Node] = None
        self.rear: Optional[Node] = None

    def add(self, item: int) -> None:
        """Add the given item to the queue.
        
        :param item: The item to be added.
        """
        # Initialize the node to be added
        s = Node(item)

        # The process of addition
        if self.rear == None:
            self.front = self.rear = s
        else:
            self.rear.next = s
            self.rear = s


    def delete(self) -> int:
        """Delete the item from the queue.
        
        :return: The value to be deleted from the queue.
        """
        # Check whether the queue is empty
        if self.front == None:
            raise IndexError('queue is empty.')

        # Store the value of the item to be deleted
        value = self.front.data
        
        # The process of deletion
        if self.front is self.rear:
            self.front = self.rear = None
        else: 
            self.front = self.front.next
        
        # Check the value type
        if isinstance(value, int):
            return value
        else:
            raise TypeError('value type is not int.')
            



        



            
