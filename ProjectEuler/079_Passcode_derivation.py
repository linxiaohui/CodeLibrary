#!/usr/bin/env python

from datetime import datetime
print datetime.now()

data=open("p079_keylog.txt").read().split('\n')

edge=set()

for d in data:
    a1,a2,a3=list(d)
    edge.add((a1,a2))
    edge.add((a2,a3))

graph={}
vertex=set()
queue=[]

for (x,y) in edge:
    vertex.add(x)
    vertex.add(y)
    if x in graph:
        graph[x].add(y)
    else:
        graph[x]=set()
        graph[x].add(y)

def Degree(n):
    cnt=0
    for a in graph:
        if n in graph[a]:
            cnt+=1
    return cnt

for v in vertex:
    if Degree(v)==0:
        queue.append(v)

path=[]
while len(queue)!=0:
    v=queue.pop(0)
    path.append(v)
    if v in graph:
        del graph[v]
    vertex.remove(v)
    for v in vertex:
        if Degree(v)==0:
            queue.append(v)

print ''.join(path)

print datetime.now()