#!/usr/bin/env python
# -*- coding:utf-8 -*-  

def check_connection(network, first, second):
	label={}
	mark=0
	for e in network:
		e1,e2=e.split("-")
		if e1 not in label:
			label[e1]=mark
			mark+=1
		if e2 not in label:
			label[e2]=mark
			mark+=1
	graph=[[0]*mark for i in range(mark)]
	for _ in range(mark):
		graph[_][_]=1
	for e in network:
		e1,e2=e.split("-")
		graph[label[e1]][label[e2]]=1
		graph[label[e2]][label[e1]]=1
	matrix=[[0]*mark for i in range(mark)]
	for i in range(mark):
		for j in range(mark):
			matrix[i][j]=graph[i][j]
	for _ in range(mark):
		for i in range(mark):
			for j in range(mark):
				if matrix[i][j]==0:
					for k in range(mark):
						matrix[i][j]+=matrix[i][k]*graph[k][j]
	return matrix[label[first]][label[second]]>0 or matrix[label[second]][label[first]]>0

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
