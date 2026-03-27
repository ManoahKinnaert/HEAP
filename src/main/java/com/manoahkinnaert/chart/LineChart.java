package com.manoahkinnaert.chart;

import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;
import org.jfree.ui.ApplicationFrame;

import java.awt.*;

public class LineChart extends ApplicationFrame {
    public LineChart(String winTitle, DefaultCategoryDataset compares, DefaultCategoryDataset exchanges) {
        super(winTitle);
        JFreeChart comparesChart = ChartFactory.createLineChart(
                "Compares",
                "N",
                "Compares",
                compares,
                PlotOrientation.VERTICAL,
                true, true, false
        );

        JFreeChart exchangesChart;
        if (exchanges != null) {
            exchangesChart = ChartFactory.createLineChart(
                    "Exchanges",
                    "N",
                    "Exchanges",
                    exchanges,
                    PlotOrientation.VERTICAL,
                    true, true, false
            );
        }
        ChartPanel comparesPanel = new ChartPanel(comparesChart);
        comparesPanel.setPreferredSize(new Dimension(600, 600));
        setContentPane(comparesPanel);
    }

    // TODO: To be implemented
    public void convertToImage() {
    }
}
