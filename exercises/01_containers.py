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


# ==========
# Excercises
# ==========
#
# Try to fill in your own code at the [CODE] markers.
# Interesting list methods
# (http://docs.python.org/2/library/stdtypes.html#mutable-sequence-types):
#       - list.append()
#       - list.insert()
#       - list.remove()
#       - list.reverse()
#       - list.sort()
#       - list.count()

# comment out the following two lines when you are ready for the excercises
import sys
sys.exit(0)

# Lists
# =====

###############################################################################
# a) Define your own list of at least 4 integers, print it.

print("a)")

#[CODE]

print("")


###############################################################################
# b) Print out the length of the list (NOT: print(4)).

print("b)")
print("Length of the variable `container`:")

#[CODE]

print("")


###############################################################################
# c) Sort the list and print it.

print("c)")
print("The list after sorting:")

#[CODE]

print("")


###############################################################################
# d) Look at the following lines of code. What will the list look like at the
#    end? Assign your guess to the variable `guess`.

lst = ["blood", "sugar", "sex", "magick"]
lst.sort()
lst.reverse()
lst.insert(2, "smurfs")
lst.remove(1)

guess = []  # [CODE]

print("d)")
# don't worry about the stuff below right now

assert len(guess) == len(lst), \
    "FAIL: Your list is too {} to be correct".format(
        "short" if len(guess) < len(lst) else "long")
for g, i in zip(lst, guess):
    assert g == i, "FAIL: First incorrect item of your list: {}".format(g)
print("CORRECT: Your guess is correct!")
