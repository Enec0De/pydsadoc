#!/usr/bin/env python

import pytest
from pydsadoc import LinkedList


class TestLinkedList:

    @pytest.fixture(autouse=True)
    def initialize(self, randomdata: tuple[int, list[int]]) -> None:
        self.seed, self.array = randomdata
        self.linked: LinkedList[int] = LinkedList()

        for item in self.array:
            self.linked.append(item)

    def test_append(self) -> None:
        for i in range(len(self.array)):
            assert self.array[i] == self.linked[i], f"{self.seed}"

    def test_index(self) -> None:
        for item in set(self.array):
            assert self.array.index(item) == self.linked.index(item), f"{self.seed}"

    def test_pop(self) -> None:
        import random

        index = random.randint(0, len(self.array) - 1)
        assert (
            self.array.pop(index) == self.linked.pop(index).obj
        ), f"{self.seed}, pop({index})"

    def test_insert(self) -> None:
        import random
        import sys

        value = random.randint(-sys.maxsize, sys.maxsize)
        index = random.randint(0, len(self.array) - 1)
        self.array.insert(index, value)
        self.linked.insert(index, value)
        for i in range(len(self.array)):
            assert (
                self.array[i] == self.linked[i]
            ), f"{self.seed}, insert({index}, {value})"

    def test_remove(self) -> None:
        import random

        value = random.choice(self.array)
        self.array.remove(value)
        self.linked.remove(value)
        for i in range(len(self.array)):
            assert self.array[i] == self.linked[i], f"{self.seed}, remove({value})"
