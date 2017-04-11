# *-* coding:UTF-8 *-*
import hashlib
broken = open('mybroken.zip', "rb").read()
for i in range(len(broken)):
    for j in range(256):
        repaired = broken[:i] + bytes([j]) + broken[i + 1:]
        if hashlib.md5(repaired).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
            open('unbroken.zip', 'wb').write(repaired)
            print(i, j)
            raise StopIteration
