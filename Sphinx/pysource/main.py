#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import polynomial


def poly_input():
    # Imput and initialize polynomail
    s = input().split(sep=' ') 
    s_poly = polynomial.Polynomial(None, None)
    it = iter(s)

    # Add the polynomial
    for coef, expon in zip(*[it]*2):
        s_poly += polynomial.Polynomial(int(coef), int(expon))
    
    # Print polynomial
    print(s_poly)


if __name__ == '__main__':
    poly_input()