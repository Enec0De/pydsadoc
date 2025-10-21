:tocdepth: 3


Linear List
===========

Linear list is a data structure that stores data elements in a linear order.

Fundamental 
-----------

.. automodule:: linearlist

   .. rubric:: Sequential List 

   A sequential list has a basic structure similar to the built-in ``List`` 
   type.

   .. autoclass:: SequentialList
      :members:
      :special-members: __init__


   .. rubric:: Sequential Stack
   
   Stack is a linear list that follows the Last-In-Fist-Out (LIFO) principle.
   Implementing a single stack with a sequential list can be done in the same 
   way. So I will just present the dual stack.
   
   .. autoclass:: SequentialDualStack
      :members:
      :special-members: __init__
   
   
   .. rubric:: Sequential Queue
   
   Queue is the linear list follows the First-In-First-Out (FIFO) principle.
   
   .. autoclass:: SequentialQueue
      :members:
      :special-members: __init__
   

   .. rubric:: Node

   All of the linked lists are comprised of :py:class:`linearlist.Node`.
   
   .. autoclass:: Node
      :special-members: __init__
   
   
   .. rubric:: Linked List
   
   The linked list initialized with a *Sentinel Node* (or *Dummy Node*), whose 
   data is None, will always begin with this *Sentinel Node* (or *Dummy Node*). 
   And the head always reference to this *Sentinel Node*.
   
   .. autoclass:: LinkedList
      :members:
      :special-members: __init__
   
   
   .. rubric:: Linked Stack
   
   .. autoclass:: LinkedStack
      :members:
      :special-members: __init__
   
   
   .. rubric:: Linked Queue
   
   .. autoclass:: LinkedQueue
      :members:
      :special-members: __init__


Generalization
--------------

Generalized List
''''''''''''''''

The generalized list is the generalization of the linear list. It means that one
the elements of generalized list may be either single element or other
generalized list. In python, you just make the data of Node reference the 
linkedlist. But it will be moer eleborate in C. It's just like:

.. code-block:: C

   typedef struct GNode *GList;
   struct GNode{
       int Tag;                // Tag field: 0 for atomic element, 1 for sublist
       union { 
           ElementType Data;   // Stores atomic data (valid when Tag is 0)
           GList SubList;      // Points to a sublist (valid when Tag is 1)
       } URegion;              // Union: atomic data or sublist pointer
       GList Next;             // Pointer to the next GNode
   };


Multilinked List
''''''''''''''''

Nodes in the linked list may point to more than one other node, which is not
the circle reference(it may reference the doubly linked list.), considered as
the *Multilinked List*. For example, the *Orthogonal List*.
