#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Friends:
    def __init__(self, connections):
        self.nodes=set()
        self.edges=set()
        for (x,y) in connections:
            self.nodes.add(x)
            self.nodes.add(y)
            self.edges.add((x,y))
            self.edges.add((y,x))

    def add(self, connection):
        (x,y)=connection
        if (x,y) in self.edges:
            return False
        self.nodes.add(x)
        self.nodes.add(y)
        self.edges.add((x,y))
        self.edges.add((y,x))
        return True

    def remove(self, connection):
        (x,y)=connection
        if (x,y) not in self.edges:
            return False
        self.edges.remove((x,y))
        self.edges.remove((y,x))
        return True       

    def names(self):
        self.h=set()
        for (x,y) in self.edges:
            self.h.add(x)
            self.h.add(y)
        return self.h

    def connected(self, name):
        self.friends=set()
        for (x,y) in self.edges:
            if x==name:
                self.friends.add(y)
            if y==name:
                self.friends.add(x)
        return self.friends


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"