Sequence List
=============

**Source code:** `src/pydsadoc/_linear/contiguous.py <https://github.com/Enec0De/pydsadoc/blob/main/src/pydsadoc/_linear/contiguous.py>`__

.. py:currentmodule:: pydsadoc

.. autoclass:: SequenList
   :members:
   :special-members: __str__

.. rubric:: Stack


A stack can be implemented with a sequential list :py:class:`SequenList` and its
methods :py:meth:`SequenList.append` and :py:meth:`SequenList.pop` as described
above.  Specifically, the ``stack.append(object)`` and ``stack.pop()``
operations.

Notably, in this case, the time complexity of these two methods is
:math:`O(1)`.

.. rubric:: Queue

A queue can be implemented with a sequential list :py:class:`SequenList` and its
methods :py:meth:`SequenList.append` and :py:meth:`SequenList.pop` as described
above.  Specifically, the ``queue.append(object)`` and ``queue.pop(0)``
operations.

Notably, in this case, the time complexity of the method
:py:meth:`SequenList.append` is :math:`O(1)`, but of the method 
:py:meth:`SequenList.pop` is :math:`O(n)`.
