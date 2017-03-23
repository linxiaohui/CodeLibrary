#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def PE004():
    M=0
    for i in range(100,10000):
        for j in range(i+1,1000):
            k=i*j
            #if k==int(str(k)[::-1]) and k>M :
            if k>M and k==int(str(k)[::-1]) :
                M=k
    print M

print timeit.timeit(PE004, number=1)
