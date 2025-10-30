Complete Binary Search Tree
===========================

For n nodes, for :math:`k` meet the condition :math:`2^k \leq n \leq 2^{k+1}`.
:math:`n - 2^k` (last layers of the tree) sperates to two parts: Precedes
:math:`2^{k-1}` and succeeds :math:`2^{k-1}`. Expect root node and last layer,
left subtree has :math:`2^{k-1} - 1` nodes and right subtree also has
:math:`2^{k-1} - 1` nodes. Last layer may has up to :math:`2^k` nodes.

::

    # k = n.bit_length() - 1
    k = floor(log(n,2))

    if n < 2**k + 2**(k-1):
       left.size = n - 2**(k-1)
    else:
       left.size = 2**k - 1

for a sorted list: 

.. code-block:: text

   data_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   the root node is data_list[6] = 6
   then the left sub tree is data_list[:6] = [0, 1, 2, 3, 4, 5]
   the right sub tree is data_list[7:] = [7, 8, 9]

the same process to the left sub tree 

.. code-block:: text

   left_list = [0, 1, 2, 3, 4, 5]
   the root node is left_list[3] = 3
   the left sub tree is left_list[:3] = [0, 1, 2]
   the right sub tree is left_list[4:] = [4, 5]


Interface
---------

.. automodule:: cbst
   :members:
   :special-members: __init__
   :exclude-members: main