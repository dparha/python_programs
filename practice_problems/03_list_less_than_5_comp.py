#!/usr/bin/env python3
# list comp prints a list numbers in list less than 5


print([x for x in input("enter integers:\n") if x.isdigit() and int(x) < 5])
