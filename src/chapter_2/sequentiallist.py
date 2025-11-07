#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Implement a linear list sequentially."""

from __future__ import annotations
from typing import Optional


class SeqList:
    """Linear list implemented with sequential storage"""

    def __init__(self, MAXSIZE: int = 10) -> None:
        """Initialize an empty sequential list.

        :param MAXSIZE: Determines the max size of the squential list. Optional,
                        defaults to 10 if not provided.
        
        :var data: A list stores all of the data.
        :var last: The position of the last value in the list.
        """
        # Define MAXSIZE
        self._size = MAXSIZE
        
        # Define Data[MAXSIZE]
        self.data: list[Optional[int]] = [None] * self._size 

        # Define subscript, '-1' means empty
        self.last: int = -1

    def len(self) -> int:
        """Calculate the length of the list.
        
        Time complexity is :math:`O(1)`.

        :return: Return the amount of the elements within the list.
        """
        return self.last + 1

    def index(self, index: int) -> int:
        """Find the first encountered element by its index.
        
        Time complexity is :math:`O(1)`.

        :param index: The specified index of the target element.
        :return: The elment of the given index.
        """
        # Check the legality of the index
        if 0 <= index < self.len():
            value = self.data[index]

            # Check the value type
            if isinstance(value, int):
                return value
            else:
                raise TypeError('data type is not int.')
        
        else:
            raise IndexError('list index out of range.')

    def element(self, element: int, start_index: int = 0) -> int:
        """Find the index of the specified element encountered first time.

        Time complexity is :math:`O(n)`.

        :param element: The specified element you want to find.

        :param start_index: The specified index from which you want to start 
                            finding the element. Optional, defaults to 0 if not
                            provided.

        :return: The index of the given element. If the return value is -1 ,it 
                 means the given element was not found.
        """
        # Begin the process of finding the index of the element within the list
        i = start_index
        while i <= self.last and self.data[i] != element:
            i += 1

        # Not found, return -1
        if i > self.last: 
            return -1 

        # Find it and return the index of the element
        else: 
            return i

    def insert(self, element: int, index: int) -> None:
        """Insert the specified element into the list of the specified index.
        
        Time complexity is :math:`O(n)`.
        
        :param element: Specify the element to be inserted.
        :param index: Specify the index to be inserted.
        """
        # Judge whether the list is full
        if self.last + 1 == self._size: 
            raise IndexError('The list is full.')

        # Check the legality of the index
        if index < 0 or index > self.last + 1: 
            raise IndexError('list index out of range.')

        # Shift the elements backward
        for j in range(self.last, index - 1, -1):
            self.data[j + 1] = self.data[j]
            
        # The process of insertion
        self.data[index] = element
        self.last += 1

    def delete(self, index: int) -> None:
        """Delete the element from the list . 
        
        Time complexity is :math:`O(n)`.

        :param index: Specify the index to be delete.
        """
        # Check the legality of the index
        if index < 0 or index > self.last:
            raise IndexError('list index out of range.')

        # Shift the element forward
        for j in range(index, self.last):
            self.data[j] = self.data[j + 1]

        # Begin the process of deletion
        self.data[self.last] = None
        self.last -= 1


class SeqDualStack:
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


class SeqQueue:
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
