#!/usr/bin/env python
# *-* coding:UTF-8 *-*

from datetime import date
from datetime import timedelta

def checkio(from_date, to_date):
    tm=(to_date-from_date).days+1
    s=0
    for i in range(0,tm%7):
        d=to_date-timedelta(i)
        if d.weekday()==5 or d.weekday()==6:
            s+=1
    return s+tm//7*2


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"
