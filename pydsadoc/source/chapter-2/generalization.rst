Generalization
==============

Generalized List
----------------

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
----------------

Nodes in the linked list may point to more than one other node, which is not
the circle reference(it may reference the doubly linked list.), considered as
the *Multilinked List*. For example, the *Orthogonal List*.
