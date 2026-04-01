package com.manoahkinnaert.experiments;

import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.util.ArrayList;
import java.util.Random;

public class HeapExp {
    // Helper function to generate a Dataset to be used in the charts
    public XYSeriesCollection generateDataset(String name, int[] sizes, ArrayList<Integer> data) {
        assert sizes.length == data.size();
        XYSeries measuredSeries = new XYSeries("Measured " + name);
        for (int i = 0; i < sizes.length; i++) {
            measuredSeries.add(sizes[i], data.get(i));
        }
        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(measuredSeries);
        return dataset;
    }

    // Helper function to generate a random fixed size array
    public int[] constructRandomArray(int size) {
        int[] randomArray = new int[size];
        Random random = new Random();
        for (int i=0; i < size; i++) randomArray[i] = random.nextInt();
        return randomArray;
    }
}
