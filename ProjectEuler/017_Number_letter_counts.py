#!/usr/bin/env python

from datetime import datetime
print datetime.now()

DICT={1:"one",2:"two",3:"three",4:"four",
      5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
      11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",
      16:"sixteen", 17:"seventeen",18:"eighteen",19:"nineteen",
      20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",
      70:"seventy",80:"eighty",90:"ninety" }

def MakeWord(i):
    if i in DICT:
        return DICT[i]
    elif i<100:
        t=i/10
        o=i%10
        return DICT[t*10]+" "+DICT[o]
    elif i<1000:
        h=i/100
        cnt = DICT[h]+" hundred"
        if i%100!=0:
            return cnt+" and "+MakeWord(i%100)
        else:
            return cnt
    else:
        return "one thounsand"

def WordCharCount(i):
    if i in DICT:
        X=DICT[i].replace(' ','')
        return len(X)
    elif i<100:
        t=i/10
        o=i%10
        return len(DICT[t*10])+len(DICT[o])
    elif i<1000:
        h=i/100
        cnt = len(DICT[h])+len("hundred")
        if i%100!=0:
            return cnt+len("and")+WordCharCount(i%100)
        else:
            return cnt
    else:
        return len("onethousand")

cnt=0
for i in range(1,1000+1):
    cnt+=WordCharCount(i)

print MakeWord(42)
print MakeWord(15)
print MakeWord(342)
print MakeWord(115)

print cnt
print datetime.now()