#!/usr/bin/env python

def SumEvenFibonacciNumbers(limit):
    i,j=1,2
    s=2
    n=i+j
    while n <= limit:
        s+= n if n%2==0 else 0
        i,j=j,n
        n=i+j
    return s

print SumEvenFibonacciNumbers(4000000)
