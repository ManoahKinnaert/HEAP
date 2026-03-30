package com.manoahkinnaert.experiments;

import com.manoahkinnaert.chart.Chart;
import com.manoahkinnaert.core.Heap;
import org.jfree.data.xy.XYSeriesCollection;

import java.util.ArrayList;

public class Heap1 extends HeapExp {
    public void run() {
        Heap emptyHeap = new Heap();

        ArrayList<Integer> compares = new ArrayList<>();
        ArrayList<Integer> exchanges = new ArrayList<>();

        int[] randomArray = constructRandomArray(100);
        for (int j : randomArray) {
            emptyHeap.insert(j);
            // extract compares
            compares.add(emptyHeap.getCounter().getCompares());
            exchanges.add(emptyHeap.getCounter().getExchanges());
            emptyHeap.resetCounter();
        }

        XYSeriesCollection comparesSet = generateDataset("Compares", new int[100], compares, compares);
        XYSeriesCollection exchangesSet = generateDataset("Exchanges", new int[100], exchanges, exchanges);

        new Chart("HEAP - 1", comparesSet, exchangesSet);
    }
}
