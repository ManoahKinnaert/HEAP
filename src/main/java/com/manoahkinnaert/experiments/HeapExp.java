package com.manoahkinnaert.experiments;

import org.jfree.data.category.DefaultCategoryDataset;

import java.util.ArrayList;

public class HeapExp {
    // Helper function to generate a Dataset to be used in the charts
    public DefaultCategoryDataset generateDataset(String name, int[] sizes, ArrayList<Integer> data, ArrayList<Integer> dataTheoretical) {
        DefaultCategoryDataset dataset = new DefaultCategoryDataset();
        assert sizes.length == data.size() && data.size() == dataTheoretical.size();
        for (int i=0; i < data.size(); i++) {
            // Measured data
            dataset.addValue(sizes[i], "Measured: " + name, data.get(i));
            // Expected theoretical data
            dataset.addValue(sizes[i], "Expected: " + name, dataTheoretical.get(i));
        }
        return dataset;
    }
}
