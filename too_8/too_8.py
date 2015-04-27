#!/usr/bin/env python3

__author__ = "Taaniel Jakobson"
__version__ = "0.0002a"
import os

def fib(n):                                     #Generate fibonacci number upto n
    a, b = 0, 1
    fib_number = []                             #Create empty list to hold fibonacci numbers
    while b < n:
        a, b = b, a+b                           #Calculate next fib number...
        fib_number.append(b)                    #... and add it to the list
    return fib_number                           #returns list of fibonacci numbers

def main():
    print("write Fibonacci series up to n")
    n = int(input("n="))
    output = fib(n)
    text_file = open("output.txt", "w")
    text_file.write(str(output))
    text_file.close()
    print(output)
    return(output)
if __name__ == "__main__":
    main()
