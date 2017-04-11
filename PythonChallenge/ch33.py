# *-* coding:UTF-8 *-*
from PIL import Image
import math
'''
Each time, if the pixels could fit into a square, check the brightest pixels and log the information. 
Then remove the brightest pixels and Go to the next round.
'''
beer = Image.open('beer2.png')
#获取颜色信息
colors = beer.getcolors()
colors_len = len(colors)
data = list(beer.getdata())
colors_index = colors_len - 1
while colors_index > 0:
    #创建一幅新的图片，以像素数总数的开平方数为长宽值
    dim = int(math.sqrt(len(data)))
    new_img = Image.new('1', (dim, dim))
    #把所有以最大颜色值为颜色参数的像素点标记为'亮'，其余像素点标记为'暗'
    output = [item == colors[colors_index][1] for item in data]
    new_img.putdata(output)
    new_img.save('ch33_%d.png'%(colors_index / 2))
    new_img.close()
    #抛弃颜色值最大的一组颜色，并且抛弃使用这些颜色的像素
    eli_color_a = colors.pop(colors_index)[1]
    eli_color_b = colors.pop(colors_index - 1)[1]
    for k in range(len(data) - 1, -1, -1):
        if data[k] == eli_color_a or data[k] == eli_color_b:
            data.pop(k)
    colors_index -= 2
