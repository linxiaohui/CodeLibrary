# *-* coding:UTF-8 *-*
import http.client
import base64
import wave
from PIL import Image

def get_file(page, local):
    conn = http.client.HTTPConnection('www.pythonchallenge.com')
    headers = {'Authorization': 'Basic ' + base64.b64encode(b'butter:fly').decode()}
    conn.request('GET', page, '', headers)
    resp = conn.getresponse()
    open(local,"wb").write(resp.read())
    
for i in range(1, 26):
    name = "lake%d.wav"%i
    print(name)
    get_file("/pc/hex/%s"%name, name)
    
wavs = [wave.open('lake%d.wav' % i,"rb") for i in range(1,26)]

def jig(w):
    return Image.frombytes('RGB', (60,60), w.readframes(w.getnframes()))
    
jigsaw = Image.new('RGB', (300,300), 0)
for i in range(len(wavs)):
    jigsaw.paste(jig(wavs[i]), (60 * (i % 5), 60 * (i // 5)))

jigsaw.save('jigsaw.png')
