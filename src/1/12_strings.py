#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


# String Manipulation
# ===================
#
# Now we will start playing around with strings. Remember
# that the string class is immutable, which means that
# you cannot change the characters of a given string. 
# However, you can use string methods to create a new string
# that is changed in the way you like. 
#
# You can find much information in the 
# [documentation](http://docs.python.org/2/library/stdtypes.html#string-methods)


# Strings (sequences of characters) are defined by putting
# them into quotation marks. 
# >>> a = "Hello"
# >>> b = 'World'

# The `print()` command does what it is supposed to do:
# >>> print(a)
# Hello

# strings can be joined by the `+` operator
# >>> greeting = a + " " + b + "!"
# >>> print(greeting)
# Hello World!

# even multi-line strings are allowed with triple-quotation (multi-line strings
# can also be used as code comments)
# >>> longstring = """Hello,
# World!"""
# >>> print(longstring)
# Hello,
# World!

# you can select substrings
# >>> d = greeting[0:5]
# >>> e = longstring[7:12]

# strings are compared with the `==` (equals) operator
# >>> print(a == d == "Hello")
# True
# >>> print(e == "World")
# True

# Strings are immutable, you can't assign to a string
# >>> a = "Hello, world!"
# >>> a[0:5] = "Adios"
# TypeError: 'str' object does not support item assignment

# Good string replacement example
# >>> a = "Hello, world!"
# >>> b = a.replace("Hello", "Goodbye")
# >>> print(b)
# Goodbye, world!

# There are many more exciting string methods, just 
# take a look around in the documentation. Recommended
# reading:
#	- str.strip()
#	- str.split()
#	- str.join()
#	- str.find()
#	- str.lower()
#	- str.upper()
#	- str.startswith()
#	[- str.format(), be patient with this one, it will 
#	   be clearer later on]


# Excercises
# ==========
#
# Try to fill in your own code at the [CODE] markers. 


###############################################################################
# a) Try replacing `damn` with `***` (no need to count characters!), store your
#    result in a variable `ratedPG`.

insult = "You are a damn fool!"

ratedPG = ""  # [CODE]

print("a)")
print(insult + " -> " + ratedPG)
print("")


###############################################################################
# b) Remove all leading and trailing whitespace characters, store your result
#    in a variable `accepted`.

challenge = """


   Good luck removing all the whitespace I posted. HAHA!


"""

accepted = ""  # [CODE]

print("b)")
print("Challenge accepted: {}".format(accepted))
print("")


###############################################################################
# c) Join a given list of strings together, seperated by the string `"; "`.
#    Don't do it manually (`lst[0] + "; " + list[1] + ` ...)!
#    Hint: Try to find out the mechanics of str.join().

lst = ["Apples", "Oranges", "Eggplants"]

joined = ""  # [CODE]

print("b)")
print("Joined list: {}".format(joined))
print("")




