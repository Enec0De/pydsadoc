#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""There are two ways to stroe a linear list: sequentially and linkedly."""

from __future__ import annotations
from typing import Optional


class SequentialList:
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
            
