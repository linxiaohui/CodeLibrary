#!/usr/bin/env python

from datetime import datetime
print datetime.now()

import operator 
def C(n, k):
    if k>n:
        return 1
    return  reduce(operator.mul, range(n - k + 1, n + 1))/reduce(operator.mul, range(1, k +1))

print C(20+20,20)

print datetime.now()