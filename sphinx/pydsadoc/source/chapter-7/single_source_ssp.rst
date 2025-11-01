Single - Source SSP
===================

Theorem
-------

For a non - negative weighted graph, given vertices :math:`A` and
:math:`B \in S`, and any other vertex neighbor :math:`v \in S` where the set
:math:`S` is the collection of all of the neighbor vertices of :math:`A` in the
graph. The :math:`\text{weight}(A,v)` is the path weight directly from :math:`A`
to :math:`v`. We have:

**Lemma:** If :math:`\text{weight}(A,B)` meets the condition for all
:math:`v \in S`:

.. math::

   \text{weight}(A,B) \leq \text{weight}(A,v),

the global shortest path from :math:`A` to :math:`B` is the direct path from
:math:`A` to :math:`B`.

.. tip::
   It can be improved to be Dijkstra's Algorithm by replacing vertex :math:`A` 
   with the set :math:`S`.

Interface
---------

.. automodule:: single_source_ssp
   :members:
   :special-members: __init__
   :exclude-members: main