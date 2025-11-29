Disjoint Set Union
==================

**Source code:** `src/tree/dsu.py <https://github.com/Enec0De/pydsadoc/blob/main/src/tree/dsu.py>`__

.. autoclass:: tree.UnionFind
   :members:
   :special-members: __str__

.. rubric:: The Amortized Time

.. py:currentmodule:: tree

In this case, The Inverse `Ackermann Function`_ :math:`\alpha(n)` is in fact
treated as a constant. So the amortized time complexity of the two operations
of the :py:class:`UnionFind` can be optimized to :math:`O(1)`.

.. _Ackermann Function: https://mathworld.wolfram.com/AckermannFunction.html
