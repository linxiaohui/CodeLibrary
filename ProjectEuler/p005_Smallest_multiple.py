#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def PE005():
    def LCM(a,b):
        def GCD(a,b):
            if a%b==0:
                return b
            else:
                return GCD(b,a%b)
        if a<b:
            a,b=b,a
        return a*b/GCD(b,a)
    print reduce(lambda x,y:LCM(x,y), range(2,21))

print timeit.timeit(PE005, number=1)
