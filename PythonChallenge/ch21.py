# *-* coding:UTF-8 *-*

import zlib
import bz2
import pprint

def uncompress(data, log):
    if data[:2] == b'\x78\x9c':
        log.append('z')
        return zlib.decompress(data)
    elif data[:2] == b'BZ':
        log.append('b')
        return bz2.BZ2Decompressor().decompress(data)
    elif data[-2:] == b'\x9c\x78':
        log.append('Z')
        return zlib.decompress(data[::-1])
    elif data[-2:] == b'ZB':
        log.append('B')
        return bz2.BZ2Decompressor().decompress(data[::-1])
    else:
        return None
        
pack = open('package.pack','rb').read()
unpack = ''
log = []
while True:
    unpack = uncompress(pack, log)
    if unpack is None:
        unpack = pack
        print(pack)
        print(pack[::-1])
        break
    else:
        pack = unpack

pprint.pprint(''.join(log).replace('z',' ').split('Z'))
