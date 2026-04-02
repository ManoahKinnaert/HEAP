package com.manoahkinnaert.experiments;

import com.manoahkinnaert.chart.Chart;
import com.manoahkinnaert.core.Heap;

import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.util.ArrayList;

public class Heap1 extends HeapExp {

    private final int[] sizes = new int[100];

    private void generateInsertData(Heap heap, ArrayList<Integer> compares, ArrayList<Integer> comparesTheoretical) {
        // generate worst case input
        int[] array = new int[sizes.length];
        for (int i = 0; i < sizes.length; i++)
            array[i] = i;
        // build the heap and get the data
        for (int n = 1; n <= sizes.length; n++) {
            heap.clear();
            // build heap
            for (int i = 0; i < n; i++)
                heap.insert(i);
            // get data
            compares.add(heap.getCounter().getCompares());
            heap.resetCounter();
        }
        // generate the theoretical data
        for (int n = 1; n <= 100; n++)
            comparesTheoretical.add((int) (1 + ((Math.log(n) / Math.log(2)))));
    }

    private void generateDeleteMaxData(Heap heap, ArrayList<Integer> compares, ArrayList<Integer> comparesTheoretical) {
        for (int k=1; k <= sizes.length; k++) {
            heap.clear();
            heap.resetCounter();
            // First we want to generate the heap
            // generate worst case input
            int[] array = new int[k + 1];
            for (int i = 0; i < k + 1; i++)
                array[i] = i;
            // build the heap
            for (int j: array)
                heap.insert(j);
            heap.resetCounter();
            // Now delete the top node
            heap.delMax();
            // Add the data to the compares
            compares.add(heap.getCounter().getCompares());
        }
        // generate theoretical data
        for (int n = 1; n <= 100; n++)
            comparesTheoretical.add((int) ((Math.log(n) / Math.log(2))));
    }

    public void run() {
        Heap heap = new Heap();

        for (int i = 0; i < 100; i++)
            sizes[i] = i + 1;

        ArrayList<Integer> compares = new ArrayList<>();
        ArrayList<Integer> comparesTheoretical = new ArrayList<>();

        ArrayList<Integer> deletionCompares = new ArrayList<>();
        ArrayList<Integer> deletionComparesTheoretical = new ArrayList<>();

        generateInsertData(heap, compares, comparesTheoretical);
        generateDeleteMaxData(heap, deletionCompares, deletionComparesTheoretical);

        XYSeriesCollection comparesSet = new XYSeriesCollection(generateDataset("Insert Compares", sizes, compares));
        comparesSet.addSeries(generateDataset("Deletion Compares", sizes, deletionCompares));

        XYSeriesCollection theoreticalSet = new XYSeriesCollection(generateDataset("Theoretical Insert Compares", sizes, comparesTheoretical));
        theoreticalSet.addSeries(generateDataset("Theoretical Deletion Compares", sizes, deletionComparesTheoretical));

        new Chart("HEAP - 1", comparesSet, theoreticalSet);
    }
}
