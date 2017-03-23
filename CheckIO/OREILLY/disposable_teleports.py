#!/usr/bin/env python
# *-* coding:UTF-8 *-*


def ConstuctPath(teleport_map, start):
	ret=[""]
	for (x,y) in teleport_map:
		param=set(teleport_map)
		param.remove((x,y))
		if x==start:
			for r in ConstuctPath(param,y):
				ret.append(str(x)+str(y)+","+r)
		elif y==start:
			for r in ConstuctPath(param,x):
				ret.append(str(y)+str(x)+","+r)
	return ret


def checkio(teleports_string):
	teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_string.split(",")]
	paths=ConstuctPath(teleports_map,1)
	for p in paths:
		if p.endswith("1,") and len(set(p))==9:
			res=[]
			for _ in p[:-1].split(","):
				res.append(_[0])
			res.append("1")
			return "".join(res)

#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"