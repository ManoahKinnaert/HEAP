class Heap:
    def __init__(self, size: int):
        self._size = size   # theoretical size
        self._counter = None
    
        self._arr = [self._size]


    @property
    def size(self):
        return self._size

    @property
    def compares(self):
        return self._counter.compares

    def reset_counter(self):
        self._counter.reset()

   
    def _swim(self, k: int):
        while (k > 1 and less(self._arr, k // 2, k)):
            exch(self._arr, k, k // 2)
            k = k // 2

    def _sink(self, k: int):
        pass 

