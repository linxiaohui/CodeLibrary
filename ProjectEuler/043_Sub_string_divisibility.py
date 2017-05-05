#!/usr/bin/env python

from datetime import datetime
print datetime.now()

import itertools
import math

digits=range(0,10)


s=0

it = itertools.permutations(digits, 3)
for (d8,d9,d10) in it:
    if (100*d8+10*d9+d10)%17==0:
        digits7=list(digits)
        digits7.remove(d8)
        digits7.remove(d9)
        digits7.remove(d10)
        it7 = itertools.permutations(digits7, 3)
        for (d5,d6,d7) in it7:
            if (100*d7+10*d8+d9)%13==0 and (100*d6+10*d7+d8)%11==0 and (100*d5+10*d6+d7)%7==0:
                digits4=list(digits7)
                digits4.remove(d5)
                digits4.remove(d6)
                digits4.remove(d7)
                it4 = itertools.permutations(digits4, 3)
                for (d2,d3,d4) in it4:
                    if(100*d4+10*d5+d6)%5==0 and (100*d3+10*d4+d5)%3==0 and (100*d2+10*d3+d4)%2==0:
                        digits1=list(digits4)
                        digits1.remove(d2)
                        digits1.remove(d3)
                        digits1.remove(d4)
                        d1=digits1[0]
                        if d1!=0:
                            number=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10]
                            print number
                            s+=int(''.join(map(str,number))) 

print s

print datetime.now()