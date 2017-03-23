#!/usr/bin/env python
# *-* coding:UTF-8 *-*

ip2int = lambda ip: reduce(lambda a, b: (a << 8) + b, map(int, ip.split('.')), 0)
int2ip = lambda n: '.'.join([str(n >> (i << 3) & 0xFF) for i in range(0, 4)[::-1]])

from pprint import pprint

def checkio(data):
	ips=[]
	for d in data:
		_=bin(ip2int(d))[2:]
		ips.append("0"*(32-len(_))+_)
	if len(ips)==0:
		return ""
	pprint(ips)
	res=[]
	cont=True
	for i in range(0,32):
		for j in range(1,len(ips)):
			if ips[j][i]!=ips[0][i]:
				cont=False
				break
		else:
			res.append(ips[0][i])
		if cont==False:
			break
	bit=len(res)
	res.extend(["0"]*(32-bit))
	return int2ip(int("".join(res),2))+"/"+str(bit)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"