#!/usr/bin/env python

from datetime import datetime
print datetime.now()

data=open("p067_triangle.txt").readlines()

tri=[]
for _ in data:
    tri.append(map(int, _.split(" ")))

for i in range(1,len(tri)):
    dlen = len(tri[i])
    for j in range(dlen):
        m1=tri[i-1][j-1] if j>0 else 0
        m2=tri[i-1][j] if j<dlen-1 else 0
        tri[i][j]+=max(m1,m2)

print max(tri[-1])


print datetime.now()