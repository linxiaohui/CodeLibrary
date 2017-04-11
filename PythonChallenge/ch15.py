# *-* coding:UTF-8 *-*

import calendar
for year in range(1006,1997,10):
	if calendar.isleap(year) and calendar.weekday(year,1,1)==3:
		print(year)

#PS: 1582 was the first year of the Gregorian calendar

'''
输出
1176
1356
1576
1756
1976

结合
he ain't the youngest, he is the second, buy flowers for tomorrow
与1756-01-27有关
搜索得知这一天莫扎特诞生,所以是mozart  
'''
