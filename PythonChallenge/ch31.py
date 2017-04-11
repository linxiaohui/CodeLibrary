# *-* coding:UTF-8 *-*
from PIL import Image

ufo_1 = Image.open('mandelbrot.gif')
def mandelbrot(left=0.34, bottom=0.57, width=0.036, height=0.027, max=128, size=(640, 480)):
    xstep = width / size[0]
    ystep = height / size[1]
    for y in range(size[1] - 1, -1, -1):
        for x in range(size[0]):
            c = complex(left + x * xstep, bottom + y * ystep)
            z = 0+0j
            for i in range(max):
                z = z * z + c
                if abs(z) > 2:
                    break
            yield i

#绘制一个新的分形图
ufo_2 = ufo_1.copy()
ufo_2.putdata(list(mandelbrot()))
#ufo_2.show()
#查找两副图片的差异
differences = [(a - b) for a, b in zip(ufo_1.getdata(), ufo_2.getdata()) if a != b]
#根据差值绘制出一张新的图片
plot = Image.new('1', (23, 73))
plot.putdata([i < 16 for i in differences])
#plot.resize((230, 730)).show()
plot.show()

#arecibo