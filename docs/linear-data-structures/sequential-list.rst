Sequential List
===============

**Source code:** `src/pydsadoc/_linear/seque.py <https://github.com/Enec0De/pydsadoc/blob/main/src/pydsadoc/_linear/seque.py>`__

.. py:currentmodule:: pydsadoc

.. autoclass:: SeqList
   :members:
   :special-members: __str__

.. rubric:: Stack


A stack can be implemented with a sequential list :py:class:`SeqList` and its
methods :py:meth:`SeqList.append` and :py:meth:`SeqList.pop` as described
above.  Specifically, the ``stack.append(object)`` and ``stack.pop()``
operations.

Notably, in this case, the time complexity of these two methods is
:math:`O(1)`.

.. rubric:: Queue

A queue can be implemented with a sequential list :py:class:`SeqList` and its
methods :py:meth:`SeqList.append` and :py:meth:`SeqList.pop` as described
above.  Specifically, the ``queue.append(object)`` and ``queue.pop(0)``
operations.

Notably, in this case, the time complexity of the method
:py:meth:`SeqList.append` is :math:`O(1)`, but of the method 
:py:meth:`SeqList.pop` is :math:`O(n)`.
