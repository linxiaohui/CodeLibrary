#!/usr/bin/env python

from datetime import datetime
print datetime.now()

CNT=1
for a in range(200/100+1):
    cur=a*100
    if cur==200: CNT+=1
    if cur>=200: break
    for b in range(200/50+1):
        cur2=cur+b*50
        if cur2==200: CNT+=1
        if cur2>=200:  break
        for c in range(200/20+1):
            cur3=cur2+c*20
            if cur3==200: CNT+=1
            if cur3>=200: break
            for d in range(200/10+1):
                cur4=cur3+d*10
                if cur4==200: CNT+=1
                if cur4>=200: break
                for e in range(200/5+1):
                    cur5=cur4+e*5
                    if cur5==200: CNT+=1
                    if cur5>=200: break
                    for f in range(200/2+1):
                        cur6=cur5+f*2
                        if cur6==200: CNT+=1
                        if cur6>=200: break
                        for g in range(200/1+1):
                            cur7=cur6+g*1
                            if cur7==200: CNT+=1
                            if cur7>=200: break        

print CNT

print datetime.now()
