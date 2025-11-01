Ex. Tree Traversals Again
=========================

For example

.. code-block:: text

   pre_list   1 2 3   4 5  6 
   in_list    3 2 4   1 6  5
   post_list [= = =] [- -] 1

retrieve the root from ``pre``
The node that precedes the root node is the left subtree, i.e., ``[3, 2, 4]``.
The node that succeeds the root node is the right subtree, i.e., ``[6, 5]``.

::

   root = pre_list[0]
   root_index = in_list.index(root)
   last_index = len(post_list) - 1

so, for left subtree we have:

.. code-block:: text

   pre_list  2 3 4  |  pre[1:root_index+1]
   in_list   3 2 4  |  in_list[0:root_index]
   post_list = = 2  |  post_list[post_list] = root

for right subtree we have:

.. code-block:: text

   pre_list  5 6    |  pre[root_index+1:] 
   in_list   6 5    |  in_list[root_index+1:]
   post_list - 5    |  post_list[post_list] = root


Interface
---------

.. automodule:: tta
   :members:
   :special-members: __init__
   :exclude-members: main