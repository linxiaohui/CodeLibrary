
from PIL import Image
img = Image.open('bell.png')
img.load()
r,g,b = img.split()

gdata = list(g.getdata())
newlist = [(gdata[i]-gdata[i+1]) for i in range(0,len(gdata),2)]
s = ''
for i in newlist:
    if i != -42 and i!=42:
        s+=chr(abs(i))
print(s)
