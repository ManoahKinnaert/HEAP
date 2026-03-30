package com.manoahkinnaert.core;

import com.manoahkinnaert.utils.Counter;

import java.util.ArrayList;

public class Array extends ArrayList<Integer> {
    private Counter counter;

    public Array() {
        super();
        counter = new Counter();
        add(1);
    }

    public void exch(int a, int b) {
        Integer obj = get(a);
        set(a, get(b));
        set(b, obj);
        counter.increaseExchanges();
        System.out.println("Exchanges: " + counter.getExchanges());
    }

    public boolean less(int a, int b) {
        counter.increaseCompares();
        System.out.println("Compares: " + counter.getCompares());
        return get(a) < get(b);
    }

    public void resetCounter() {
        counter.reset();
    }

    public Counter getCounter() {
        return counter;
    }
}
