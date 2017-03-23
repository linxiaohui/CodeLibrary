#!/usr/bin/env python
# *-* coding:UTF-8 *-*

import socket
import struct
def checkio(data):
	ips=[]
	for d in data:
		_=bin(struct.unpack("!I",socket.inet_aton(d))[0])[2:]
		ips.append("0"*(32-len(_))+_)
	if len(ips)==0:
		return ""
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
	return socket.inet_ntoa(struct.pack("!I",int("".join(res),2)))+"/"+str(bit)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.16.14.0", "172.16.15.0"]) == "172.16.12.0/22"), "First Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9"]) == "172.0.0.0/8"), "Second Test"
    assert (checkio(["172.16.12.0", "172.16.13.0", "172.155.43.9", "146.11.2.2"]) == "128.0.0.0/2"), "Third Test"