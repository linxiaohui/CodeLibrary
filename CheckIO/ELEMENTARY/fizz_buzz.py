#!/usr/bin/env python
# -*- coding:utf-8 -*- 

def checkio(number):
	return " ".join(["Fizz" if number%3==0 else "","Buzz" if number%5==0 else ""]).strip() or str(number)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio(15)
    print checkio(6)
    print checkio(5)
    print checkio(7)
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"