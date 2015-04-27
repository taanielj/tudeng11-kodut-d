#!/usr/bin/env python3

__author__ = "Taaniel Jakobson"
__version__ = "0.0002a"
import os

def fib(n):                                     
    a, b = 0, 1
    fib_number = []
    while b < n:
        a, b = b, a+b
        fib_number.append(b)
    return fib_number

def main():
    print("write Fibonacci series up to n")
    n = int(input("n="))
    output = fib(n)
    text_file = open("output.txt", "w")
    text_file.write(str(output))
    text_file.close()
    return(output)
if __name__ == "__main__":
    main()