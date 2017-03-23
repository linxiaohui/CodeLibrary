#!/usr/bin/env python
# -*- coding:utf-8 -*-  

def checkio(game_result):
	Xwin=False
	Owin=False
	for i in range(0,3):
		for j in range(0,3):
			if game_result[i][j]=='X':
				if (j+2<3 and game_result[i][j+1]=='X' and game_result[i][j+2]=='X' or
				    i+2<3 and game_result[i+1][j]=='X'  and game_result[i+2][j]=='X' or
				    i+2<3 and j+2<3 and game_result[i+1][j+1]=='X' and game_result[i+2][j+2]=='X' or
				    i+2<3 and j-2>=0 and game_result[i+1][j-1]=='X' and game_result[i+2][j-2]=='X'):
				    Xwin=True
			if game_result[i][j]=='O':
				if (j+2<3 and game_result[i][j+1]=='O' and game_result[i][j+2]=='O' or
				    i+2<3 and game_result[i+1][j]=='O'  and game_result[i+2][j]=='O' or
				    i+2<3 and j+2<3 and game_result[i+1][j+1]=='O' and game_result[i+2][j+2]=='O' or
				    i+2<3 and j-2>=0 and game_result[i+1][j-1]=='O' and game_result[i+2][j-2]=='O'):
				    Owin=True
	if Xwin and not Owin:
		return 'X' 
	if Owin and not Xwin:
		return 'O'
	return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"

