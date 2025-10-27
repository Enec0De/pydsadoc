#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Optional

a = []

try:
    a[4] = 1
except IndexError:
    a.append(4)

print('a is: ', a)