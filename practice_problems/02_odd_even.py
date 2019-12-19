#!/usr/bin/env python3
# determines if a number is odd or even or
# checks if a number divides evenly into another number


option = int(input("enter 1 or 2 "))

if option == 1:

    num = int(input("enter a number: "))

    if num % 2 and num % 4:
        print("odd")

    elif not num % 2 and not num % 4:
        print("even and divisible by 4")

    else:
        print("even but not divisible by 4")

elif option == 2:
    num = int(input("enter first number: "))
    check = int(input("enter second number: "))

    if num % check:
        print(str(check) + " does not divide evenly into " + str(num))
    else:
        print(str(check) + " divides evenly into " + str(num))
else:
    print("must enter 1 or 2")
