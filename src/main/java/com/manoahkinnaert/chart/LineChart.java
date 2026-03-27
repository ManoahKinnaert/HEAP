package com.manoahkinnaert.chart;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;

import javax.swing.*;
import java.awt.*;

public class LineChart extends JFrame {

    public LineChart(String winTitle, DefaultCategoryDataset comparesData, DefaultCategoryDataset exchangesData) {
        super(winTitle);

        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        // 1 row and 2 cols for side by side compares and exchanges
        JPanel chartPanelGroup = new JPanel(new GridLayout(1, 2));

        // Create compares chart
        JFreeChart comparesChart = ChartFactory.createLineChart("Compares", "N", "Compares", comparesData, PlotOrientation.VERTICAL, true, true, false);
        chartPanelGroup.add(new ChartPanel(comparesChart));

        // Create exchanges chart
        JFreeChart exchanges = ChartFactory.createLineChart("Exchanges", "N", "Exchanges", exchangesData, PlotOrientation.VERTICAL, true, true, false);
        chartPanelGroup.add(new ChartPanel(exchanges));

        add(chartPanelGroup);
        pack();
        setSize(1000, 700);
        setLocationRelativeTo(null);
        setVisible(true);
    }
}
