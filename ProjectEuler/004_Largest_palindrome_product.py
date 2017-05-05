#!/usr/bin/env python

def IsPalindromic (num):
    s=list(str(num))
    s.reverse()
    s = ''.join(s)
    return int(s) == num

def LargetsPalindrome():
    p=[]
    for i in range(100,1000):
        for j in range(100, 1000):
            k=i*j
            if IsPalindromic(k):
                p.append(k)
    return max(p)

print LargetsPalindrome()
