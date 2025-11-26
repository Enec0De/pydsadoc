#!/urs/bin/env python

from __future__ import annotations

__all__ = ['tim_sort']
__version__ = '0.1'
__author__ = 'Aina'

import random
from typing import Union, Optional

# Define ElementType
ElementType = Union[int]


def tim_sort(arr: list[int]) -> None:
    """Sort a list of numbers in ascending order(TBD)."""