#!/usr/bin/env python
# *-* coding:UTF-8 *-*

def count_gold(pyramid):
	"""
	Return max possible sum in a path from top to bottom
	"""
	nlen=len(pyramid)
	res=[[0]*i for i in range(1,nlen+1)]
	res[0][0]=pyramid[0][0]
	for i in range(1,nlen):
		for j in range(0,i+1):
			res[i][j]=pyramid[i][j]+max(res[i-1][j if j<i else j-1],res[i-1][0 if j==0 else j-1])
	return max(res[-1])

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
