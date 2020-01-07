#!/usr/bin/env python3

# python the hard way exercise 13
from sys import argv

try:
    script, first, second, third = argv

    print("The script is called:", script)
    print("The first variable is:", first)
    print("The second variable is:", second)
    print("The third variable is:", third)

except ValueError:
    print("Must have three arguments")
