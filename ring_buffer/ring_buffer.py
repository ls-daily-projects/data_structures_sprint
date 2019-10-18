class RingBuffer:
    """
    A ring buffer is a non-growable buffer with a fixed size.
    When the ring buffer is full and a new element is inserted,
    the oldest element in the ring buffer is overwritten with the newest element. 
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        self.storage[self.current] = item
        self.current = (self.current + 1) % self.capacity
        return self

    def get(self):
        return [item for item in self.storage if item != None]
