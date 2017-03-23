#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit
def P006():
    print sum(range(101))**2-sum([i**2 for i in range(101)])

print timeit.timeit(P006,number=1)
