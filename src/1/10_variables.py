#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


# Basics
# ======

# This is a commented line

# `pass` is a so called 'zero operation', which does nothing
pass  # You can also comment at the end of a line of code

# This is a statement. It gets evaluated, but no assignment is taking
# place here
(5 + 4) * 2

# This is an assignment to a variable. In Python, variables are declared by
# assigning to them (you don't need to tell the interpreter that you are going
# to use a variable in advance).
n = 12

# In principle, statements are constructed from
#       - operations, like `+`, `*`, ...
#       - primitives, like `0`, `1e9`, `42.0`, ...
#       - variables that have been defined earlier
#       - brackets for grouping `()`
#       - function calls, like `print()`
# Statements can be assigned to variables, or passed to functions
example = (5 + 4) * 3
example = example - (8 % 3)

print("The content of the variable `example` is now")
print(example)
print("")

print("The remainder of the division `example / 2` is")
print(example % 2)
print("")


# Simple Types - Primitives
# =========================
#
# Primitive types are basic building blocks of a computer program. There are a
# few primitive types in python<1>, also called builtins:
#       - None
#       - boolean, one of `True` and `False`
#       - integer, like `4`, `-31337`
#       - float, like `41.0`
#       - string, like `"Hello World"`
#       - tuple, like `(15, 0, 3.4, -1, "abc")`
#       - list, like `[15, 0, 3.4, -1, "abc"]`
#       - dictionary, like `{'ham': 'egg', 'tree': 'bark', 'dog': 'bark', 0: 1}`
#       - set, like `{23, 'ham', 12}`
# The first six types are 'immutable', which means they cannot be modified by
# the program.

## Really basic types:
myInteger = 1
myFloat = 2.3

## So called 'iterables', which can be accessed item-by-item:
myString = "these are multiple characters"

# Items of strings, tuples and lists can be accessed by their index. Indices
# in python always start at 0!
print("The first character of the string variable `myString` is:")
print(myString[0])
print("")

# The statement `3:12` is 'slice notation', a range given as `start:stop`. Note
# that the last item (the item at index 12) is not included.
print("A sequence of characters inside variable `myString`:")
print(myString[3:12])
print("")

# All iterables can be counted by using the function len()
print("The lenght of variable `myString` is")
print(len(myString))
print("")


# ==========
# Excercises
# ==========
#
# Try to fill in your own code at the [CODE] markers.

# comment out the following two lines when you are ready for the excercises <2>
import sys
sys.exit(0)

# HINT: commenting out would look like this:

# import sys
# sys.exit(0)

# or like this:

'''
import sys
sys.exit(0)
'''


# Simple Assignment
# =================
#
# Try to assign the number `4` to the variable `a`, the
# number `5` to the variable `b` and to assign the sum
# of both `a` and `b` to the variable `c`. Print `c`.
#
# You can run this program
#   - in IDLE, by hitting F5 (or selecting Run->Run Module)
#   - in the console, by typing `python 10_variables.py` (Mac/Linux)
#     (make sure that you are in the right directory)


#[CODE]


# Tuples
# ======
#
# We try the same indexing that we did for strings on tuples.

myTuple = (4, 15, "Hello", 3.0, ("tuple in a tuple", 17), "foo")

print("The third element of tuple `myTuple` is:")
#[CODE]

print("The subtuple from index 3 to index 5 (including 5!) is:")
#[CODE]



# <1> This is not to be taken too serious, rather as a
# [Wittgenstein's ladder](http://en.wikipedia.org/wiki/Lie-to-children). The
# concept of primitive data types is not really a part of python, instead 
# everything in python is an object.
# <2> These lines let the program exit, so that you just see the examples
# when you run it for the first time.
