# *-* coding:UTF-8 *-*
# '1'
# 1'1'
# 2'1'
# 1'2'1'1'
# 1'1'1'2'2'1'
# .....

def count(l):
	cnt=1
	pre=l[0]
	for x in l[1:]:
		if x==pre:
			cnt+=1
		else:
			yield cnt
			yield pre
			pre=x
			cnt=1
	yield cnt
	yield pre

a=[1]
for i in range(30):
	print(i+1,end=':')
	a=list(count(a))
	print(len(a))
