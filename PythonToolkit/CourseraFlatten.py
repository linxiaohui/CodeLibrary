#-*- coding:UTF-8 -*-
'''
使用coursera-dl下载coursera课程资源后, 减少目录层级
'''
import sys
import os

def FlatDir(destdir):
    os.chdir(destdir) ## 课程目录
    for week in sorted(os.listdir(".")):
        #print(week)
        os.chdir(week) # 每周目录
        i=1
        for clazz in sorted(os.listdir(".")):
            #print(clazz)
            os.chdir(clazz)
            files = sorted(os.listdir("."))
            mp4srt = list(zip(*[iter(files)]*2))
            #for f in files:
            #    print(f)
            #    print("{:02d}{}".format(i,f))
            for m in mp4srt:
                #print(m)
                assert len(os.path.commonprefix(m))>=10
                srt = m[0]
                mp4 = m[1]
                dest_srt = "..\\{:02d}_{}".format(i,"_".join(srt.split("_",1)[1:]))
                dest_mp4 = "..\\{:02d}_{}".format(i,"_".join(mp4.split("_",1)[1:]))
                print(dest_srt)
                print(dest_mp4)
                os.rename(srt, dest_srt)
                os.rename(mp4, dest_mp4)
                i=i+1
            os.chdir("..")
        os.chdir("..")
        
DESTDIR=""
if len(sys.argv)>=2:
    DESTDIR=sys.argv[1]

FlatDir(DESTDIR)
