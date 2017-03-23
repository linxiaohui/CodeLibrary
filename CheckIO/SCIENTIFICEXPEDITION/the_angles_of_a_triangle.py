#!/usr/bin/env python
# *-* coding:UTF-8 *-*

from math import acos
from math import pi
def checkio(a, b, c):
    e=[a,b,c]
    e.sort()
    a,b,c=e
    if a+b<=c:
        return [0,0,0]
    cosC=1.0*(a*a+b*b-c*c)/(2*a*b)
    cosA=1.0*(b*b+c*c-a*a)/(2*b*c)
    cosB=1.0*(a*a+c*c-b*b)/(2*a*c)
    A=int(round(acos(cosA)*180/pi,0))
    B=int(round(acos(cosB)*180/pi,0))
    C=int(round(acos(cosC)*180/pi,0))
    return [A,B,C]

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"