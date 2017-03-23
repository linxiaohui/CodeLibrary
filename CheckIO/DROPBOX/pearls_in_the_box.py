#!/usr/bin/env python
# *-* coding:UTF-8 *-*


from collections import Counter

def whitep(state, step):
	wn=state['w']
	bn=state['b']
	if step==1:
		return 1.0*wn/(wn+bn)
	wstate=dict(state)
	bstate=dict(state)
	wp,bp=0.0,0.0
	if wn!=0:
		wstate['w']=wstate['w']-1
		wstate['b']=wstate['b']+1
		wp=whitep(wstate,step-1)*1.0*wn/(wn+bn)
	if bn!=0:
		bstate['w']=bstate['w']+1
		bstate['b']=bstate['b']-1
		bp=whitep(bstate,step-1)*1.0*bn/(wn+bn)
	return wp+bp


def checkio(marbles, step):
	init=dict(Counter(marbles))
	if 'w' not in init:
		init['w']=0
	if 'b' not in init:
		init['b']=0
	return round(whitep(init,step),2)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'bbw', 3) == 0.48, "1st example"
    assert checkio(u'wwb', 3) == 0.52, "2nd example"
    assert checkio(u'www', 3) == 0.56, "3rd example"
    assert checkio(u'bbbb', 1) == 0, "4th example"
    assert checkio(u'wwbb', 4) == 0.5, "5th example"
    assert checkio(u'bwbwbwb', 5) == 0.48, "6th example"