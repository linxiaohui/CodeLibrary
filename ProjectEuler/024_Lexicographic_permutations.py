#!/usr/bin/env python

from datetime import datetime
print datetime.now()

source=range(10)
cnt = [1]*11
cnt[1]=1
for _ in range(2,11):
    cnt[_]=_*cnt[_-1]

print cnt

result=[]
LIMIT=1000000
for i in range(10,0,-1):
    if LIMIT == cnt[i] or LIMIT==0:
        source.sort(reverse=True)
        break
    if LIMIT <= cnt[i-1]:
        result.append(str(source[0]))
        source.remove(source[0])
        source.sort()
    else:
        result.append(str(source[(LIMIT-1)/cnt[i-1]]))
        source.remove(source[(LIMIT-1)/cnt[i-1]])
        source.sort()
        LIMIT%=cnt[i-1]

for _ in source:
    result.append(str(_))

print ''.join(result)

print datetime.now()
