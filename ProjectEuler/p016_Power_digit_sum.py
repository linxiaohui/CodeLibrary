#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def P016():
    print reduce(lambda x,y:x+y, map(lambda x:int(x), str(pow(2,1000))))

print timeit.timeit(P016, number=1)
