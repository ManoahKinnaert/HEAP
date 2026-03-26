package com.manoahkinnaert.heap;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class HeapMain {

    private static String readLine(String message) {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(message);
        try {
            return reader.readLine();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) throws IOException {
        String test = readLine("test");
        System.out.println(test);
    }
}
