Adjacency Matrix Graph
======================

.. autoclass:: graph.MGraph
   :members:

.. rubric:: Floyd-Warshall Algorithm

The adjacency list for graph representation suits most algorithms except the
Floyd-Warshall Algorithm. The Floyd-Warshall Algorithm is more efficient in a
graph represented by an adjacency matrix.

.. rubric:: Prim's Algorithm

The key to the optimization of the Prim's algorithm is the implementation of a
priority queue, such as the :py:class:`~tree.huffman.MinHeap` in the 
:ref:`previous chapter <tree-chapter>`, or the :py:mod:`heapq` in the python
standard library.

The algorithm is more efficient for dense graph. Also, it offers more
flexibility when implemented with an adjacency list for graph representation.
Combining with the priority queue and adjacency list, its time complexity can
be optimized to :math:`O(\vert E \vert \log \vert V \vert)`.