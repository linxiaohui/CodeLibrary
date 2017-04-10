#!/bin/python

import urllib
import re
import base64
import codecs

def hex(s): return codecs.getencoder('hex')(s)[0]


data = open("bin.base64","rb").read()
with open('indian.wav','wb') as f:
    f.write(base64.decodestring(data))

import wave
iw = wave.open('indian.wav','rb')
#iaudio = iw.readframes(iw.getnframes())

print(iw.getnframes())

iw2 = wave.open('indian2.wav','wb')
iw2.setparams(iw.getparams())  
for i in range(iw.getnframes()):  
    iw2.writeframes(iw.readframes(i)[::-1])  #图片大陆和海颜色反转了
iw2.close()

