#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


# You can run this program
#   - in IDLE, by hitting F5 (or selecting Run->Run Module)
#   - in the console, by typing `python 10_variables.py` (Mac/Linux)
#     (make sure that you are in the right directory)


# ==========
# Excercises
# ==========
#
# Try to fill in your own code at the [CODE] markers.

###############################################################################
# a) Simple Assignment
# ====================
#
# Try to assign the number `4` to the variable `a`, the
# number `5` to the variable `b` and to assign the sum
# of both `a` and `b` to the variable `c`. Print `c`.

print("a)")
print("Variable c is now:")

a = 4
b = 5
c = a + b
print(c)

print("")


###############################################################################
# b) Strings
# ==========
#
# Let's say we have a program that validates email addresses. To do this, we 
# have to check (among other things)
#       - that it contains an '@' sign
#       - that it has a German TLD ('.de' at the end)
# Save the (boolean results) in the variables `containsAt` and `isGermanTLD`,
#  and print them. 
#
# Hints:
#       - You can check whether a string contains another string with the `in`
#         keyword, and whether a string is equal to another one with `a == b` 
#       - Strings (and other container types) can be indexed from the end by
#         using negative numbers: `s[-3:-2]` would give the third-from-last
#         character. To include the last character in your selection, you might
#         need to use `len(s)`.

email = "test@example.de"

print("b)")

containsAt = '@' in email
isGermanTLD = email[-2:len(email)] == "de"

print(containsAt)
print(isGermanTLD)

print("")


###############################################################################
# c) Tuples
# =========
#
# We try the same indexing that we did for strings on tuples.


myTuple = (4, 15, "Hello", 3.0, ("tuple in a tuple", 17), "foo")

print("c)")

print("The third element of tuple `myTuple` is:")
print(myTuple[2])

print("The subtuple from index 3 to index 5 (including 5!) is:")
print(myTuple[3:6])

print("The last two elements of the tuple are:")
print(myTuple[-2:len(myTuple)])



