#!/usr/bin/env python
# *-* coding:UTF-8 *-*

FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
	assert 0<number<1000, "cannot deal with number ge 1000"
	res=""
	unit=number%10
	number/=10
	tened=number%10
	number/=10
	hundred=number%10
	if hundred!=0:
		res=res+FIRST_TEN[hundred-1]+" hundred "
	if tened==1:
		res=res+SECOND_TEN[unit]+" "
	elif tened>=2:
		res=res+OTHER_TENS[tened-2]+" "
	if unit!=0 and tened!=1:
		res=res+FIRST_TEN[unit-1]
	return res.strip()


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"