"""
This file contains everything concerning the Heap 1 experiment. 
This experiment aims to show that the basic heap operations swim, sink, getting the max value and removing the max value, can be 
executed in log time (with n the amount of elements present in the heap at the time of insert or deletion).
"""
from core.heap import Heap 
import matplotlib.pyplot as plt 
import random
import math

class Heap1:
    def __init__(self):
        plt.style.use('ggplot')

        self.fig1, ((self.ax1, self.ax2), (self.ax3, self.ax4)) = plt.subplots(2, 2)

        self.x = []
        self.x_heapify = []
        self.y_log = []
        self.y_compares_empty = []
        self.y_compares_heapify = []
        self.y_exchanges_empty = []
        self.y_exchanges_heapify = []

    def construct_heap_empty(self, size: int):
        heap = Heap()
        values = [random.uniform(0, size) for _ in range(size)]
        for i in range(len(values)):
            heap.insert(values[i])
            self.x.append(heap.size)
            self.y_compares_empty.append(heap.compares)
            self.y_exchanges_empty.append(heap.exchanges)
            heap.reset_counter()
        
    def construct_heapify(self, size: int):
        heap = Heap()
        for s in range(1, size + 1):
            values = [random.uniform(0, s) for _ in range(s)] 
            heap.heapify(values)
            self.x_heapify.append(s)
            self.y_compares_heapify.append(heap.compares)
            self.y_exchanges_heapify.append(heap.exchanges)
            heap.reset_counter()

    def run_exp(self, size=100, trials=20):
        self.x = []
        self.x_heapify = []
        self.y_log = []
        self.y_compares_empty = []
        self.y_compares_heapify = []
        self.y_exchanges_empty = []
        self.y_exchanges_heapify = []

        for _ in range(trials):
            self.construct_heap_empty(size) 
            self.construct_heapify(size)

    def plot_findings(self):
        self.y_log = [1 + math.floor(math.log2(i+1)) for i in list(set(self.x))]
        self.ax1.scatter(self.x, self.y_compares_empty, label="Measured")
        self.ax1.plot(list(set(self.x)), self.y_log, label="Theoretical worst", color="blue")
        self.ax1.set_title("Compares insert empty")
        self.ax1.set_xlabel("N (size of Heap at time of insert)")
        self.ax1.set_ylabel("Measured compares")
        self.ax1.set_yscale("log", base=2)
        self.ax1.set_xscale("log")
        self.ax1.legend()

        self.ax2.scatter(self.x, self.y_exchanges_empty, label="Measuerd")
        #self.ax2.plot(self.x, self.y_log, color="red", label="Theoretical worst")
        self.ax2.set_title("Exchanges insert empty")
        self.ax2.set_xlabel("N (size of Heap at time of insert)")
        self.ax2.set_ylabel("Measured exchanges")
        self.ax2.set_yscale("log", base=2)
        self.ax2.set_xscale("log")
        self.ax2.legend()

        self.ax3.set_title("Compares Heapify")
        self.ax3.scatter(self.x_heapify, self.y_compares_heapify, label="Measured")
        self.ax3.plot(list(set(self.x_heapify)), [2 * n for n in list(set(self.x_heapify))], label="Theoretical worst", color="blue")
        self.ax3.set_xlabel("N (heap size)")
        self.ax3.set_ylabel("Measured compares")
        self.ax3.legend()

        self.ax4.set_title("Exchanges Heapify")
        self.ax4.scatter(self.x_heapify, self.y_exchanges_heapify, label="Measured")
        self.ax4.plot(list(set(self.x_heapify)), [n for n in list(set(self.x_heapify))], label="Theoretical worst", color="blue")
        self.ax4.set_xlabel("N (heap size)")
        self.ax4.set_ylabel("Measured exchanges")
        self.ax4.legend()

        plt.show()

    # the main run function called to run and display the experiment 
    def run(self):
        self.run_exp()
        self.plot_findings()