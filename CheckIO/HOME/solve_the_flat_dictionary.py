#!/usr/bin/env python
# -*- coding:utf-8 -*-  

def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if v=={}:
                result["/".join((path + (k,)))] = ""
            if isinstance(v, dict):
                stack.append((path + (k,), v))
            else:
                result["/".join((path + (k,)))] = v
    return result


def flatten2(dictionary):
	result={}
	for k,v in dictionary.items():
		if v=={}:
			result[k]=""
		elif isinstance(v,dict):
			D=flatten(v)
			for kk,vv in D.items():
				result[k+"/"+kk]=vv
		else:
			result[k]=v
	return result


print flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) 

print flatten({"empty": {}}) 

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}