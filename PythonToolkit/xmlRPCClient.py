# -*- coding: utf-8 -*-

import time

try:
    from xmlrpclib import ServerProxy
except:
    from xmlrpc.client import ServerProxy

s = ServerProxy("http://127.0.0.1:1234")

print(s.Hello("World"))
print(s.inc(100))

CNT=100
start=time.time()
for i in range(CNT):
    s.Hello("World")
end=time.time()
print(CNT/(end-start))
start=time.time()
for i in range(CNT):
    s.inc(123)
end=time.time()
print(CNT/(end-start))
