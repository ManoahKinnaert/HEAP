"""
Small experiment counting comparisons of heapsort.
"""
from core import heap
import matplotlib.pyplot as plt 
import random
import math

class Heap2:
    def __init__(self):
        plt.style.use('ggplot')

        self.fig, self.ax = plt.subplot()

        self.x = []
        self.y = [] 


    def run_exp(self):
        pass 

    def plot_findings(self):
        pass 

    def run(self):
        self.run_exp()
        self.plot_findings()