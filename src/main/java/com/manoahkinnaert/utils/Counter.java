package com.manoahkinnaert.utils;

public class Counter {
    private int compares;
    private int exchanges;

    public Counter() {
        compares = 0;
        exchanges = 0;
    }

    public int getCompares() {
        return compares;
    }

    public int getExchanges() {
        return exchanges;
    }

    public void increaseCompares() {
        compares += 1;
    }

    public void increaseExchanges() {
        exchanges += 1;
    }

    public void reset() {
        compares = 0;
        exchanges = 0;
    }
}
