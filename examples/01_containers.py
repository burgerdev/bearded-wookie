#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


# Lists
# =====
#
# Lists are a mutable container type, which means you can change the content of
# an existing list. Lists are defined with square brackets `[]` and can contain
# every data type, even another list.

myList = [12, 12.21, "hello", ["another", "list"]]

# Lists are indexed exactly like tuples, but with lists, assignment is also
# an option.

print("Variable `myList` before changing it")
print(myList)
print("")

myList[2] = "something else"

print("Variable `myList` after changing it")
print(myList)
print("")


# Lists are (like the other primitives) 'objects'. Objects have so called
# 'methods', which perform operations on a specific object.
# Note that some methods take arguments
#       `object.method(arg1, arg2)`
# while some others don't, and all methods return values
#       `returnValue = object.method(arg1)`
# Sometimes however, the return value can be `None`. 
# The concept of methods, functions and objects will become clearer after the
# next sections.

# Methods are used as follows:
myList.append(100)  # appends the integer `100` to the end of the list.

print("Variable `myList` after appending to it")
print(myList)
print("")

myList.reverse()  # reverse the order of the list items, this is done 'in place'

print("Variable `myList` after reversing it")
print(myList)
print("")


