#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def P014():
    def Collatz(n):
        r=1
        while n!=1:
            if n%2==0:
                n=n/2
            else:
                n=3*n+1
            r+=1
        return r
    longest=(1,1)
    for i in range(2,1000000+1):
        l=Collatz(i)
        if l>longest[0]:
            longest=(l,i)
    print longest[1]

print timeit.timeit(P014, number=1)