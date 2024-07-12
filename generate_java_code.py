import sys
from pytzdata import tz_path

# Use an obscure dependency to verify pip_parse is actually working.
tz = tz_path('America/Los_Angeles')

# Actually generate the code.
output_path = sys.argv[-1]

with open(output_path, 'w') as f:
    f.write('''\
package com.example;

public class GeneratedClass {
    public static String name() {
        return "GenerateJavaCodeWithPyPiDependency";    
    }
}''')