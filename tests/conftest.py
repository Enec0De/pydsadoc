#!/usr/bin/env python

import sys
from collections.abc import Callable
from typing import Optional

import pytest


def _random_list(
    seed: Optional[int] = None, length: Optional[int] = None
) -> tuple[int, list[int]]:
    """Retrun the tuple (seed, array).

    The length of the array is the given argument length.  The array is
    generated with the random seed.  If neither the seed nor the lenght
    is given (or is None), the seed and length default to random values.
    """
    import random

    seed = random.randint(0, sys.maxsize) if not seed else seed
    length = random.randint(0, 10000) if not length else length

    random.seed(seed)
    array = [random.randint(-sys.maxsize, sys.maxsize) for _ in range(length)]

    return seed, array


@pytest.fixture
def randlist() -> Callable[[int, int], tuple[int, list[int]]]:
    return _random_list
