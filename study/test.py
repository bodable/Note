#!/usr/bin/python
#-*- coding:utf8 -*-

item_list = ["a", "b", "c"]
result = []
"""
for item in item_list:
    #new_item = do_something_with(item)
    print item
    result.append(item)
"""


def do_something_with(item):
    print item

"""
#生成list
result = [item for item in item_list]
#生成iterator
result = (item for item in item_list)
print result

"""
old_list = [1, 2, 3]

doubled_list = map(lambda x: x * 2, old_list)

print doubled_list

from functools import reduce

