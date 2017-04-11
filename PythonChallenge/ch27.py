# *-* coding:UTF-8 *-*
from PIL import Image
import bz2
import string
import keyword

zig = Image.open('zigzag.gif')
zigdata=zig.tobytes() 
palette = zig.palette.getdata()[1][::3] #获取其调色板
t = bytes.maketrans(bytes([i for i in range(256)]),palette)
zigtrans = zigdata.translate(t) # 用调色板值转换像素值

deltas = [p for p in zip(zigdata[1:], zigtrans[:-1]) if p[0] != p[1]]
diffs=[bytes([p[i] for p in deltas]) for i in range(2)]

bz = bz2.decompress(diffs[0])

keywords=bz.split(b' ')
keys={}
for k in keywords:
    keys[k]=1

print(list(keys.keys()))

#将不一样的像素按位置显示出来
im = Image.new('1',zig.size,0)
im.putdata([ p[0]==p[1] for p in zip(zigdata[1:],zigtrans[:-1])])
im.save('ch27.png')

for k in list(keys.keys()):
    if not keyword.iskeyword(k.decode()):
        print(k)

