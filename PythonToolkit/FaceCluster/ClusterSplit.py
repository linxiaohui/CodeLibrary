#!/usr/bin/python
#-*- coding:UTF-8 -*-

# 根据KNN的结果将同一个目录下的图片移动到不同的目录(聚类)中

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

fp = open("cluster.pickle","rb")
clusters = pickle.load(fp)
fp.close()

ROOT=sys.argv[1]
for ll, c in clusters.items():
    print(ll,type(c))
    l=str(ll)
    os.mkdir(ROOT+os.sep+l)
    for x in c:
        print(x)
        os.rename(x,ROOT+os.sep+l+os.sep+x.split('\\')[-1])

