#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import maxsubseqsum

class TestMaxsubseqsum(unittest.TestCase):

    def test_kadane(self):
        self.assertEqual(maxsubseqsum.kadane([-2, 11, -4, 13, -5, -2]), 20)
        self.assertEqual(maxsubseqsum.kadane([-1, -3, -7, -4]), -1)
    
if __name__ == '__main__':
    unittest.main()