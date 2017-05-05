#!/usr/bin/env python


def FindPrime(ith):
    primes=[2, 3]
    number=primes[-1]+2
    plen=len(primes)
    while plen<ith:
        c=False
        for p in primes:
            if number%p==0:
                c=True
                break
        if not c:
            primes.append(number)
            plen+=1
        number+=2
    return primes[-1]

print FindPrime(10001)
