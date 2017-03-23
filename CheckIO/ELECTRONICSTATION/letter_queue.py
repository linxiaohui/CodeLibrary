#!/usr/bin/env python
# *-* coding:UTF-8 *-*

def letter_queue(commands):
    q=[]
    for cmd in commands:
        if cmd.startswith("PUSH"):
            q.append(cmd.split(" ")[1])
        else:
            if len(q)>0:
                q.pop(0)
    return "".join(q)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
