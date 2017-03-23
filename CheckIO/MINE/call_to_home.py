#!/usr/bin/env python
# *-* coding:UTF-8 *-*
import math
def total_cost(calls):
    preday, left, ret = "", 100, 0
    for call in calls:
        (day, m, duration) = call.split(" ")
        duration = int(math.ceil(int(duration)*1.0/60))
        if day!=preday:
            preday=day
            left=100
        if duration<=left:
            ret+=duration*1
            left-=duration
        else:
            ret+=left*1+(duration-left)*2
            left=0
    return ret


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert total_cost((u"2014-01-01 01:12:13 181",
                       u"2014-01-02 20:11:10 600",
                       u"2014-01-03 01:12:13 6009",
                       u"2014-01-03 12:13:55 200")) == 124, "Base example"
    assert total_cost((u"2014-02-05 01:00:00 1",
                       u"2014-02-05 02:00:00 1",
                       u"2014-02-05 03:00:00 1",
                       u"2014-02-05 04:00:00 1")) == 4, "Short calls but money..."
    assert total_cost((u"2014-02-05 01:00:00 60",
                       u"2014-02-05 02:00:00 60",
                       u"2014-02-05 03:00:00 60",
                       u"2014-02-05 04:00:00 6000")) == 106, "Precise calls"
