import http.client,bz2,base64

def get_resp(page):
    conn = http.client.HTTPConnection('www.pythonchallenge.com')
    headers = {'Authorization': 'Basic ' + base64.b64encode(b'repeat:switch').decode()}
    conn.request('GET', page, '', headers)
    resp = conn.getresponse()
    return resp

resp = get_resp('/pc/ring/guido.html')
data = bytes([len(i)-1 for i in resp.readlines()[12::]])
print(bz2.decompress(data))
