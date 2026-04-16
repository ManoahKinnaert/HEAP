"""
Small experiment counting comparisons of heapsort.
"""
from core.heap import Heap
import matplotlib.pyplot as plt 
import random
import math

class Heap2:
    def __init__(self):
        plt.style.use('ggplot')

        self.fig, (self.ax, self.ax2) = plt.subplots(1, 2)

        self.x = []
        self.y = [] 
        self.c = []

    def sort(self, size):
        heap = Heap()
        values = [random.uniform(0, size) for _ in range(size)]  
        heap.sort(values)
        self.x.append(size)
        self.y.append(heap.compares)
        heap.reset_counter()

        # try to estimate c
        # T(n) = C * n * log2(n)
        # so C = T(n) / (n * log2(n))
        self.c.append(self.y[-1] / (size * math.log2(size)))
    
    def run_exp(self):
        for s in range(10, 10010, 10): self.sort(s) 

    def plot_findings(self):
        self.ax.scatter(self.x, self.y, label="Measured")
        self.ax.plot(self.x, [2 * n * math.log2(n) for n in self.x], color="blue", label="Theoretical max")
    
        self.ax.set_title("Heapsort Comparisons")
        self.ax.set_xlabel("Input size (n)")
        self.ax.set_ylabel("Number of comparisons")
        self.ax.legend()

        self.ax2.plot(self.x, self.c, label="Estimated c")
        self.ax2.set_title("Estimation of C * n * log2(n)")
        self.ax2.set_xlabel("Input size (n)")
        self.ax2.set_ylabel("Estimation")
        self.ax2.legend()

        plt.show() 

    def run(self):
        self.run_exp()
        self.plot_findings()