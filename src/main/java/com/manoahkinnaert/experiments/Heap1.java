package com.manoahkinnaert.experiments;

import com.manoahkinnaert.chart.Chart;
import com.manoahkinnaert.core.Heap;
import org.jfree.data.xy.XYSeriesCollection;

import java.util.ArrayList;

public class Heap1 extends HeapExp {
    public void run() {
        Heap emptyHeap = new Heap();

        ArrayList<Integer> compares = new ArrayList<>();
        ArrayList<Integer> comparesTheoretical = new ArrayList<>();
        ArrayList<Integer> exchanges = new ArrayList<>();
        ArrayList<Integer> exchangesTheoretical = new ArrayList<>();

        int[] randomArray = constructRandomArray(100);
        for (int j : randomArray) {
            emptyHeap.insert(j);
            // extract compares
            compares.add(emptyHeap.getCounter().getCompares());
            exchanges.add(emptyHeap.getCounter().getExchanges());
            emptyHeap.resetCounter();
        }

        int[] sizes = new int[100];
        for (int i = 0; i < 100; i++) sizes[i] = i;

        // TODO: Generate theoretical data
        for (int n = 0; n < 100; n++) {
            if (n <= 1) {
                comparesTheoretical.add(0);
            } else {
                comparesTheoretical.add((int) (Math.log(n) / Math.log(2)));
            }

        }

        System.out.println(compares);
        System.out.println(exchanges);

        XYSeriesCollection comparesSet = generateDataset("Compares", sizes, compares, comparesTheoretical);
        XYSeriesCollection exchangesSet = generateDataset("Exchanges", sizes, exchanges, exchanges);

        new Chart("HEAP - 1", comparesSet, exchangesSet);
    }
}
