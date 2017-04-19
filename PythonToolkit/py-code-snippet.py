x = 2
if 3 > x > 1:
   print x

if 1 < x > 0:
   print x

nfc = ["Packers", "49ers"]
afc = ["Ravens", "Patriots"]
for teama, teamb in zip(nfc, afc):
     print teama + " vs. " + teamb

# 列表分组
l=[1,2,3,4,5,6,7]
list(zip(*[iter(l)]*2))


print "Hello" if True else "World"


teams = ["Packers", "49ers", "Ravens", "Patriots"]
for index, team in enumerate(teams):
    print index, team

for x in range(101):print"fizz"[x%3*4::]+"buzz"[x%5*4::]or x


from itertools import combinations
teams = ["Packers", "49ers", "Ravens", "Patriots"]
for game in combinations(teams, 2):
    print game

#python 获得本机MAC地址
import uuid
def get_mac_address():  
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]  
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

import socket
#获取本机电脑名
myname = socket.getfqdn(socket.gethostname(  ))
#获取本机ip
myaddr = socket.gethostbyname(myname)
print myname 
print myaddr

import socket
import fcntl
import struct

#在linux下可用   
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
  
get_ip_address('lo')
'127.0.0.1'
  
get_ip_address('eth0')
'38.113.228.130'


def strQ2B(ustring):
    """把字符串全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code==0x3000:
            inside_code=0x0020
        else:
            inside_code-=0xfee0
        if inside_code<0x0020 or inside_code>0x7e:      #转完之后不是半角字符返回原来的字符
            rstring += uchar
        rstring += unichr(inside_code)
    return rstring

def strB2Q(ustring):
    """把字符串半角转全角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code<0x0020 or inside_code>0x7e:      #不是半角字符就返回原来的字符
            rstring += uchar
        if inside_code==0x0020: #除了空格其他的全角半角的公式为:半角=全角-0xfee0
            inside_code=0x3000
        else:
            inside_code+=0xfee0
        rstring += unichr(inside_code)
    return rstring


import codecs  
start,end = (0x4E00, 0x9FA5)  
with codecs.open("chinese.txt", "wb", encoding="utf-8") as f:  
    for codepoint in range(int(start),int(end)):  
        f.write(unichr(codepoint))

