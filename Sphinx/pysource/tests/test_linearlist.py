#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import unittest
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import linearlist

class TestLinearlist(unittest.TestCase):

    def setUp(self):
        # random.seed(40)
        self.list_length = random.randint(1,10)
        self.random_list = [
            random.randint(-100, 100) for _ in range(0, self.list_length)
        ]

        self.sqlist = linearlist.SequentialList()
        self.lllist = linearlist.LinkedList()
        self.insert_list(self.random_list, self.sqlist)
        self.insert_list(self.random_list, self.lllist)

    def insert_list(self, random_list, linearelist):
        for i in range(0, len(random_list)):
            linearelist.insert(0, random_list[i])

    def test_find_kth(self):
        ts = self.sqlist
        tl = self.lllist 
        for i in range(0, self.list_length):
            self.assertEqual(ts.find_kth(i), tl.find_kth(i))

    def test_find_element(self):
        r = random.randint(0, self.list_length - 1)
        fs = self.sqlist
        fl = self.lllist 
        self.assertEqual(
            fs.find_element(self.random_list[r]),
            fl.find_element(self.random_list[r])
        )

    def test_delete(self):
        s =  random.randint(0, self.list_length - 1)
        sqlist = linearlist.SequentialList()
        lllist = linearlist.LinkedList()
        self.insert_list(self.random_list, sqlist)
        self.insert_list(self.random_list, lllist)
        print(s)
        print(sqlist.length())
        print(lllist.length())
        sqlist.delete(s)
        lllist.delete(s) 
        for i in range(0, self.list_length - 1):
            self.assertEqual(
                sqlist.find_kth(i),
                lllist.find_kth(i) 
            )

if __name__ == '__main__':
    unittest.main()


