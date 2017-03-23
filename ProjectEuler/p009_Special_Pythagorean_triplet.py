#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def P009():
    for a in range(1,333):
        for b in range(a+1,666):
            if b<1000-a-b and a*a+b*b==(1000-a-b)**2:
                print a*b*(1000-a-b)
                break

print timeit.timeit(P009, number=1)
