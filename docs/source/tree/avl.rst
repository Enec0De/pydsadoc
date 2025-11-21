AVL Tree
========

.. automodule:: tree.avl
   :members: 
   :exclude-members: _level_order_traversal


Implementation Details
----------------------

The AVL tree is somewhat more difficult than other data structures, so there
are some implementation details to be shown.
These methods mainly form the basics of the :py:meth:`AVL.insert` and
:py:meth:`AVL.remove` operations described above.

.. rubric:: Methods for Maintaining Balance 

.. automethod:: tree.avl.AVL._adjust
.. automethod:: tree.avl.AVL._get_balance
.. automethod:: tree.avl.AVL._get_height
.. automethod:: tree.avl.AVL._rotation_left
.. automethod:: tree.avl.AVL._rotation_right

.. rubric:: Other Methods

.. automethod:: tree.avl.AVL._get_min
.. automethod:: tree.avl.AVL._insert_recursion
.. automethod:: tree.avl.AVL._remove_recursion