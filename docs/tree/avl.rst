AVL Tree
========

**Source code:** `src/tree/avl.py <https://github.com/Enec0De/pydsadoc/blob/main/src/tree/avl.py>`__

.. autoclass:: tree.AVLNode
.. autoclass:: tree.AVL
   :members: 
   :exclude-members: _level_order_traversal


Implementation Details
----------------------

.. py:currentmodule:: tree

The AVL tree is somewhat more difficult than other data structures, so there
are some implementation details to be shown.
These methods mainly form the basics of the :py:meth:`AVL.insert` and
:py:meth:`AVL.remove` operations described above.

.. rubric:: Methods for Maintaining Balance 

.. automethod:: tree.AVL._adjust
.. automethod:: tree.AVL._get_balance
.. automethod:: tree.AVL._get_height
.. automethod:: tree.AVL._rotation_left
.. automethod:: tree.AVL._rotation_right

.. rubric:: Other Methods

.. automethod:: tree.AVL._get_min
.. automethod:: tree.AVL._insert_recursion
.. automethod:: tree.AVL._remove_recursion