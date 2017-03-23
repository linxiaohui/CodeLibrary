#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def P014():
    collatz=[0]*(1000000+1)
    collatz[1]=1
    def Collatz(k):
        r=1
        n=k
        while n!=1:
            if n%2==0:
                n=n/2
                if n<1000000 and collatz[n]!=0:
                    collatz[k]=collatz[n]+r
                    return collatz[k]
            else:
                n=3*n+1
                if n<1000000 and collatz[n]!=0:
                    collatz[k]=collatz[n]+r
                    return collatz[k]
            r+=1
        collatz[k]=r
        return r
    longest=(1,1)
    for i in range(2,1000000+1):
        l=Collatz(i)
        if l>longest[0]:
            longest=(l,i)
    print longest[1]

print timeit.timeit(P014, number=1)
