#!/usr/bin/python3

def fizzbuzz():
    # Loop from 1 to 100
    for i in range(1, 101):
        # Check if the number is a multiple of both three and five
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        # Check if the number is a multiple of three
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # Check if the number is a multiple of five
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

