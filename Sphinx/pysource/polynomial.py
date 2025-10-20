#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""Implementation of the plus two polynomial."""

from __future__ import annotations
from typing import cast, Optional


class PolyNode:
    """The atomic element of the linked list."""

    def __init__(self, coef: Optional[int] = None, expon: Optional[int] = None):
        """Initialize an empty node of the linked list

        :var coef: The coefficient of the polynomial.
        :var expon: The exponential of the polynomial.
        :var next: The pointer to the next node.
        """
        # Definition of the variables
        self.coef = coef
        self.expon = expon
        self.next: Optional[PolyNode] = None


class Polynomial:
    """A linked list stores the coefficent and exponential of a polynomial."""

    def __init__(self, item: Optional[tuple[int, int]] = None) -> None:
        """Initialize an empty linked list.
        
        :var head: The pointer to the sentinel node of linked list.
        """
        # Pointer to the sentinel node of the linked list
        if isinstance(item, tuple):
            self.head = PolyNode(*item)
        else:
            self.head = None

    def __add__(self, polynomial: Polynomial) -> Polynomial:
        # Define the variables for two polynomials to be added, p_1, p_2
        p_1: Optional[PolyNode] = self.head
        p_2: Optional[PolyNode] = polynomial.head

        # Create the result polynomials with a sentinel node, s
        s: PolyNode = PolyNode(None, None)
        temp: PolyNode = s

        # Process until any of the polynomials is empty
        while p_1 is not None and p_2 is not None:

            # Type annotation
            p_1, p_2 = cast(PolyNode, p_1), cast(PolyNode, p_2)
            p_1.expon, p_2.expon = cast(int, p_1.expon), cast(int, p_2.expon)
            p_1.coef, p_2.coef = cast(int, p_1.coef), cast(int, p_2.coef)

            if p_1.expon == p_2.expon:

                # Insert the new node to the end of the s
                if p_1.coef + p_2.coef != 0:
                    temp.next = PolyNode(p_1.coef + p_2.coef, p_1.expon)
                    temp = temp.next
                    
                # Treaverse to the next node
                p_1 = p_1.next
                p_2 = p_2.next

            elif p_1.expon < p_2.expon:

                # Insert the p_2 node to the end of the s
                temp.next = PolyNode(p_2.coef, p_2.expon)
                temp = temp.next

                # Treaverse to the next node
                p_2 = p_2.next
                
            elif p_1.expon > p_2.expon:

                # Insert the p_1 node to the end of the s
                temp.next = PolyNode(p_1.coef, p_2.expon)
                temp = temp.next

                # Treaverse to the next node
                p_1 = p_1.next

        while p_1 is not None:
            # Insert the rest of the node in the p_1 into the s
            temp.next = PolyNode(p_1.coef, p_1.expon)
            temp = temp.next
            p_1 = p_1.next

        while p_2 is not None:
            # Insert the rest of the node in the p_2 into the s
            temp.next = PolyNode(p_2.coef, p_2.expon)
            temp = temp.next
            p_2 = p_2.next

        # Delete the sentinel node
        polynomial_result = Polynomial(None)
        polynomial_result.head = s.next
        return polynomial_result

                

        
        




        ...


   