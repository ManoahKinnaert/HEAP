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

        // TODO: generate theoretical data

        int[] sizes = new int[100];
        for (int i = 0; i < 100; i++) sizes[i] = i;

        System.out.println(compares);
        System.out.println(exchanges);

        XYSeriesCollection comparesSet = generateDataset("Compares", sizes, compares, compares);
        XYSeriesCollection exchangesSet = generateDataset("Exchanges", sizes, exchanges, exchanges);

        new Chart("HEAP - 1", comparesSet, exchangesSet);
    }
}
