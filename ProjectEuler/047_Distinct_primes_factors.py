#!/usr/bin/env python
from datetime import datetime
print datetime.now()

import sympy

n=2*3*5*7

while True:
    if len(sympy.factorint(n))==4:
        if len(sympy.factorint(n+1))==4:
            if len(sympy.factorint(n+2))==4:
                if len(sympy.factorint(n+3))==4:
                    print n
                    break
                else:
                    n+=4
            else:
                n+=3
        else:
            n+=2
    else:
        n+=1

print datetime.now()