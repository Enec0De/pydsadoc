.. _sort-chapter:

Sorting Algorithms
==================

**Source code:** `src/pydsadoc/sorting/__init__.py <https://github.com/Enec0De/pydsadoc/blob/main/src/pydsadoc/sorting/__init__.py>`__

A *Sorting Algorithm* is used to rearrange a given array or list of elements in
an order. 


Comparison Based Sort
---------------------

.. py:currentmodule:: pydsadoc.sorting

We compare the elements in a comparison-based sorting algorithm.

.. rubric:: Basics Sorting Algorithms

.. autofunction:: bubble_sort
.. autofunction:: insertion_sort
.. autofunction:: selection_sort

.. rubric:: Advanced Sorting Algorithms

.. autofunction:: shell_sort

.. seealso::

   The `Sedgewick sequence <https://oeis.org/A033622>`__ of increments for
   Shell sort (best on big values).

.. autofunction:: heap_sort
.. autofunction:: merge_sort
.. autofunction:: quick_sort
.. autofunction:: tim_sort


Non-Comparison Based Sort(TBD)
------------------------------

We do not compare the elements in a non-comparison-based sorting algorithm.

.. autofunction:: bucket_sort
.. autofunction:: count_sort
.. autofunction:: radix_sort
