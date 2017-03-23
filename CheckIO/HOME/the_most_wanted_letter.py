#!/usr/bin/env python
# -*- coding:utf-8 -*-  

from collections import Counter
import string

def checkio(text):
    text=text.lower()
    text=[l for l in text if l in string.lowercase]
    cnter=Counter(text)
    lm,nm='a',0
    for c in string.lowercase:
        if c in cnter:
            if cnter[c]>nm:
                nm,lm = cnter[c],c
    return lm


print checkio("Hello World!")