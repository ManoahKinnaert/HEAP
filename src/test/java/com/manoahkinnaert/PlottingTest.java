package com.manoahkinnaert;

import com.manoahkinnaert.chart.Chart;
import com.manoahkinnaert.experiments.HeapExp;
import org.jfree.data.xy.XYSeriesCollection;

import java.util.ArrayList;

/*
 * This isn't a test as in the traditional sense of a test (unit test or regression test).
 * This is just to test the charting functionality.
 */
public class PlottingTest {

    public static void main(String[] args) {
        HeapExp exp = new HeapExp();

        ArrayList<Integer> test1 = new ArrayList<Integer>();
        test1.add(10); test1.add(20); test1.add(30);

        XYSeriesCollection set1 = exp.generateDataset("TEST", new int[] {1, 2, 3}, test1);
        new Chart("HEAP-1", set1, set1);
    }
}
