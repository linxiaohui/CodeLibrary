# *-* coding:UTF-8 *-*
from PIL import Image
im = Image.open("mozart.gif")
print(im.mode, im.size)

w, h = im.size

#按行扫描,每行粉红色条的第一个点
bars = []
'''把粉红色(195)对齐'''
magenta = 195
for j in range(h):
    for i in range(w):
        if im.getpixel((i, j)) == magenta:
            if i > 1 and im.getpixel((i - 1, j)) == magenta:
                pass
            else:
                bars.append((i, j))
print(len(bars))
im2 = Image.new(im.mode, (w, h))
for j in range(h):
    for i in range(w):
        im2.putpixel(((i + w - bars[j][0])%w, j), im.getpixel((i, j)))
im2.save("ch16.png")
