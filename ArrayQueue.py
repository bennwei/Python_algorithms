class ArrayQueue(object):
    """ FIFO queue implementation using a Python list as underlying storage. """
    default_capacity = 10     # moderate capacity for all new queues
    
    def __init__(self):
        """ made an empty queue. """
        self._data = [None] * ArrayQueue.default_capacity
        self._size = 0
        self._front = 0
    
    def __len__(self):
         """ Return the number of elements in the queue. """
         return self._size
    
    def is_empty(self):
        """ Return True if the queue is empty. """
        return self._size == 0
    
    def first(self):
        """ Return (but do not remove) the element at the front of the queue. """
        if self.is_empty():
            raise ('Queue is empty')
        return self._data[self._front]
        
    def dequeue(self):
        """ Remove and return the first element of the queue (i.e., FIFO). """
        if self.is_empty():
            raise  ('Queue is empty')
            item_out = self._data[self._front]
            self._data[self._front] = None    # help garbage collection
            self._front = (self._front + 1) % len(self._data)    # implement a circular array. reset front position
            self._size -= 1
        return item_out
        
    def enqueue(self, e):
        """ Add an element to the back of queue. """
        if self._size == len(self._data):
            self.resize(2*len(self._data))    # if queue is full, double the array size
            empty_position = (self._front + self._size) % len(self.data)
            self._data[empty_position] = e
            self._size += 1
            
    def _resize(self, cap):
        """ Resize to a new list of capacity >= len(self)."""
        oldList = self._data    # keep track of existing list
        self._data = [None] * cap     # allocate list with new capacity
        walk = self._front
        for k in range(self._size):     # only consider existing elements
            self._data[k] = oldList[walk]
            walk = (1+walk) % len(oldList)
        self._front = 0
            
        
        
    
            
        
          