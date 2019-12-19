#!/usr/bin/env python3
# prints a list numbers in list less than 5

list = list(input("enter a list of integers: \n"))
new_list = []

for i in list:
    if i.isdigit() and int(i) < 5:
        new_list.append(i)
    elif not i.isdigit():
        print(i + " is not an integer")

if not new_list:
    print("No numbers less than 5")
else:
    print(new_list)
