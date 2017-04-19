# coding=cp936
from struct import*
import string, sys

def ip2string(ip):
    a = (ip & 0xff000000) >>24
    b = (ip & 0x00ff0000) >>16
    c = (ip & 0x0000ff00) >>8
    d = ip & 0x000000ff
    return '%d.%d.%d.%d' % (a, b, c, d)

def string2ip(mystr):
    ss = string.split(mystr, '.');
    ip = 0L
    for s in ss:
        ip = (ip << 8) + string.atoi(s)
    return ip;

class IpLocater:
    def __init__(self, ipdb_file):
        self.ipdb = open(ipdb_file, 'rb')
        # get index address
        header = self.ipdb.read(8)
        (self.first_index, self.last_index) = unpack('II', header)
        self.index_count = (self.last_index - self.first_index) / 7 + 1

    def getString(self, offset = 0):
        if offset :
            self.ipdb.seek(offset)
        mystr = ''
        if self.ipdb.tell() == 0:
           return 'Waht?'
        ch = self.ipdb.read(1)
        (byte,) = unpack('B', ch)
        while byte != 0:
            mystr = mystr + ch
            ch = self.ipdb.read(1)
            (byte,) = unpack('B',ch)
        return mystr

    def getLong3(self, offset = 0):
        if offset :
            self.ipdb.seek(offset)
        mystr = self.ipdb.read(3)
        (a,b) = unpack('HB', mystr)
        return (b << 16) + a

    def getAreaAddr(self, offset=0):
        if offset :
            self.ipdb.seek(offset)
        mystr = self.ipdb.read(1)
        (byte,) = unpack('B', mystr)
        if byte == 0x01 or byte == 0x02:
            
            p = self.getLong3()
            if p:
                return self.getString(p)
            else:
                return ''
        else:
            
            self.ipdb.seek(self.ipdb.tell() - 1)
            return self.getString()

    def getAddr(self, offset, ip = 0):
        self.ipdb.seek(offset + 4)

        countryAddr = ''
        areaAddr = ''
        mystr = self.ipdb.read(1)
        (byte,) = unpack('B', mystr)
        if byte == 0x01:
            
            countryOffset = self.getLong3()
            self.ipdb.seek(countryOffset)
            mystr = self.ipdb.read(1)
            (b,) = unpack('B', mystr)
            if b == 0x02:
                
                countryAddr = self.getString(self.getLong3())
                self.ipdb.seek( countryOffset + 4 )
            else:
                countryAddr = self.getString(countryOffset)
            areaAddr = self.getAreaAddr()
        elif byte == 0x02:
            
            countryAddr = self.getString(self.getLong3())
            areaAddr = self.getAreaAddr(offset + 8)
        else:
            countryAddr = self.getString(offset + 4)
            areaAddr = self.getAreaAddr()
        #print countryAddr
        #print areaAddr
        return countryAddr + '/' + areaAddr

    def output(self, first, last):
        if last > self.index_count :
            last = self.index_count
        for index in range(first, last):
            offset = self.first_index + index * 7
            self.ipdb.seek(offset)
            buf = self.ipdb.read(7)
            (ip,of1,of2) = unpack('IHB', buf)
            print '%s - %s' % (ip2string(ip), self.getAddr( of1 + (of2 <<16)))

    def find(self, ip, left, right):
        if right-left == 1:
            return left
        else:
            middle = (left + right) / 2
            offset = self.first_index + middle * 7
            self.ipdb.seek(offset)
            buf = self.ipdb.read(4)
            (new_ip,) = unpack('I', buf)
            if ip <= new_ip :
                return self.find(ip, left, middle)
            else:
                return self.find(ip, middle, right)

    def getIpAddr(self, ip):
        index = self.find(ip, 0, self.index_count - 1)
        ioffset = self.first_index + index * 7
        aoffset = self.getLong3(ioffset + 4)
        address = self.getAddr(aoffset)
        return address

def main(argv=None):
    if len(sys.argv) != 2:
       print 'usage: locate <ip>'
       sys.exit(-1)
    ip_locater = IpLocater(r'F:\MyEnvs\OpenSSH\bin\QQWry.Dat')
    ip_locater.output(1, 250000)
    print '%d?' % ip_locater.index_count
    ip = sys.argv[1]
    address = ip_locater.getIpAddr(string2ip(ip))
    print 'the ip %s come from %s' % (ip, address)

if __name__ == '__main__' :
    main()
