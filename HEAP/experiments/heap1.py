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
        self.fig2, (self.ax7, self.ax8) = plt.subplots(1, 2)
        self.fig3, (self.ax5, self.ax6) = plt.subplots(1, 2)

        self.init_data_arrays()
    
    def init_data_arrays(self):
        self.x = []
        self.x_worst = []
        self.x_heapify = []
        self.y_log = []
        self.y_compares_empty_worst = []
        self.y_compares_empty = []
        self.y_compares_heapify = []
        self.y_exchanges_empty = []
        self.y_exchanges_empty_worst = []
        self.y_exchanges_heapify = []

        self.x_del = []
        self.y_del_compares = []
        self.y_del_exchanges = []

    def construct_heap_empty(self, size: int, count=True):
        heap = Heap()
        values = [random.uniform(0, size) for _ in range(size)]
        for i in range(len(values)):
            heap.insert(values[i])
            if count:
                self.x.append(heap.size)
                self.y_compares_empty.append(heap.compares)
                self.y_exchanges_empty.append(heap.exchanges)
            heap.reset_counter()
        return heap


    def construct_heap_empty_worst(self, size: int, count=True):
        heap = Heap()
        values = range(size)
        for val in values:
            heap.insert(val)
            if count:
                self.x_worst.append(heap.size)
                self.y_compares_empty_worst.append(heap.compares)
                self.y_exchanges_empty_worst.append(heap.exchanges)
            heap.reset_counter()
        return heap
        
    def construct_heapify(self, size: int, count=True):
        heap = Heap()
        values = [random.uniform(0, size) for _ in range(size)] 
        for s in range(1, size):
            heap.heapify(values[:s])
            if count:
                self.x_heapify.append(heap.size)
                self.y_compares_heapify.append(heap.compares)
                self.y_exchanges_heapify.append(heap.exchanges)
            heap.reset_counter()
        return heap

    def run_exp(self, size=100, trials=20):
        self.init_data_arrays()

        # heap building experiments
        self.construct_heap_empty(size) 
        self.construct_heap_empty_worst(size)
        self.construct_heapify(size)
        
        # delete max from heap experiments
        h = self.construct_heap_empty(size, False)

        for _ in range(size):
            self.x_del.append(h.size)
            h.del_max()
            self.y_del_compares.append(h.compares)
            self.y_del_exchanges.append(h.exchanges)
            h.reset_counter()

    def plot_findings_heap_build(self):
        self.ax1.scatter(list(set(self.x)), self.y_compares_empty, label="Measured")
        self.ax1.plot(list(set(self.x)), [1 + math.floor(math.log2(n)) for n in list(set(self.x))], label="Theoretical worst", color="blue")
        self.ax1.set_title("Compares insert (random)")
        self.ax1.set_xlabel("N (size of Heap at time of insert)")
        self.ax1.set_ylabel("Measured compares")
        self.ax1.set_yscale("log", base=2)
        self.ax1.legend()

        self.ax2.scatter(list(set(self.x)), self.y_exchanges_empty, label="Measuerd")
        self.ax2.plot(list(set(self.x)), [math.floor(math.log2(n)) for n in list(set(self.x))], color="blue", label="Theoretical worst")
        self.ax2.set_title("Exchanges insert (random)")
        self.ax2.set_xlabel("N (size of Heap at time of insert)")
        self.ax2.set_ylabel("Measured exchanges")
        self.ax2.set_yscale("log", base=2)
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

        # worst case insert (compares)
        self.ax5.set_title("Compares insert worst case")
        self.ax5.scatter(self.x_worst, self.y_compares_empty_worst, label="Measured")
        self.ax5.plot(self.x_worst, [1 + math.floor(math.log2(n)) for n in self.x_worst], label="Theoretical worst", color="blue")
        self.ax5.set_xlabel("N (size of Heap at time of insert)")
        self.ax5.set_ylabel("Measuerd compares")
        self.ax5.legend()

        # worst case insert (exchanges) 
        self.ax6.set_title("Exchanges insert worst case")
        self.ax6.scatter(self.x_worst, self.y_exchanges_empty_worst, label="Measured")
        self.ax6.plot(self.x_worst, [math.floor(math.log2(n)) for n in self.x_worst], color="blue", label="Theoretical worst")
        self.ax6.set_xlabel("N (size of Heap at time of insert)")
        self.ax6.set_ylabel("Measured compares")
        self.ax6.legend()
    
    def plot_findings_heap_del(self):
        self.ax7.scatter(self.x_del, self.y_del_compares, label="Measuerd")
        self.ax7.plot(self.x_del, [2 * math.floor(math.log2(n)) for n in self.x_del], color="blue", label="Theoretical worst")
        self.ax7.set_title("Delete-max compares")
        self.ax7.set_xlabel("N (heap size)")
        self.ax7.set_ylabel("Measured compares")
        self.ax7.legend()

        self.ax8.scatter(self.x_del, self.y_del_exchanges, label="Measured")
        self.ax8.plot(self.x_del, [1 + math.floor(math.log2(n)) for n in self.x_del], color="blue", label="Theoretical worst")
        self.ax8.set_title("Delete-max exchanges")
        self.ax8.set_xlabel("N (heap size)")
        self.ax8.set_ylabel("Measured exchanges")
        self.ax8.legend()

    # the main run function called to run and display the experiment 
    def run(self):
        self.run_exp()
        self.plot_findings_heap_build()
        self.plot_findings_heap_del()
        plt.show()