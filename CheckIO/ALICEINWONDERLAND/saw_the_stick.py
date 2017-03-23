#!/usr/bin/env python
# -*- coding:utf-8 -*- 

#0<number<1000
SIZE=50
triangulars=[n*(n+1)/2 for n in range(SIZE)]
sums=[0]*SIZE
for i in range(1,SIZE):
    sums[i]=triangulars[i]+sums[i-1]

def checkio(number):
    if number>=1000:
        return []
    MAX=None
    I=None
    J=None
    for i in range(SIZE):
        for j in range(i,SIZE):
            if sums[j]-sums[i]==number:
                if MAX is None or j-i>MAX:
                    MAX=j-i
                    I=i
                    J=j
    if MAX is None:
        return []
    else:
        return triangulars[I+1:J+1]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
