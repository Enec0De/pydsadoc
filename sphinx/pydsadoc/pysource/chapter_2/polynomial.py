#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""The Implementation of some operators for two polynomials in linked list."""

from __future__ import annotations
from typing import cast, Optional, Any


class PolyNode:
    """The atomic element of the linked list."""

    def __init__(self, coef: Optional[int] = None, expon: Optional[int] = None):
        """Initialize an empty node of the linked list

        :var coef: The coefficient of the polynomial. Note that there is no term
                   having a coef valued 0. 
        :var expon: The exponential of the polynomial.
        :var next: The pointer to the next node.
        """
        # Definition of the variables
        self.coef = coef
        self.expon = expon
        self.next: Optional[PolyNode] = None


class Polynomial:
    """A linked list stores the information of the polynomial."""

    def __init__(self, coef: Any, expon: Any) -> None:
        """Initialize an linked list that contains only one single node.

        A multi-terms polynomial can be created by adding some single 
        polynomials.
        
        :var head: The pointer directly to the data node of the linked list that
                   implements the polynomial. It's None when either of the 
                   parameters is not an int.
        """
        # Pointer to the sentinel node of the linked list
        if all(isinstance(item, int) for item in (coef, expon)) and coef != 0:
            self.head = PolyNode(coef, expon)
        else:
            self.head = None

    def __str__(self) -> str:
        """Implementation of the built-in function ``print()``.
        
        
        :return: The string object need to be printed.
        """
        # Define the string variable to store the data
        p_str = ''

        # Type annotations
        p_poly = cast(PolyNode, self.head)
        
        # Stores the coefficient and exponential of non-empty node
        while p_poly is not None:

            # Type annotations
            p_poly.coef = cast(int, p_poly.coef)
            p_poly.expon = cast(int, p_poly.expon)

            # Form the string like '+ax^b'
            if p_poly.coef == 0:
                pass

            elif p_poly.coef > 0 and p_poly.expon == 0:
                p_str += f'+{p_poly.coef}'

            elif p_poly.coef > 0 and p_poly.expon > 0:
                p_str += f'+{p_poly.coef}x^{p_poly.expon}'
            
            elif p_poly.coef > 0 and p_poly.expon < 0:
                p_str += f'+{p_poly.coef}x^({p_poly.expon})'

            elif p_poly.coef < 0 and p_poly.expon == 0:
                p_str += f'{p_poly.coef}'
                
            elif p_poly.coef < 0 and p_poly.expon > 0:
                p_str += f'{p_poly.coef}x^{p_poly.expon}'
                
            elif p_poly.coef < 0 and p_poly.expon < 0:
                p_str += f'{p_poly.coef}x^({p_poly.expon})'

            # Treaverse to the next node
            p_poly = p_poly.next

        # Return the final string 
        return p_str

    def __add__(self, polynomial: Polynomial) -> Polynomial:
        """Implementation of the addition (``+``) operators.
        
        :var polynomial: The polynomial to be added.
        """
        # Define the variables for two polynomials to be added, p_1, p_2
        p_1: Optional[PolyNode] = self.head
        p_2: Optional[PolyNode] = polynomial.head

        # Create the result polynomials with a sentinel node, s
        s: PolyNode = PolyNode(None, None)
        temp: PolyNode = s

        # Process until any of the polynomials is empty
        while p_1 is not None and p_2 is not None:

            # Type annotation
            p_1, p_2 = (cast(PolyNode, x) for x in (p_1, p_2))
            p_1.coef, p_1.expon = (cast(int, x) for x in (p_1.coef, p_1.expon))
            p_2.coef, p_2.expon = (cast(int, x) for x in (p_2.coef, p_2.expon))

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
                temp.next = PolyNode(p_1.coef, p_1.expon)
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

        # Delete the sentinel node and store the linked list as the Polynomial
        polynomial_result = Polynomial(None, None)
        polynomial_result.head = s.next
        return polynomial_result

    def __mul__(self, polynomial: Polynomial) -> Polynomial:
        """Implementation of the multiplication (``*``) operator.
        
        :var polynomial: The polynomial to be multiplied.
        """
        # Define the variables point to the polynomial to be manipulated
        p_1 = cast(PolyNode, self.head)

        # Define the polynomial to stores the result
        result = Polynomial(1, 0)

        
        # Traverse all of the p_1
        while p_1 is not None:

            # Begin from head of the polynomial of p_2
            p_2 = cast(PolyNode, polynomial.head)
            
            # Traverse all of the p_2
            while p_2 is not None:
                
                # Type annotations
                p_1.coef, p_1.expon = (
                    cast(int, x) for x in (p_1.coef, p_1.expon)
                )

                p_2.coef, p_2.expon = (
                    cast(int, x) for x in (p_2.coef, p_2.expon)
                )
                
                # Create a new term of polynomial to be multipled
                s = Polynomial(p_1.coef * p_2.coef, p_1.expon + p_2.expon)

                # Add the term to the result
                result += s

                # Traverse to the next node
                p_2 = p_2.next

            # Traverse to he next node
            p_1 = p_1.next
        
        # Return the fixed result polynomial
        return result + Polynomial(-1, 0)






                

        