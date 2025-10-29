#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Basic module
import unittest

# The module to manipulate the search path
import sys
from pathlib import Path

# Insert path in which the module locates 
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Other necessary module
import random
import linearlist


class TestLinearlist(unittest.TestCase):

    def setUp(self):
        # Generate a random list length
        # random.seed(40)
        self.list_len = random.randint(1,10)

        # Generate a random list
        self.random_list = [
            random.randint(-100, 100) for _ in range(0, self.list_len)
        ]

        # Initialize the sequential list
        self.sq = linearlist.SequentialList()
        self.initialize_list(self.sq)

        # Initialize the linked list
        self.ll = linearlist.LinkedList()
        self.initialize_list(self.ll)


    def initialize_list(self,list):
        # Insert the element one by one
        for i in range(0, self.list_len):
            list.insert(self.random_list[i], i)

    def test_index_and_insert(self):
        # Depending the function initialize_list
        # The element in the two lists should be the same
        for i in range(0, self.list_len):
            self.assertEqual(self.sq.index(i), self.ll.index(i))

    def test_len_and_element(self):
        # Take an element from the random list
        t = random.choice(self.random_list)

        # Check the length of the two lists
        self.assertEqual(self.sq.len(),self.ll.len())

        # Check the index returend by the element method
        self.assertEqual(self.sq.element(t), self.ll.element(t))

    def test_index_and_delete(self):
        # Take the random index from the random list. Note that the index of the
        # random list should be in range from 0 to list_len - 1.
        r = random.randint(0, self.list_len - 1)

        # The element in the two lists are now should be the same
        for i in range(0, self.list_len - 1):
            self.assertEqual(self.sq.index(i), self.ll.index(i))


# Main entry point
if __name__ == '__main__':
    unittest.main()


