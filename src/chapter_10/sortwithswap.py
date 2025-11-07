#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional

def main() -> None:
    arr = [3, 5, 7, 2, 6, 4, 9, 0, 8, 1]
    t = []
    for i in range(len(arr)):
        t[arr[i]] = i

if __name__ == '__main__':
    main()