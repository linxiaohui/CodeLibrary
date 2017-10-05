# -*- coding: utf-8 -*-
# Python 3.6

import struct
from io import BytesIO
from collections import namedtuple
from gevent import socket
from gevent.server import DatagramServer

Hex = lambda x : '0x{0:04x}'.format(x) # Hex(256) => "0x0100"

QueryResult = namedtuple("DnsQuery",
                 "transactionID,flags,questions,answerRrs, authorityRrs,additionalRrs,qname,qtype,qclass"
)

LOCALDNS = ("219.239.26.42",53)

Hosts = {
    b"d3c33hcgiwev3.cloudfront.net":b"52.84.246.90"
}


def udp_send(address,data):
    sock = socket.socket(type=socket.SOCK_DGRAM)
    sock.connect(address)
    sock.send(data)
    response, address = sock.recvfrom(8192*4)
    return response,address

class DnsParser:
    '''参考 DNS协议报文格式'''
    @classmethod
    def parseQuery(self,query):
        # ! network (= big-endian) 
        # H unsigned short
        transactionID,flags,questions,answerRrs,authorityRrs,additionalRrs = map(Hex,struct.unpack("!6H",query[:12]))
        quries = BytesIO(query[12:])
        c = struct.unpack("!c",quries.read(1))[0]
        domain = []
        while  c != b'\x00':
            n = ord(c)
            domain.append(b''.join(struct.unpack("!%sc" % n,quries.read(ord(c)))))
            c = struct.unpack("!c",quries.read(1))[0]
        domain = b'.'.join(domain)
        qtype,qclass = map(Hex,struct.unpack("!2H",quries.read()))
        return QueryResult(transactionID,flags,questions,answerRrs,
                            authorityRrs,additionalRrs,domain,qtype,qclass)

    @classmethod
    def generateReqponse(self,queryData,ip):
        """
        only support ipv4
        """
        return b''.join([queryData[:2],b"\x81\x80\x00\x01\x00\x02\x00\x00\x00\x00",
          queryData[12:],b"\xc0\x0c",b"\x00\x01",b"\x00\x01",b"\x00\x00\x00\x1e",b"\x00\x04",
          struct.pack('BBBB',*map(int,ip.split(b'.')))
          ])

class DnsServer(DatagramServer):
    def handle(self,data,address):
        query = DnsParser.parseQuery(data)
        print("get dns query from %s,query:%s" %(str(address),str(query.qname)))
        find = False
        if query.qname in Hosts:
            find = True
            ip = Hosts[query.qname]
            print("Find a Hint: %s:%s"%(query.qname, ip))
        if find and query.qtype == "0x0001": #only handle A record
            print('domain:%s in hosts' % query.qname)
            response = DnsParser.generateReqponse(data,ip)
            self.socket.sendto(response,address)
        else:
            print('transfer for %s' % query.qname)
            response,serveraddress = udp_send(LOCALDNS,data)
            self.socket.sendto(response,address)


if __name__ == "__main__":
    DnsServer("192.168.1.107:53").serve_forever()