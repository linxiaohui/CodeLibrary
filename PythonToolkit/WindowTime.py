# -*- coding:UTF-8 -*-

try:
	from _winreg import *
except:
	from winreg import *

import ctypes
import time
def getInstallTime():
	datepath = "Software\\Microsoft\\Windows NT\\CurrentVersion"
	datepath2 = "Software\\Microsoft\\Windows\\CurrentVersion"
	try:
		key = OpenKey(HKEY_LOCAL_MACHINE, datepath)
		when,type = QueryValueEx(key, "InstallDate")
		installtime = time.strftime("%z %Y-%m-%d %X %A",time.localtime(when))
		return installtime
	except WindowsError:
		try:
			key=OpenKey(HKEY_LOCAL_MACHINE,datepath2)
			when,type=QueryValueEx(key, "FirstInstallDate")
			installtime=time.strftime("%z %Y-%m-%d %X %A",time.localtime(when))
			return installtime
		except WindowsError:
			raise Exception("Can not read install time")

def FormatSeconds(sec):
    sec /= 1000
    min = sec/60
    sec %= 60
    hour = min/60
    min %= 60
    return "%d hours %d minutes %d seconds" %( hour,min,sec)
   
def main():
	MessageBox = ctypes.windll.user32.MessageBoxA
	installtime = getInstallTime()
	sec=ctypes.windll.kernel32.GetTickCount()
	installtime +="\n Running "+FormatSeconds(sec)
	print(installtime)
	MessageBox(0,installtime,"Install Time",0)
	
if __name__ == "__main__":
	main()