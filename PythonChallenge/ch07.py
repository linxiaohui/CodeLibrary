# *-* coding:UTF-8 *-*
import sys
import PIL
from PIL import Image 
im= Image.open("oxygen.png")

print(im.mode)

for (r,g,b,a) in im.getdata():
	if r==g and r==b:
		sys.stdout.write(chr(r))

print()
x=[105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join([chr(i) for i in x]))
