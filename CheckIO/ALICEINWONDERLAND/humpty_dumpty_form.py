#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# https://en.wikipedia.org/wiki/Spheroid
import math
def checkio(height, width):
    S=0
    V=0
    if height<width:
        e2=1.0-(1.0*height*height/(1.0*width*width))
        e=math.sqrt(e2)
        S=math.pi*width*width*(1+(1.0-e2)/e*math.atanh(e))/2
    elif height>width:
        e2=1.0-(width*width*1.0/(1.0*height*height))
        e=math.sqrt(e2)
        S=math.pi*width*width*(1+height/(width*e)*math.asin(e))/2
    else:
        S=math.pi*width*width
    V=math.pi/6.0*width*width*height
    return [round(V,2), round(S,2)]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 2) == [8.38, 21.48], "Prolate spheroid"
    assert checkio(2, 2) == [4.19, 12.57], "Sphere"
    assert checkio(2, 4) == [16.76, 34.69], "Oblate spheroid"