package com.manoahkinnaert.experiments;

import com.manoahkinnaert.chart.Chart;
import com.manoahkinnaert.core.Heap;
import org.jfree.data.xy.XYSeriesCollection;

import java.util.ArrayList;

public class Heap1 extends HeapExp {
    public void run() {
        Heap heap = new Heap();

        ArrayList<Integer> compares = new ArrayList<>();
        ArrayList<Integer> comparesTheoretical = new ArrayList<>();

        // generate worst case input
        int[] array = new int[100];
        for (int i = 0; i < 100; i++)
            array[i] = i;

        for (int j : array) {
            heap.insert(j);
            compares.add(heap.getCounter().getCompares());
            heap.resetCounter();
        }

        int[] sizes = new int[100];
        for (int i = 0; i < 100; i++)
            sizes[i] = i + 1;
        
        for (int n = 1; n <= 100; n++)
            comparesTheoretical.add((int) (Math.log(n) / Math.log(2)));
        
        XYSeriesCollection comparesSet = generateDataset("Compares", sizes, compares);
        XYSeriesCollection theoreticalSet = generateDataset("Compares Theoretical", sizes, comparesTheoretical);

        new Chart("HEAP - 1", comparesSet, theoreticalSet);
    }
}
