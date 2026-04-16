"""
This file contains everything concerning the Heap 1 experiment. 
This experiment aims to show that the basic heap operations swim, sink, getting the max value and removing the max value, can be 
executed in log time (with n the amount of elements present in the heap at the time of insert or deletion).
"""
from core.heap import Heap 
import matplotlib.pyplot as plt 
import numpy as np
import math

class Heap1:
    def __init__(self):
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2)

        self.x = []
        self.y_log = []
        self.y_compares = []
        self.y_exchanges = []

    def construct_heap(self, size: int):
        heap = Heap()
        values = list(np.random.uniform(low=0, high=size, size=size))
        for i in range(len(values)):
            heap.insert(values[i])
            self.x.append(i)
            self.y_compares.append(heap.compares)
            self.y_exchanges.append(heap.exchanges)
            heap.reset_counter()
        
    def run_exp(self):
        self.construct_heap(10000) 

    def plot_findings(self):
        self.y_log = [1 + math.floor(math.log2(i+1)) for i in self.x]
        self.ax1.scatter(self.x, self.y_compares)
        self.ax1.plot(self.x, self.y_log, color="red")
        self.ax1.set_title("Compares")

        self.ax2.scatter(self.x, self.y_exchanges)
        self.ax2.set_title("Echanges")

        plt.show()

    # the main run function called to run and display the experiment 
    def run(self):
        self.run_exp()
        self.plot_findings()