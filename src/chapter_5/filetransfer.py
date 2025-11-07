#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""You shoud implement it with **Union by rank** and **Path compression**."""


class DSU:

    def __init__(self, number) -> None:
        """Initialize an empty DSU."""
        # Item represented by index, data stores the parent index
        self.parent: list[int] = [-1] * number

    def find(self, item: int) -> int:
        """Find the set name (root) of the item."""
        # item is the index of the item itself
        while self.parent[item] != -1:
            item = self.parent[item]

        return item

    def union(self, item_x: int, item_y: int) -> None:
        """Union of two sets."""
        # Simply set the parent of the item_y by item_x
        # But it not check whether they are the same set
        self.parent[item_y] = item_x

def main():
    temp = int(input('Number of item: '))
    input_set = DSU(temp)

    while True:
        construct = input('-->').split(' ')
        if construct[0] == 'C':
            x = input_set.find(int(construct[1])-1)
            y = input_set.find(int(construct[2])-1)
            if x == y:
                print('Joint.')
            else:
                print('Disjoint!')

        elif construct[0] == 'I':
            x = input_set.find(int(construct[1])-1)
            y = input_set.find(int(construct[2])-1)
            if x != y:
                input_set.union(x, y)
        
        elif construct[0] == 'S':
            print(input_set.parent.count(-1))
            break
        else:
            continue

    return


if __name__ == '__main__':
    main()