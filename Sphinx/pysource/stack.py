#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""""""

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





class Node:
    """The automic element of the :py:class:`LinkedStack`."""

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




        

        