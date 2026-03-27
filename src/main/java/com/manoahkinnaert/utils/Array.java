package com.manoahkinnaert.utils;

import java.util.ArrayList;

public class Array extends ArrayList<Integer> {

    public Array() {
        super();
    }

    public void exch(int a, int b) {
        Integer obj = get(a);
        set(a, get(b));
        set(b, obj);
    }

    public boolean less(int a, int b) {
        return get(a) < get(b);
    }
}
