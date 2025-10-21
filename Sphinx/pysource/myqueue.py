#!/usr/bin/env python
# -*- coding: UTF-8 -*-
""""""

from __future__ import annotations
from typing import Optional





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






        



            
