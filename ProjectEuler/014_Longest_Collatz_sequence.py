#!/usr/bin/env python

from datetime import datetime
print datetime.now()

LIMIT=1000000

def CollatzSequence(LIMIT):
    Collatz=[0]*(LIMIT+1)
    for i in range(2, LIMIT+1):
        cnt = 0
        n = i
        while n!=1:
            if n%2==0:
                n=n/2
            else:
                n=n*3+1
            cnt+=1
            if 1<n<i:
                Collatz[i] = Collatz[n]+cnt
                break
        if Collatz[i]==0:
            Collatz[i]=cnt
    #print  zip(range(len(Collatz)), Collatz)
    MAX=0
    INDEX=0
    for _ in range(2, LIMIT+1):
        if  Collatz[_]>MAX:
            MAX=Collatz[_]
            INDEX=_
    print MAX
    return INDEX

print CollatzSequence(13)
  
print CollatzSequence(1000000)

print datetime.now()