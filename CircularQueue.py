# -*- coding: utf-8 -*-
class CircularQueue:
    """ Queue implementation using circularly linked list for storage. """
    #-------------------------- nested Node class --------------------------
    class _Node:
        """ Lightweight, nonpublic class for storing a singly linked node. """
        __slots__ = '_element', '_next'     # streamline memory usage
        
        def __init__(self, element, next):    # initialize node’s fields
            self._element = element    # reference to user’s element
            self._next = next    # reference to next node
    
    #------------------------------- Queue methods -------------------------------
    def __init__(self):
        """ set a empty queue. """
        self._tail = None    # will represent tail of queue
        self._size = 0     # number of queue elements
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise ('Queue is empty.')
        head = self._tail._next
        return head._element
    
    def dequeue(self):
        if self.is_empty():
            raise ('Queue is empty.')
        old_head = self._tail._next
        if self._size == 1:    # removing only element
            self._tail = None    # queue becomes empty
        else:
            self._tail._next = old_head._next # bypass the old head
        self._size -= 1
        return old_head._element
        
    def enqueue(self, e):
        newest = self._Node(e, None)    # node will be new tail node
        if self.is_empty():
            newest._next = newest    # initialize circularly
        else:
            newest._next = self._tail._next     # new node points to head
            self._tail._next = newest    # old tail points to new node
        self._tail = newest
        self._size += 1
        
    def rotate(self):
          """ Rotate front element to the back of the queue. """
          if self._size > 0:
              self._tail = self._tail._next     # old head becomes new tail
        
        
        
        
        
        
        
        
        
        