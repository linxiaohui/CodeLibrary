import codecs
import re
import gzip


def unhex(s):
    return codecs.getdecoder('hex')(re.sub('[^0-9a-fA-F]', '', s))[0]

deltas = gzip.open('deltas.gz').read().decode()
lines = deltas.split('\n')
pairs = [(l[:53], l[56:]) for l in lines]
columns = ['\n'.join([p[i] for p in pairs]) for i in range(2)]
left = columns[0].splitlines(keepends=True)
right = columns[1].splitlines(keepends=True)

'''there are interpolated lines in the left-hand column that don't appear in the right-hand column'''
import difflib

column_diffs = list(difflib.Differ().compare(left, right))
#print(column_diffs)
#print('=====')
import pprint
# pprint.pprint(column_diffs)
pngs = [''.join([l for l in column_diffs if l[0] == d]) for d in " +-"]
#print(pngs)
for i in range(len(pngs)):
    open('delta%d.png' % i, 'wb').write(unhex(pngs[i]))
