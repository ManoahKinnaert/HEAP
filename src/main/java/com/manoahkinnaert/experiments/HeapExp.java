package com.manoahkinnaert.experiments;

import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.data.xy.XYDataset;
import org.jfree.data.xy.XYSeries;
import org.jfree.data.xy.XYSeriesCollection;

import java.util.ArrayList;

public class HeapExp {
    // Helper function to generate a Dataset to be used in the charts
    public XYSeriesCollection generateDataset(String name, int[] sizes, ArrayList<Integer> data, ArrayList<Integer> dataTheoretical) {
        assert sizes.length == data.size() && data.size() == dataTheoretical.size();
        XYSeries measuredSeries = new XYSeries("Measured " + name);
        XYSeries theoreticalSeries = new XYSeries("Theoretical " + name);
        for (int i = 0; i < sizes.length; i++) {
            measuredSeries.add(sizes[i], data.get(i));
            theoreticalSeries.add(sizes[i], dataTheoretical.get(i));
        }
        XYSeriesCollection dataset = new XYSeriesCollection();
        dataset.addSeries(measuredSeries);
        dataset.addSeries(theoreticalSeries);
        return dataset;
    }
}
