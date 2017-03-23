#!/usr/bin/env python
# -*- coding:utf-8 -*- 
def checkio(array):
    """
        sums even-indexes elements and multiply at the last
    """
    return len(array)!=0 and sum([array[i] for i in range(len(array)) if i%2==0])*array[-1] or 0

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
