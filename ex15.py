#!/usr/bin/env python3

# python the hard way exercise 15
from sys import argv

try:
    script, filename = argv

    txt = open(filename)

    print(f"Here's your file {filename}:")
    print(txt.read())

    print("Type the filename again:")
    file_again = input("> ")

    txt_again = open(file_again)

    print(txt_again.read(), end='')

except ValueError:
    print("Must enter filename")
