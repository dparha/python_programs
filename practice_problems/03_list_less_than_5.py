#!/usr/bin/env python3
# prints numbers in list less than 5

list = list(input("enter a list of integers: \n"))

for i in list:
    if i.isdigit() and int(i) < 5:
        print(i)
    elif not i.isdigit():
        print(i + " is not an integer")
