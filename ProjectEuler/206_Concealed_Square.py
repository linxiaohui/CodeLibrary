#!/usr/bin/env python
from datetime import datetime
print datetime.now()


import math

least=int(math.sqrt(1020304050607080900))/100
most =int(math.sqrt(1929394959697989990))/100

def Check(sq):
    s=str(sq)
    if s[2]!='2':return False
    if s[4]!='3':return False
    if s[6]!='4':return False
    if s[8]!='5':return False
    if s[10]!='6':return False
    if s[12]!='7':return False
    if s[14]!='8':return False
    return True

i=least
while i<=most:
    n=100*i+30
    if Check(n*n):
        print n,n*n
        break
    n=100*i+70
    if Check(n*n):
        print n,n*n
        break
    i+=1

print datetime.now()