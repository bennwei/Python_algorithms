# -*- coding: utf-8 -*-
class LinedQueue:
    """ FIFO queue implementation using a singly linked list for storage. """
    #-------------------------- nested Node class --------------------------
    class _Node:
        """ Lightweight, nonpublic class for storing a singly linked node. """
        __slots__ = '_element', '_next'     # streamline memory usage
        
        def __init__(self, element, next):    # initialize node’s fields
            self._element = element    # reference to user’s element
            self._next = next    # reference to next node
    
    #------------------------------- Queue methods -------------------------------
    def __init__(self):
        """ Create an empty stack. """
        self._head = None       # reference to the head node
        self._tail = None
        self._size = 0
    
    def __len__(self):
        """ Return the number of elements in the Queue. """
        return self._size
    
    def is_empty(self):
        """ Return True if the queue is empty. """
        return self._size == 0
    
    def first(self):
        """ Return (but do not remove) the element at the front of queue. 
        Raise Empty exception if the Queue is empty. """
        
        if self.is_empty():
            raise ("Queue is empty")
        return self._head._element
    
    def dequeue(self): 
        """ Remove and return the first element of the queue (i.e., FIFO)."""
        if self.is_empty():
            raise ("Queue is empty.")
        answer = self._head._element
        self._head = self._head._next
        self.size -= 1
        if self.is_empty():    # special case as queue is empty
            self._tail = None    # removed head had been the tail
        return answer
        
    def enqueue(self, e):
        """ Add an element to the back of queue. """
        newest = self._Node(e, None)    # node will be new tail node
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
        
            
        
        
        
    