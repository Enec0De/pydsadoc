#!/usr/bin/env
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional


Position = Union[int]
NotFound = 1

def build_match(pattern: str, match: list[int]) -> None:
    len_p = len(pattern)
    for j in range(1, len_p):
        last = match[j-1]

        while last >= 0 and pattern[last+1] != pattern[j]:
            last = match[last]

        if pattern[last+1] == pattern[j]:
            match[j] = last + 1
        else:
            match[j] = -1

def kmp(string: str, pattern: str) -> Position:
    len_s = len(string)
    len_p = len(pattern)
    if len_s < len_p:
        return NotFound
    s = 0
    p = 0
    match = [-1] * len_p
    build_match(pattern, match)
    print(match)
    while s < len_s and p < len_p:
        if string[s] == pattern[p]:
            s, p = s+1, p+1
        elif p > 0:
            p = match[p-1] + 1
        else:
            s += 1

    if p == len_p:
        retval = s - len_p
    else:
        retval = NotFound
    return retval


    ...

def main() -> None:
    string = 'This is a simple example.'
    pattern = 'simple'
    p = kmp(string, pattern)
    if p == NotFound:
        print('Not Fount.')
    else:
        print(f'{string[p:]}')

if __name__ == '__main__':
    main()