#!/usr/bin/env python
# -*- coding:utf-8 -*- 

def clock_angle(time):
	h,m=time.split(":")
	h,m=int(h),int(m)
	if h>12:
		h=h-12
	ha=(h*60+m)/(12*60.0)*360
	ma=m/60.0*360
	ang=abs(ma-ha)
	if ang>180:
		ang=360-ang
	ang=int(ang*10)
	return ang//10 if ang%10==0 else ang/10.0

if __name__ == "__main__":
	print clock_angle("00:00")
	print clock_angle("02:30")
	print clock_angle("13:42")
	print clock_angle("01:43")
	print clock_angle("12:01")

