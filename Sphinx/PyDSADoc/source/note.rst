Note
====


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

.. literalinclude:: ../pysource/chapter_2/sequentiallist.py
   :pyobject: SeqList.len
   :dedent: 4
   :lines: 1,8-
   
        


    