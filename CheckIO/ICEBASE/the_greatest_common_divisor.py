#!/usr/bin/env python
# *-* coding:UTF-8 *-*

def gcd(a,b):
    if b>a:
        a,b=b,a
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)

def greatest_common_divisor(*args):
    return reduce(lambda x,y:gcd(x,y), args)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"