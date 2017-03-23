#!/usr/bin/env python
# -*- coding:utf-8 -*- 

O=[0]*10001
AGE=[0]*5000
AGE[0]=10000
def GenFib(m):
	a,b=1,1
	while a<m:
		yield a
		a, b = b, a+b
fiblt5000=[x for x in GenFib(5000)]

for i in range(1,5000):
	if i in fiblt5000:
		AGE[i]=AGE[i-1]-i
	else:
		AGE[i]=AGE[i-1]+1

for i in range(0,5000):
	O[AGE[i]]=i

def checkio(opacity):
	return O[opacity]

if __name__ == '__main__':
	assert checkio(9990) == 5,"5"
