package com.manoahkinnaert.core;

public class Heap extends Array {

    public Heap() {
        super();
    }

    // heap swim operation
    private void swim(int k) {
        while (k > 1 && less(k / 2, k)) {
            exch(k, k / 2);
            k = k / 2;
        }
    }

    // heap sink operation
    private void sink(int k) {
        final int n = size();
        while (2 * k <= n) {
            int j = 2 * k;
            if (j < n && less(j, j + 1)) j++;
            if (!less(k, j)) break;
            exch(k, j);
            k = j;
        }
    }

    public void insert(int a) {
        add(a);
        swim(size() - 1);
    }

    public int delMax() {
        int n = size();
        int max = get(1);
        exch(1, n);
        remove(n);
        sink(1);
        return max;
    }
}
