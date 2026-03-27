package com.manoahkinnaert.core;

import com.manoahkinnaert.utils.Array;

public class Heap extends Array {

    public Heap() {
        super();
    }

    // heap swim operation
    private void swim(int k) {
        while (k > 1 && less(k, k / 2)) {
            exch(k, k / 2);
            k = k / 2;
        }
    }

    public void insert(int a) {
        int n = size();
        add(++n, a);
        swim(n);
    }
}
