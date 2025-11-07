Miscellaneous Notes (draft)
===========================


::

    def Treaverse():
        # Code to be run
        ... 

        Treaverse() # Entry point
        # Return point

        # The rest code to be run
        ...

::

    while stack:

        current, status = pop()

        if status == 0:
            # Code to be run
            ...

            # Change the status of current
            push(current, 1)

            # The next function to be excuted
            push(current.next, 0)

            # Return point
            continue
        
        elif status == 1:
            ...

::

    class Sentinel:
    """Unique sentinel value."""
    _registry = None

    def __new__(cls):
        if cls._registry is None:
            cls._registry = super().__new__(cls)
        return cls._registry

    def __repr__(self):
        return 'Sentinel'


.. literalinclude:: /../../src/chapter_2/sequentiallist.py
   :pyobject: SeqList.len
   :dedent: 4
   :lines: 1,8-
   
.. rubric:: To do list:

* Simplify the :ref:`sequential-list`.

* Fix :py:meth:`pre_order_traversal() <tree.BinaryTree.pre_order_traversal>` 
  in the Prelusion of Tree.

* Test :ref:`tree`. It must be wrong.
    