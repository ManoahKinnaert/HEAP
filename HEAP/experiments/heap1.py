"""
This file contains everything concerning the Heap 1 experiment. 
This experiment aims to show that the basic heap operations swim, sink, getting the max value and removing the max value, can be 
executed in log time.
"""
from core.heap import Heap 
import matplotlib.pyplot as plt 
import numpy as np

class Heap1:
    def __init__(self):
        self.fix, (self.ax1, self.ax2) = plt.subplots(1, 2)

        self.x = []
        self.y_compares = []
        self.y_exchanges = []

    def construct_heap(self, size: int):
        heap = Heap()
        values = list(np.random.uniform(low=0, high=size, size=size))
        for val in values:
            heap.insert(val)
            self.x.append(size)
            self.y_compares.append(heap.compares)
            self.y_exchanges.append(heap.exchanges)

    def run_exp(self):
        for size in range(10, 100, 10):
            self.construct_heap(size) 
            print(self.x)
            print(self.y_compares)
            print(self.y_exchanges)

    def plot_findings(self):
        self.ax1.scatter(self.x, self.y_compares)
        self.ax1.set_title("Compares")

        self.ax2.scatter(self.x, self.y_exchanges)
        self.ax2.set_title("Echanges")
        
        plt.show()

    # the main run function called to run and display the experiment 
    def run(self):
        self.run_exp()
        self.plot_findings()