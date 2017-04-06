#!/bin/python

'''
ch11.py 的结果是 `evil`, 打开`evil.html`显示图片, 看到html源码里 `evil1.jpg`, 试下`evil2.jpg`内容提示将jpg改为gfx;
下载`evil2.gfx`, 然后根据之前的图片提示, 像分牌那样分5堆
'''
content = open("evil2.gfx","rb").read()
r=[open("ch12_%d.jpg"%i,"wb") for i in range(5)]
w=[r[i].write(content[i::5]) for i in range(5)]
[f.close() for f in r]


