#!/usr/bin/env python

from datetime import datetime
print datetime.now()

data=open("p022_names.txt").read()
def NameScore(name):
    score=0
    for c in name:
        score+=ord(c)-ord('A')+1
    return score

names=eval("["+data+"]")
names.sort()
print names.index('COLIN')
size=len(names)
i=0
s=0
while i<size:
    s+=(i+1)*NameScore(names[i])
    i+=1

print s   

print datetime.now()