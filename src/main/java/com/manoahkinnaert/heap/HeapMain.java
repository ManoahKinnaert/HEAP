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
        while (true) {
            int testNum = Integer.parseInt(readLine("Which test would you like to run (1-3)?"));
            // TODO: run the desired experiment...
            String cmd = readLine("Would you like to exit?");
            if (cmd.equalsIgnoreCase("y")) break;
        }
    }
}
