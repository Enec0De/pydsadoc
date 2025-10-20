#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import maxsubseqsum


class TestMaxsubseqsum(unittest.TestCase):

    def setUp(self):
        self.normal_arr1 = [4, -3, 5, -2, -1, 2, 6, -2]
        self.normal_arr2 = [-2, 11, -4, 13, -5, -2]
        self.negetive_arr = [-1, -3, -7, -4]
        self.positive_arr = [1, 2, 3, 4]

    def test_bfe(self):
        self.specific_function(maxsubseqsum.brute_force_enumeration)
        
    def test_oe(self):
        self.specific_function(maxsubseqsum.optimized_enumeration)

    def test_dac(self):
        self.specific_function(maxsubseqsum.divide_and_conquer)
        
    def test_dp(self):
        self.specific_function(maxsubseqsum.dynamic_programming)

    def specific_function(self, func):
        self.assertEqual(func(self.normal_arr1), 11)
        self.assertEqual(func(self.normal_arr2), 20)
        self.assertEqual(func(self.negetive_arr), -1)
        self.assertEqual(func(self.positive_arr), 10)

    
if __name__ == '__main__':
    unittest.main()