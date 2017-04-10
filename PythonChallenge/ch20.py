import http.client
import pprint
import base64
import re

def get_range(page, base, limit):
    conn = http.client.HTTPConnection('www.pythonchallenge.com')
    headers = {'Authorization': 'Basic ' + base64.b64encode(b'butter:fly').decode(),
               'Range': 'bytes=%s-%s' % (base, limit)}
    conn.request('GET', page, '', headers)
    return conn.getresponse()

def next_range(base):
    r = get_range('/pc/hex/unreal.jpg', base, 2123456789)
    print("============")
    print(r.read())
    pprint.pprint(r.getheaders())
    if r.getheader('content-range') is None:
        return 0
    m = re.match('bytes %d-([0-9]+)/2123456789' % base, r.getheader('content-range'))
    if m:
        return int(m.group(1)) + 1
    else:
        return 0

base = 30203
cont = False
cont = True
while cont:
    base = next_range(base)
    if base == 0:
        cont = False

print("###")
r = get_range('/pc/hex/unreal.jpg',2123456789, pow(2,31))
print(r.read()[::-1])
pprint.pprint(r.getheaders())


r = get_range('/pc/hex/unreal.jpg',2123456743, pow(2,31))
print(r.read())
pprint.pprint(r.getheaders())

r = get_range('/pc/hex/unreal.jpg',1152983631, pow(2,31))
data = r.read()
pprint.pprint(r.getheaders())
open("ch20.zip","wb").write(data)
