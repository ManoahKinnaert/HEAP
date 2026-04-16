from utils import less, exch

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
        n = len(self._arr)
        while 2 * k <= n:
            j = 2 * k 
            if j < n and less(self._arr, j, j + 1): j += 1
            if not less(self._arr, k ,j): break
            exch(self._arr, k, j)
            k = j
    

