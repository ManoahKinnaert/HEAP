package com.manoahkinnaert.core;

import com.manoahkinnaert.utils.Counter;

import java.util.ArrayList;

public class Array extends ArrayList<Integer> {
    private Counter counter;

    public Array() {
        super();
        counter = new Counter();
    }

    public void exch(int a, int b) {
        Integer obj = get(a);
        set(a, get(b));
        set(b, obj);
    }

    public boolean less(int a, int b) {
        counter.increaseCompares();
        return get(a) < get(b);
    }

    public void resetCounter() {
        counter.reset();
    }

    public Counter getCounter() {
        return counter;
    }
}
