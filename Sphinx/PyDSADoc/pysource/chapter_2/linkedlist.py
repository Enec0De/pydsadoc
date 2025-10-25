#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Implement a linked linear list."""

from __future__ import annotations
from typing import Optional


class Node:
    """The aotomic element of the linked list."""

    def __init__(self, data: Optional[int] = None) -> None:
        """Initialized the node of the linked list.
        
        :var data: Stores the data of the node. It is None only when it is 
                   *Sentinel Node* or *Dummy Node*.

        :var next: Stores the point of the next node.
        """
        # Define data
        self.data = data

        # Define pointer to the next node
        self.next: Optional[Node] = None


class LinkedList:
    """Linear List implemented with linked list."""

    def __init__(self) -> None:
        """Initialize an empty linked list begin with a sentinel node.
        
        :var head: A pointer to the sentinel node of the linkd list.
        """
        # pointer to the sentinel node
        self.head: Node = Node(None)

    def len(self) -> int:
        """Calculate the length of the given node. 
        
        Time complexity is :math:`O(n)`.

        :return: Return the number of nodes int the linked list has, excluding 
                 the sentinel node.
        """
        # Define the variables for the length and the sentinel node
        length: int = 0
        ptr = self.head

        # Loop for counting the length
        while ptr.next is not None:
            ptr = ptr.next
            length += 1
        return length
            
    def index(self, index: int) -> int:
        """Find the value of the node at the given index.

        Time complexity is :math:`O(n)`.

        :param index: Specify the index of the node to be found.
        :return: The value of the target node.
        """
        # Index out of the left range of the list.
        if index < 0:
            raise IndexError('list index out of range.')
        # Define the varibales for the given index and the sentinel node
        i: int = -1
        ptr: Optional[Node] = self.head

        # Traverse the list to reach the node at the given index step by step
        while ptr.next is not None and i <= index - 1:
            ptr = ptr.next
            i += 1

        # Now we are at the target node
        if i == index: 
            value = ptr.data

            # Check the data type
            if isinstance(value, int):
                return value
            else:
                raise TypeError('data type is not int.')

        # The given index out of the right range of the list.
        else:
            raise IndexError('list index out of range.')

    def element(self, element: int, index: int = 0) -> int:
        """Find the index of the node that has the specifed element.

        Time complexity is :math:`O(n)`.

        :param element: Specify the element to be found.

        :param index: Specify the index from which you want to start finding the
                      node. Optional, defaults to 0 if not provided.

        :return: The index of the first encountered node will be returned.
        """
        # Define the variable for counting the index and the sentinel node
        i: int = -1
        ptr = self.head

        # Traverse to the node at the given index
        while ptr.next is not None and i <= index - 1:
            ptr = ptr.next
            i += 1
        
        # Index out of the right range of the list
        if i != index:
            raise IndexError('list index out of range')

        # The process of finding the node that has the given element
        while ptr.next is not None and ptr.data != element:
            ptr = ptr.next
            i += 1

        # Find the element in the linked list
        if ptr.data == element: 
            return i

        # The element is not found
        else:
            raise ValueError(f"'{element}' not found in the list.")
        
    def insert(self, element: int, index: int) -> None:
        """Insert the element into the linked list.
        
        Time complexity is :math:`O(n)`.

        :param element: The element to be insert into the list.

        :param index: The position to be insert at in the list. The element 
                      would be inserted in the last of linked list if the given
                      index out the right range of the list.
        """ 
        # Index out of the left range of the list
        if index < 0 : 
            raise IndexError('list index out of range.')

        # Initalize the node with the given element
        s = Node(element)

        # Define variables for counting the index and for the sentinel node
        i: int = -1
        ptr = self.head

        # Traverse to the node preceding the given index
        while ptr.next is not None and i <= index -2:
            ptr = ptr.next
            i += 1

        # The process of insertion
        s.next = ptr.next
        ptr.next = s


    def delete(self, index: int) -> None:
        """Delete the elemenet from the list.
        
        Time complexity is :math:`O(n)`.

        :param index: Specify the index at which the element is to be deleted.
        """
        # Index out of the left range of the list
        if index < 0: 
            raise IndexError('list index out of range')

        # Define variables for counting the index and for the sentinel node
        i: int = -1
        ptr = self.head

        # Traverse to the node preceding the given index
        while ptr.next is not None and i <= index - 2:
            ptr = ptr.next
            i += 1
        
        # The process of the deletion
        s = ptr.next
        if isinstance(s, Node):
            ptr.next = s.next

        # Index out of the right range of the list
        else:
            raise IndexError('list index out of range.')    


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
        p = self.head
        s = Node(item)

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

        # Check the item type to be poped and delete the node s
        item = s.data
        if isinstance(item, int):
            p.next = s.next
            return item
        
        # The item type is not int
        raise TypeError('item type is not int.')
    
    
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
            
