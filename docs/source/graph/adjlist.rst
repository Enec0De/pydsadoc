Adjacency List Graph
====================

.. automodule:: graph.adjlist
   :members:

.. rubric:: Dijkstra's Algorithm

The Dijkstra's algorithm can be optimized by using
:py:class:`~tree.huffman.MinHeap` in the
:ref:`previous chapter <tree-chapter>`, or :py:mod:`heapq` in the python
standard library.  The algorithm is more efficient in sparse graph.

.. rubric:: Kruskal's Algorithm

The key to the optimization of the Kruskal's algorithm is the implementation of
the :py:class:`~tree.dsu.UnionFind` in the
:ref:`previous chapter <tree-chapter>`, which applies the path compression and
union by rank in it.  The algorithm is more efficient in sparse graph, too.