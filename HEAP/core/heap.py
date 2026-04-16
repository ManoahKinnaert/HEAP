from utils import less, exch
from utils.counter import Counter 

class Heap:
    def __init__(self):
        self._counter = Counter()
    
        self._arr = [None]
        self._n = 0

    @property
    def size(self):
        return len(self._arr) - 1

    @property
    def compares(self):
        return self._counter.compares
    
    @property
    def exchanges(self):
        return self._counter.exchanges

    def reset_counter(self):
        self._counter.reset()

    def _swim(self, k: int):
        while (k > 1 and less(self._arr, k // 2, k, self._counter)):
            exch(self._arr, k, k // 2, self._counter)
            k = k // 2

    def _sink(self, k: int):
        while 2 * k <= self._n:
            j = 2 * k 
            if j < self._n and less(self._arr, j, j + 1, self._counter): j += 1
            if not less(self._arr, k ,j, self._counter): break
            exch(self._arr, k, j, self._counter)
            k = j
    
    def insert(self, key):
        self._arr.append(key)
        self._n += 1
        self._swim(self._n)

    def del_max(self):
        max = self._arr[1]
        self._n -= 1
        exch(self._arr, 1, self._n, self._counter)
        self._sink(1)
        del self._arr[self._n + 1]
        return max