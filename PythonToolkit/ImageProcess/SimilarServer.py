#!/usr/bin/python
#-*- coding:UTF-8 -*-
'''
/*
    A Tiny Server to Show all pic in a directory (to browse in a browser)
    Update: text, zip
*/
Requirement: tornado chardet
'''
import urllib
import sys
import os
import zipfile
import socket
import hashlib
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import chardet
import base64  
import pickle

ROOT=""
HOSTCODE="UTF-8"
PICEXTS=(".jpg","gif","bmp","jpeg","png")
PREFIX=(".com")
MEDIAEXTS=(".mp3",".ogg")
CHECKLOGIN=True

HEADTEMPLATE="""<html><head>
<script language="javascript">
var currpos,timer;
function init(){timer=setInterval ("scrollwindow()",10);}
function clearr(){clearInterval(timer);}
function scrollwindow(){currpos=document.body.scrollTop;window.scroll(0,++currpos);
if(currpos !=document.body.scrollTop)
clearr();}
document.onmousedown=clearr
document.ondblclick=init
</script>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/></head><body>
"""

PLAYER="""
<object id="mp3_player" type="application/x-oleobject" height="80" width="300" 
classid="CLSID:6BF52A52-394A-11d3-B153-00C04F79FAA6">
<param NAME="AutoStart" VALUE="0">
<param NAME="url" value="%s">
<param NAME="PlayCount" VALUE="1">
</object>
<button onclick="mp3_player.controls.play();" alt="播放" style="cursor:hand" >播放</button>
<button onclick="mp3_player.controls.pause();" alt="暂停" style="cursor:hand">暂停</button>
<button onclick="mp3_player.controls.Stop();" alt="停止" style="cursor:hand">停止</button>
"""

HTML5PLAYER="""
<audio controls="controls">
  <source src="/%s.ogg" type="audio/ogg" >
  <source src="/%s.mp3" type="audio/mpeg" >
</audio>
"""


fp = open(sys.argv[2],"rb")
db = pickle.load(fp)
fp.close()

def CheckPasswd(passwd, hashpass):
    s = hashlib.sha256()
    p = hashpass[:2]+passwd
    s.update(p.encode('utf-8'))
    return hashpass[2:]==s.hexdigest()

def CheckLogin(self):
    global CHECKLOGIN
    if not CHECKLOGIN:
        return True
    auth_header = self.request.headers.get('Authorization', None)
    if auth_header is not None:
        auth_mode, auth_base64 = auth_header.split(' ', 1)
        auth_username, auth_password = base64.b64decode(auth_base64.encode('utf-8')).decode('utf-8').split(':', 1)
        if auth_username=="admin" and CheckPasswd(auth_password,"x$9a808243ff06b8803ff374a681d553e2498c24291730a2a4c752e21bc7b67a2e"):
            return True
    self.set_header('Access-Control-Allow-Origin', '*')
    self.set_header('WWW-Authenticate', 'Basic realm="Authentication required"')
    self.set_status(401)
    return False

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        if not CheckLogin(self):
            self.write("Not Authorized")
            return None
        global HOSTCODE
        ret = HEADTEMPLATE+"""<table>"""
        for hsh, filenames in db.items():
            if len(filenames)>1:
                for f in filenames:
                    ret+="<tr>"
                    ret+="<td><img src='{}'></td><td>{}</td>".format(f[2:],f)
                    ret+="</tr>\n"
                ret+="<tr><td>NNNNNNNNNNNNNNN</td><tr>"
        ret = ret+"</table></body></html>"
        self.write(ret)

class ClusterHandler(tornado.web.RequestHandler):
    def get(self, r):
        if not CheckLogin(self):
            return None
        ret = HEADTEMPLATE+"""<table>"""
        fnames = clusters[int(r)]
        for f in fnames:
            ret += "<tr><td><img src='/{}'></td></tr>\n".format(f)
        ret = ret+"</table></body></html>"
        self.write(ret)

class TestHandler(tornado.web.RequestHandler):
    def get(self):
        ret = os.getcwd()
        self.write(ret)


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), ROOT),
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            autoescape=None,
        )
        handlers = [
            (r"/", IndexHandler),
            (r"/cluster/(.+)", ClusterHandler),
            (r"/test", TestHandler),
            (r"/(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(80)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    ips = socket.gethostbyname_ex(socket.gethostname())
    for ip in ips[2]:
        print(ip)
    if len(sys.argv) >= 2:
        ROOT = sys.argv[1]
    else:
        ROOT = input("Specify the root directory: ")
    if len(sys.argv) >= 3:
        HOSTCODE = sys.argv[2]
    print(HOSTCODE)
    if len(sys.argv) >=4:
        CHECKLOGIN=eval(sys.argv[3])
    main()
