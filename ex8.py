#!/usr/bin/env python3

# python the hard way exercise 8

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "There are",
    "no scraps",
    "in my scrapbook\n\n",
    "\t\t\t- Phil Leatardo"
    ))
