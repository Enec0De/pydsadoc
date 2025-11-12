Multi - Source SSP
==================

:math:`D^k[i][j]`: The shortest distance from the node :math:`i` to the node
:math:`j` cross the node :math:`l(l \leq k)`.

Updata :math:`D^k[i][j]` from :math:`D^{k-1}[i][j]` by evaluating:

.. math::

   D^k[i][j] = \min \left\{ 
       D^{k-1}[i][j], D^{k-1}[i][k] + D^{k-1}[k][j]
       \right\}


Interface
---------

.. automodule:: multi_source_ssp
   :members:
   :special-members: __init__
   :exclude-members: main