#!/usr/bin/env python

from __future__ import annotations

__all__ = ['shell_sort']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional

# Define ElementType
ElementType = Union[int]


# Generate the one item of the sedgewick sequence.
def _sedgewick(n: int) -> int:
    # Check the input data n.
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be an non-negative integer.')

    # Return the item of the sequence.
    if n%2:
        return 9*(2<<n) - 9*(2<<(n//2)) + 1
    else:
        return 8*(2<<n) - 6*(2<<((n+1)//2)) + 1 


# Generate the full sedgewick sequence.
def _sedgewick_sequence(length: int) -> list[int]:
    # The sedgewick sequence perfixed with element 1.
    sedgewick_sequence: list[int] = [1]

    # Add the rest element into the sedgewick sequence.
    i = 0
    while (item := _sedgewick(i)) < length:
        sedgewick_sequence.append(item)
        i += 1

    # Reverse the sequence in place.
    sedgewick_sequence.reverse()
    return sedgewick_sequence


def shell_sort(arr: list[ElementType]) -> None:
    """The Shell Sort Algorithm.  
    
    Time complexity is between :math:`O(n^{1.25})` and :math:`O(n^{1.5})`,
    depending on the chosen gap sequence.  It is an optimization of Insertion
    Sort, which is **not stable**.
    """
    length = len(arr)
    gap_sequence = _sedgewick_sequence(length)
    for gap in gap_sequence:
        
        # Insertion sort.
        for i in range(gap, length):
            temp = arr[i]
            j = gap
            while i - j >= 0 and arr[i-j] > temp:
                arr[i-j+gap] = arr[i-j]
                j += gap
            else:
                arr[i-j+gap] = temp
    

def main() -> None:
    # Create random array.
    arr = [random.randint(-9,99) for _ in range(random.randint(1,10))]
    print(arr)

    # Shell sort.
    shell_sort(arr)
    print(arr)

    # Assertion test.
    for i in range(len(arr)-1):
        assert arr[i] <= arr[i+1]


if __name__ == '__main__':
    main()
