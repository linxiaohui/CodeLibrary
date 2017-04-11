# *-* coding:UTF-8 *-*

content = open("evil2.gfx","rb").read()
r=[open("ch12_%d.jpg"%i,"wb") for i in range(5)]
w=[r[i].write(content[i::5]) for i in range(5)]
[f.close() for f in r]


