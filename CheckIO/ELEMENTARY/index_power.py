#!/usr/bin/env python
# -*- coding:utf-8 -*- 
def index_power(array, n):
    """
        Find Nth power of the element with index N.
    """
    return -1 if n>=len(array) else pow(array[n],n)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"