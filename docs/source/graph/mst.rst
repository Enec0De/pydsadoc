Minimum Spanning Tree
=====================

.. automodule:: graph.mst
   :members:

Prim's Alogorithm
-----------------

The key to the optimization of the Prim's algorithm is the implementation of a
priority queue, such as the :py:class:`~tree.huffman.MinHeap` in the 
:ref:`previous chapter <tree-chapter>`, or the :py:mod:`heapq` in the python
standard library.


Kruskal's Alogorithm
--------------------
The key to the optimization of the Kruskal's algorithm is the implementation of
the :py:class:`~tree.dsu.UnionFind` in the
:ref:`previous chapter <tree-chapter>`, which applies the *path compression*
and *union by rank* in it.