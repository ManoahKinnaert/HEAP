package com.manoahkinnaert.utils;

public class Counter {
    private int compares;

    public Counter() {
        compares = 0;
    }

    public int getCompares() {
        return compares;
    }

    public void increaseCompares() {
        compares += 1;
    }

    public void reset() {
        compares = 0;
    }
}
