#!/bin/python

from collections import Counter

data=open("02.data").read()

cnt=Counter(data)

print(cnt)

for c in cnt:
	print((c,cnt[c]))

for c in data:
	if cnt[c]==1:
		print(c,sep='',end='')