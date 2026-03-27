package com.manoahkinnaert.utils;

import java.util.ArrayList;

public class Array extends ArrayList<Integer> {
    Counter counter;

    public Array() {
        super();
        counter = new Counter();
    }

    public void exch(int a, int b) {
        Integer obj = get(a);
        set(a, get(b));
        set(b, obj);
        counter.increaseExchanges();
    }

    public boolean less(int a, int b) {
        counter.increaseCompares();
        return get(a) < get(b);
    }

    public void resetCounter() {
        counter.reset();
    }
}
