
from PIL import Image,ImageSequence


im =  Image.open('white.gif')
joy = Image.new(im.mode, (200,200), 0)
x = 0  
y = 0  
for s in ImageSequence.Iterator(im):  
    l,u,r,d = im.getbbox()  
    dx = (l-100)  
    dy = (u-100)  
    x+=dx  
    y+=dy
    if dx==dy==0:  
        x+=20  
        y+=20  
    joy.putpixel((x,y),255)  

joy.save('joy.gif')
