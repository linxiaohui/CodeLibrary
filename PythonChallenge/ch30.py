from PIL import Image
import re

fp = open(r'yankeedoodle.csv','r')
data = re.findall(r'(0.\d*)',fp.read())
im = Image.new('F',(53,139))
im.putdata(list(map(float,data)),256)
im = im.transpose(Image.ROTATE_90)
im = im.transpose(Image.FLIP_TOP_BOTTOM)
im.show()

s = [chr(int(data[i][5]+data[i+1][5]+data[i+2][6])) for i in range(0,len(data)-2,3)]  
print(''.join(s))  
