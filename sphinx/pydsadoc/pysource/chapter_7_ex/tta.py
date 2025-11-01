#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import annotations
from typing import Union, Optional
from collections import deque
import weakref

def traversal(pre_retrieve: list[int], 
               in_retrieve: list[int]) -> list:
    """For the *pre_list* and *in_list*, populate the empty list *post_list*."""
    # Give an empty list for post_retrieve and the index of the last element 
    post_retrieve: list[Optional[int]] = [None] * len(pre_retrieve)
    last_index =  len(post_retrieve) - 1

    # Empty tree
    if last_index < 0:
        return post_retrieve

    # The root node and its index in the in_pretrieve
    root = pre_retrieve[0]
    root_index = in_retrieve.index(root)

    # The last element is confirmed
    post_retrieve[last_index] = root

    # The two retrievals of the left subtrees
    pre_left_subtree = pre_retrieve[1:root_index+1]
    in_left_subtree = in_retrieve[0:root_index]
    # Populate the post_retrieve of the left subtree
    post_retrieve[0:root_index] \
        = traversal(pre_left_subtree, in_left_subtree)

    # The two retrievals of the right subtrees
    in_right_subtree = in_retrieve[root_index+1:]
    pre_right_subtree = pre_retrieve[root_index+1:]
    # Populate the post_retrieve of the right subtree
    post_retrieve[root_index:last_index] \
        = traversal(pre_right_subtree, in_right_subtree)

    # Return the populated list
    return post_retrieve

def main():
    pre_retrieve = [1, 2, 3, 4, 5, 6]
    in_retrieve = [3, 2, 4, 1, 6, 5]
    post_retrieve = traversal(pre_retrieve, in_retrieve)
    print(post_retrieve)


if __name__ == '__main__':
    main()

