#!/usr/bin/env python3

__author__ = "Taaniel Jakobson"
__version__ = "0.0001a"
import os
from sys import argv



def main():
    def fib(n):    # write Fibonacci series up to n
        a, b = 0, 1
        text_file = open("output.txt", "w")
        while b < n:
            print(b)
            text_file.write(str(b))
            text_file.write("\n")
            a, b = b, a+b
        text_file.close()   
    print("write Fibonacci series up to n")
    n = int(input("n="))
    fib(n)
if __name__ == "__main__":
    main()
