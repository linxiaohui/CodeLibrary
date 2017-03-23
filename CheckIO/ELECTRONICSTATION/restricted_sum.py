#!/usr/bin/env python
# *-* coding:UTF-8 *-*

# The list of banned words are as follows: sum,import,for,while,reduce

def AddList(l):
    if len(l)==0:
        return 0
    else:
        return l[0]+AddList(l[1:])
def checkio(data):
    return AddList(data)