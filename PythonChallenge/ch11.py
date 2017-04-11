# *-* coding:UTF-8 *-*
from PIL import Image

im = Image.open("cave.jpg")

print(im.mode)
print(im.size)

newsize=(im.size[0]//2, im.size[1]//2)

odd=Image.new(im.mode, newsize)
even=Image.new(im.mode, newsize)

for x in range(0, im.size[0]):
	for y in range(0, im.size[1]):
		p=im.getpixel((x,y))
		if (x+y)%2==0:
			even.putpixel((x//2,y//2),p)
		else:
			odd.putpixel((x//2,y//2),p)

odd.save("odd.jpg")
even.save("even.jpg")
