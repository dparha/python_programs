#!/usr/bin/env python3
# list comprehension example

print([x for x in input("Enter numbers: ") if x.isdigit() and int(x) < 5])
