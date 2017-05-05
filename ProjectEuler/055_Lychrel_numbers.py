#!/usr/bin/env python

from datetime import datetime
print datetime.now()

def Palindrome(num):
    s=list(str(num))
    s.reverse()
    s = ''.join(s)
    return int(s)

def IsLychrel(n):
    for i in range(50):
        p=Palindrome(n)
        n=p+n
        k=Palindrome(n)
        if k==n:
            return False
    return True


cnt=0
LIMIT=10000

for i in range(1,LIMIT):
    if IsLychrel(i):
        cnt+=1
        
print cnt



print datetime.now()