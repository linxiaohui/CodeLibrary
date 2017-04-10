#!/bin/python

from PIL import Image
im = Image.open("wire.png")
print(im.mode, im.size)
im2 = Image.new(im.mode, (100, 100))

# spiral order
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# start from center
(x, y) = (49, 49)

indx = 0
d = 0
i = 1
j = 0
while i < 100:
    t = 0
    while t < 2:
        j = 0
        D = directions[d % 4]
        while j < i:
            p = im.getpixel((9999 - indx, 0))
            indx += 1
            im2.putpixel((x, y), p)
            x += D[0]
            y += D[1]
            j += 1
        d += 1
        t += 1
    i += 1

im2.save("ch14.png")
