#!/usr/bin/env python
# -*- coding:utf-8 -*-
import timeit

def P015():
    LIMIT=20
    def C(m,n):
        return reduce(lambda x,y:x*y, range(1,m+1))/(reduce(lambda x,y:x*y, range(1,n+1))*reduce(lambda x,y:x*y, range(1,m-n+1)))
    print C(LIMIT*2,LIMIT)

print timeit.timeit(P015, number=1)
