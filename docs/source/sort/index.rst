.. _sort-chapter:

Sorting Algorithms
==================

Comparison Based Sort
---------------------

We compare the elements in a comparison-based sorting algorithm.

.. rubric:: Basics Sorting Algorithms

.. autofunction:: sort.bubble_sort
.. autofunction:: sort.insertion_sort
.. autofunction:: sort.selection_sort

.. rubric:: Advanced Sorting Algorithms

.. autofunction:: sort.shell_sort

.. seealso::

   The `Sedgewick sequence <https://oeis.org/A033622>`__ of increments for
   Shell sort (best on big values).

.. autofunction:: sort.heap_sort
.. autofunction:: sort.merge_sort
.. autofunction:: sort.quick_sort



Non-Comparison Based Sort
-------------------------

We do not compare the elements in a non-comparison-based sorting algorithm.

.. automodule:: sort.bucket
   :members:

.. automodule:: sort.counting
   :members:

.. automodule:: sort.radix
   :members:
