# *-* coding:UTF-8 *-*

import urllib.request
import urllib.parse
import urllib.error
import urllib.request
import urllib.error
import urllib.parse
import http.cookiejar
import re
import bz2

auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password('inflate', 'www.pythonchallenge.com', 'huge', 'file')
jar = http.cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(jar)
opener = urllib.request.build_opener(auth_handler, cookie_handler)
urllib.request.install_opener(opener)
opener.addheaders = [
    ('User-agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.103 Safari/537.36')]
# resp=opener.open('http://www.pythonchallenge.com/pc/return/romance.html')
# print resp.read()
resp = opener.open('http://www.pythonchallenge.com/pc/def/linkedlist.php')

for cookie in jar:
    print(cookie)
    print((cookie.name, cookie.value))

nexter = re.compile("and the next busynothing is ([0-9]+)")

message = []
resp = opener.open(
    'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345')
cont = True
while cont:
    page = str(resp.read())
    print(page)
    for cookie in jar:
        print(cookie.name, cookie.value)
        message.append(cookie.value)
    m = nexter.search(page)
    if m:
        print(m.group(1))
        resp = opener.open(
            'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=%s' % m.group(1))
    else:
        cont = False

msg = ''.join(message)
print(msg)
msg = msg.replace('+', ' ')
decoded = urllib.parse.unquote_to_bytes(msg)
print(decoded)
print(bz2.decompress(decoded))
'''is it the 26th already? call his father and inform him that "the flowers are on
their way". he'll understand.'''

# Call mozart's father: Leopold Mozart

url="http://www.pythonchallenge.com/pc/phonebook.php"
import xmlrpc.client
server=xmlrpc.client.Server(url)
print(server.phone("Leopold"))
'''
555-VIOLIN
'''


list(jar)[0].value = 'the+flowers+are+on+their+way'
print(opener.open('http://www.pythonchallenge.com/pc/stuff/violin.php').read())
'''
b'<html>\n<head>\n  <title>it\'s me. what do you want?</title>\n 
 <link rel="stylesheet" type="text/css" href="../style.css">\n
 </head>\n<body>\n\t<br><br>\n\t<center><font color="gold">\n\t
 <img src="leopold.jpg" border="0"/>\n<br><br>\noh well, don\'t you dare to forget the balloons
 .</font>\n</body>\n</html>\n'
'''