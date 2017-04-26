# -*- coding:utf-8 -*-

import struct
import numpy as np
import cv2
import gzip
import os

'''
[offset] [type]          [value]          [description] 
0000     32 bit integer  0x00000803(2051) magic number 
0004     32 bit integer  10000            number of images 
0008     32 bit integer  28               number of rows 
0012     32 bit integer  28               number of columns 
0016     unsigned byte   ??               pixel 
0017     unsigned byte   ??               pixel 
........ 
xxxx     unsigned byte   ??               pixel
'''
def read_image(datapath):
    with open(datapath, 'rb') as ff, gzip.GzipFile(fileobj=ff) as f:
        magic=f.read(4)
        imgnum = struct.unpack(">i",f.read(4))[0]
        rows = struct.unpack(">i",f.read(4))[0]
        cols = struct.unpack(">i",f.read(4))[0]
        buff = f.read(rows * cols * imgnum)
        data = np.frombuffer(buff, dtype=np.uint8)
        data = data.reshape(imgnum, rows*cols)
        data = data.astype(np.float32)
        data = np.multiply(data, 1.0 / 255.0)
        return data

'''
[offset] [type]          [value]          [description] 
0000     32 bit integer  0x00000801(2049) magic number (MSB first) 
0004     32 bit integer  10000            number of items 
0008     unsigned byte   ??               label 
0009     unsigned byte   ??               label 
........ 
xxxx     unsigned byte   ??               label
'''
def read_label(datapath):
    with open(datapath, 'rb') as ff, gzip.GzipFile(fileobj=ff) as f:
        magic=f.read(4)
        items = struct.unpack(">i",f.read(4))[0]
        buf = f.read(items)
        data = np.frombuffer(buf, dtype=np.uint8)
        index_offset = np.arange(items) * 10
        labels_one_hot = np.zeros((items, 10))
        labels_one_hot.flat[index_offset + data.ravel()] = 1
        return labels_one_hot

class MNISTDataSet(object):
    def __init__(self, dpath):
        self.datapath = dpath
        self.train_images = read_image(dpath+os.sep+'train-images.idx3-ubyte.gz')
        self.train_labels = read_label(dpath+os.sep+'train-labels.idx1-ubyte.gz')
        self.test_images = read_image(dpath+os.sep+'t10k-images.idx3-ubyte.gz')
        self.test_labels = read_label(dpath+os.sep+'t10k-labels.idx1-ubyte.gz')
        self._idx = 0
        self._train_num = self.train_images.shape[0]
    
    def next_train_batch(self,size):
        if self._idx + size > self._train_num:
            pivot = np.arange(self._train_num)
            np.random.shuffle(pivot)
            self.train_images = self.train_images[pivot]
            self.train_labels = self.train_labels[pivot]
            self._idx=0
        start = self._idx
        self._idx+=size
        return (self.train_images[start:self._idx],self.train_labels[start:self._idx])
    
    def get_test_data(self):
        return (self.test_images, self.test_labels)

if __name__=="__main__":
    dataset = MNISTDataSet('mnist')
    images = dataset.get_test_data()[0]
    labels = dataset.get_test_data()[1]
    test_index=[1]
    for idx in test_index:
        #print(images[idx])
        cv2.imshow("digit",(255*images[idx]).astype(np.int8).reshape(28,28))
        cv2.waitKey(0)
        print(labels[idx])