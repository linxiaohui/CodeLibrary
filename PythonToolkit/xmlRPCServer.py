# -*- coding: utf-8 -*-

try:
    from xmlrpc.server import SimpleXMLRPCServer
except:
    from SimpleXMLRPCServer import SimpleXMLRPCServer

try:
    from socketserver import ThreadingMixIn #,ForkingMixIn
except:
    from SocketServer import ThreadingMixIn #,ForkingMixIn

class ServiceServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

def Hello(name):
    return "Hello [{}]".format(name)

def inc(n):
    return n + 1

#s = SimpleXMLRPCServer(('0.0.0.0',1234))
s = ServiceServer(('0.0.0.0',1234))
s.register_function(Hello)
s.register_function(inc)
s.serve_forever()

