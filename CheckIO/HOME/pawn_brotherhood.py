#!/usr/bin/env python
# *-* coding:UTF-8 *-*

def safe_pawns(pawns):
	cnt=0
	for l in pawns:
		col,row=l.lower()
		if int(row)==1:
			continue
		if col>='b' and chr(ord(col)-1)+str(int(row)-1) in pawns or col<='g' and chr(ord(col)+1)+str(int(row)-1) in pawns:
			cnt+=1
	return cnt

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
