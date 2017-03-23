#!/usr/bin/env python
# -*- coding:utf-8 -*-
LIMIT=4000000

def genFib(limit):
     a,b=0,1
     while a+b<limit:
         a,b=b,a+b
         if b%2==0:
             yield b
print sum(list(genFib(LIMIT)))
