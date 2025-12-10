AVL Tree
========

**Source code:** `src/pydsadoc/_tree/avl.py <https://github.com/Enec0De/pydsadoc/blob/main/src/pydsadoc/_tree/avl.py>`__

.. py:currentmodule:: pydsadoc

.. autoclass:: AVL
   :members: 
   :exclude-members: _level_order_traversal


Implementation Details
----------------------

The AVL tree is somewhat more difficult than other data structures, so there
are some implementation details to be shown.
These methods mainly form the basics of the :py:meth:`AVL.insert` and
:py:meth:`AVL.remove` operations described above.

.. rubric:: Methods for Maintaining Balance 

.. automethod:: AVL._adjust
.. automethod:: AVL._get_balance
.. automethod:: AVL._get_height
.. automethod:: AVL._rotation_left
.. automethod:: AVL._rotation_right

.. rubric:: Other Methods

.. automethod:: AVL._get_min
.. automethod:: AVL._insert_recursion
.. automethod:: AVL._remove_recursion