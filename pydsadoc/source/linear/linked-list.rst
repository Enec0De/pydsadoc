Linked List
===========

.. automodule:: linear.linked
   :members:
   :special-members: __str__
   :exclude-members: main

.. rubric:: Stack

A stack can be implemented with a linked list :py:class:`LinkedList` and its
methods :py:meth:`LinkedList.insert` and :py:meth:`LinkedList.pop` as described
above. Specifically, the ``stack.insert(0, objcet)`` and ``stack.pop(0)``
operations.

Notably, in this case, the time complexity of these two methods is
:math:`O(1)`.

.. rubric:: Queue

A queue can be implemented with a linked list :py:class:`LinkedList` and its
methods :py:meth:`LinkedList.append` and :py:meth:`LinkedList.pop` as described
above. Specifically, the ``queue.append(object)`` and ``queue.pop(0)``
operations.

Notably, in this case, the time complexity of the method
:py:meth:`LinkedList.pop` is :math:`O(1)`, but of the method
:py:meth:`LinkedList.append` is :math:`O(n)`.
