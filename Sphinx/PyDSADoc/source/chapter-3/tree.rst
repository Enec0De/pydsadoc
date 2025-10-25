Prelusion
=========

The conception is arise from the algorithm: the binary search algorithm:

.. automodule:: search
   :members:


Conception
----------

Tree
    A finite set comprised of :math:`n` nodes. It's *Empty Tree* only when 
    :math:`n = 0`, otherwise *Non-empty Tree*.
    For *Non-empty Tree*, There is a special node called *Root*. All nodes can
    be separated to :math:`m (m > 0)` disjoint sets, namely 
    :math:`T_1, T_2, ...`, every set is also a *Tree* which is called
    *Sub Tree*.

Degree
    *Degree* of a node is the number of the *Sub Tree* that belongs to itself. 
    The *Degree of the Tree* presents the maximum *Degree* within all of nodes.

Leaf
    The node whose *Degree* is 0.

Parent
    The node that has *Sub Tree* is the *Parent* node of its *Sub Tree*.

Child
    The node :math:`A` is the *Child* of the node :math:`B` if and only if 
    :math:`B` is the *Parent* of :math:`A`.

Sibling
    The nodes who have the same *Parent*.

Path and Length 
    A sequence :math:`n_1, n_2, ..., n_k`, within which :math:`n_i` is the 
    *Parent* of :math:`n_{n+1}`, is the *Path* from :math:`n_1` to
    :math:`n_k`. The node number of the sequence is the *length* of the *Path*.

Ancestor
    All nodes in the *Path* from *Root* to a node are the *Ancestor* of this
    node.

Descendant
    All nodes in the *Sub Tree* of a node are the *Descendant* of this node.

Level
    The *Level* of the *Root* is 1. The *Level* of a node is the *Level* of its
    *Parent* plus 1.

Depth
    The maximum *Level* of the nodes in a *Tree*.


Binary Tree
-----------

Inspired by :py:func:`binary_search`, we have some new conception as follows:

* *Skewed Binary Tree*
* *Perfect Binary Tree* (*Full Binary Tree*)
* *Complete Binary Tree*

.. rubric:: The relation between number of nodes:

.. math::

   n_0 + n_1 + n_2 - 1 &= 0 \times n_0 \times n_1 \times 2n_2 \\
   n_0 &= n_2 + 1

Implementation
--------------

.. automodule:: tree
   :members: