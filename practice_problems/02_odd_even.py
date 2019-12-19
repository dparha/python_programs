#!/usr/bin/env python3
# determines if a number is odd or even or
# checks if a number divides evenly into another number

run = 1

while run == 1:
    option = int(input("enter 1 or 2 "))

    if option == 1:

        num = int(input("enter a number: "))

        if num % 2 and num % 4:
            print("odd")
            break

        elif not num % 2 and not num % 4:
            print("even and divisible by 4")
            break

        else:
            print("even but not divisible by 4")
            break

    elif option == 2:
        num = int(input("enter first number: "))
        check = int(input("enter second number: "))

        if num % check:
            print(str(check) + " does not divide evenly into " + str(num))
            break
        else:
            print(str(check) + " divides evenly into " + str(num))
            break

    else:
        print("must enter 1 or 2\n")
