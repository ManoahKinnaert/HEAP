from utils import less, exch

class Heap:
    def __init__(self):
        self._counter = None
    
        self._arr = [self._size]
        self._n = 0

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
        while 2 * k <= self._n:
            j = 2 * k 
            if j < self._n and less(self._arr, j, j + 1): j += 1
            if not less(self._arr, k ,j): break
            exch(self._arr, k, j)
            k = j
    
    def insert(self, key):
        self._arr.append(key)
        self._n += 1
        self._swim(self._n)