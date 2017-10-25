# -*- coding: utf-8 -*-

import zerorpc

class Services:
    def Hello(self, name):
        return "Hello [{}]".format(name)
    def inc(self, n):
        return n + 1

s = zerorpc.Server(Services())
s.bind("tcp://0.0.0.0:1234")
s.run()