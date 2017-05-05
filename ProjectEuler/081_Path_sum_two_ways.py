#!/usr/bin/env python

from datetime import datetime
print datetime.now()

data=open("p081_matrix.txt").readlines()
matrix=[]
for _ in data:
    matrix.append(map(int,_.split(",")))

for _ in range(1,len(matrix)):
    matrix[_][0]+=matrix[_-1][0]

for _ in range(1,len(matrix[0])):
    matrix[0][_]+=matrix[0][_-1]
    
for i in range(1,len(matrix)):
    for j in range(1,len(matrix[i])):
        m1=0
        if j>0:
            m1=matrix[i][j-1]
        m2=0
        if i>0:
            m2=matrix[i-1][j]
        matrix[i][j]+=min(m1,m2)

print matrix[-1][-1]
print datetime.now()