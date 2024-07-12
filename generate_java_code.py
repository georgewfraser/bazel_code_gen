#!/usr/bin/env python3
import sys

output_path = sys.argv[1]

with open(output_path, 'w') as f:
    f.write('''\
package com.example;

public class GeneratedClass {
    public static String name() {
        return "GeneratedCode";    
    }
}''')