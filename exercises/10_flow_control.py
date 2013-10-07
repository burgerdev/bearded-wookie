#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


# Excercises
# ==========
#
# Try to fill in your own code at the [CODE] markers.


###############################################################################
# a) Simple for
#
# Print all integers from 0 to 32 that are divisible by 2. The [CODE] markers 
# denote the lines which should be replaced with meaningful instructions.
# HINT: 
#   - An integer n is divisible by to if n = 2*m holds for an integer m. 
#   - You don't need to use `if-else` here if you use hint (1)

print("a)")

maxM = 16
for m in range(maxM):
    n = 2*m
    print(n)

print("")


###############################################################################
# b) Advanced for
#
# Print all strings in variable `myStrings` in upper case. 
# HINT:
#   - You can use any iterable (e.g., a list) as a replacement for `range()`

myStrings = ["This", "is", "not", "the", "algorithm"]

print("b)")

for string in myStrings:
    print(string.upper())

print("")


###############################################################################
# c) Simple if-else
# 
# Print all integers from 0 to 32 that are divisible by 2.
# HINT:
#   - An integer n is divisible by 2 if and only if 
#       n modulo 2 == 0
#   - In python, you can use the modulo operator `%`
#       n % 2 == 0 ?
#

print("c)")

for n in range(32):
    if n % 2 == 0:
        print(n)

print("")

###############################################################################
# d) Advanced if-else
# 
# Print all integers from 0 to 32 that are divisible by 2, but not by 3.
# HINT:
#   - you can use the keywords `and`, `or`, `not` to work with booleans
#       c = a and b
#       c = b or not a
#       ...
#     Remember that `not` binds stronger than `and` or `or`!
#


print("d)")

for n in range(32):
    if n % 2 == 0 and n % 3 != 0:
        print(n)

print("")






