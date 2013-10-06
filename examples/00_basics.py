#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


# You can run this program
#   - in IDLE, by hitting F5 (or selecting Run->Run Module)
#   - in the console, by typing `python 10_variables.py` (Mac/Linux)
#     (make sure that you are in the right directory)


# Basics
# ======

# This is an assignment to a variable. In Python, variables are declared by
# assigning to them (you don't need to tell the interpreter that you are going
# to use a variable in advance).
n = 12

# This is a statement. It gets evaluated, but no assignment is taking
# place here (there's no 'equals' sign).
(5 + 4) * 2

# This is a function call. Functions are used like in mathematics, they get 
# one or more inputs and return an output. The function called here is `print`,
# which writes the argument to stdout<0> (e.g., the IDLE python console).
print(n)

# Function arguments can also be statements, like in the following instruction.
# The statement gets evaluated first, the result is passed as an argument to the
# function. 
print(5 - n)

# Strings are sequences of characters and are denoted by single or double
# quotation marks (`'` or `"`)
s1 = "this is a string"
s2 = 'this is another'

# Strings can also be concatenated, and printed.
print("Hello World!")
print(s1 + ", " + s2)

# We will sometimes use `print` to decorate the output that we're creating, like
# in the following piece of code.

print("")  # print a blank line
print("The result of `print(5-n)` is:")  # print informative text
print(5-n)  # print the actual result
print("")   # another blank line

# In principle, statements are constructed from
#       - operations, like `+`, `*`, ...
#       - primitives, like `0`, `42.0`, ...
#       - variables that have been defined earlier
#       - brackets for grouping `()`
#       - function calls, like `print()`
# Statements can be assigned to variables, or passed to functions
example = (5 + 4) * 3
example = example - 2

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
myBoolean = True

# So called 'iterables', which can be accessed item-by-item. We look at the 
# string type in this example, but tuples and lists are indexed in the same
# way. 
myString = "abcdefghijklmnopqrstuvwxyz"
myTuple = (1, 'b', 0.1)
myList = [2, 'c', 0.2]

# Items of strings, tuples and lists can be accessed by their index. Indices
# in python always start at 0!
print("The first character of the string variable `myString` is:")
print(myString[0])
print("")

# The statement `3:12` is 'slice notation', a range given as `start:stop`. Note
# that the last item (the item at index 12) is not included. Slice notation is
# only valid inside square brackets.
print("A sequence of characters inside variable `myString`:")
print(myString[3:12])
print("")

# One or two ends of the slice may be open.
print("The first 11 characters:")
print(myString[:11])
print("The characters from 11 to the end:")
print(myString[11:])
print("")

# All iterables can be counted by using the function len()
print("The lenght of variable `myString` is")
print(len(myString))
print("")

# All iterables can be concatenated with others of the corresponding type.
print("Concatenated lists:")
print(["list", 1] + ["list", 2] + ["both"])
print("")


# <0> Don't worry about this if you're using windows, it's just some sort
#     of sink for all your textual program outputs. 
#
# <1> This is not to be taken too serious, rather as a
#     [Wittgenstein's ladder](http://en.wikipedia.org/wiki/Lie-to-children). The
#     concept of primitive data types is not really a part of python, instead 
#     everything in python is an object.


