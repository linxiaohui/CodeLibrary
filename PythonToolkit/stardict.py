#!/usr/bin/python
# -*- coding:UTF-8 -*-
'''
C 2009 
'''

import struct
import dictzip

class StarDict(object):
    def __init__(self,dictname):
        self.name=dictname
        self.data = None
        self.inx=None
        self.yainx=None
        self.wordlist=[]
        self.initialize(dictname)
    
    def initialize(self,name):
        self.data=dictzip.DictzipFile(name+".dict.dz")
        #self.data.runtest()
        self.inx=open(name+".idx",'rb').read()
        self.info=open(name+".ifo",'rb').read()
        self.yainx=open(name+".yaidx",'wb')
        runner = 0
        self.wordlist.append(runner)
        i=0
        while True:
            runner = self.inx.find('\0',runner)
            if runner == -1:
                break
            runner+=9
            self.wordlist.append(runner)
            i+=1
        for pos in self.wordlist:
        	self.yainx.write(struct.pack(">i",pos))
        self.yainx.close()
       	

    def get_word(self,index):
        "get word from self.index"
        left_b = self.wordlist[index]
        right_b = self.wordlist[index+1] - 9
        #print self.index[left_b:right_b]
        return self.inx[left_b:right_b]

    def get_explanation(self,index):
        "get word from self.dict"
        right_b = self.wordlist[index+1] - 9
        offset_v = 0
        size_v =  0
        offset = self.inx[right_b+1:right_b+5]
        size = self.inx[right_b+5:right_b+9]
        offset_v = struct.unpack('!i',offset)[0]
        size_v = struct.unpack('!i',size)[0]
        self.data.seek(offset_v)
        return self.data.read(size_v)
    
    def __del__(self):
        if self.data:
            self.data.close()

if __name__=="__main__":
	path = raw_input("Please input the path of the dict (e.g. g:/stardict/dict)")
	dict = StarDict(path)