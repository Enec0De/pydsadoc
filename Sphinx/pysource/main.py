#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import maxsubseqsum

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(maxsubseqsum.kadane(arr))