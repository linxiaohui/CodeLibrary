#!/usr/bin/env python
# *-* coding:UTF-8 *-*

def digit_stack(commands):
    s=0
    stack=[]
    for cmd in commands:
        if cmd.startswith("PUSH"):
            stack.append(int(cmd.split(" ")[1]))
        else:
            if len(stack)!=0:
                if cmd=="PEEK":
                    s+=stack[-1]
                else:
                    s+=stack.pop()
    return s

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
