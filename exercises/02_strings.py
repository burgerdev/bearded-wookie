#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


# There are many exciting string methods, just take a look around in the
# documentation. Recommended reading:
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

ratedPG = insult.replace('damn', '***')

print("a)")
print(insult + " -> " + ratedPG)
print("")


###############################################################################
# b) Remove all leading and trailing whitespace characters, store your result
#    in a variable `accepted`.

challenge = """


   Good luck removing all the whitespace I posted. HAHA!


"""

accepted = challenge.strip()

print("b)")
print("Challenge accepted: {}".format(accepted))
print("")


###############################################################################
# c) Join a given list of strings together, seperated by the string `"; "`.
#    Don't do it manually (`lst[0] + "; " + list[1] + ` ...)!
#    Hint: Try to find out the mechanics of str.join().

lst = ["Apples", "Oranges", "Eggplants"]

joined = "; ".join(lst)

print("c)")
print("Joined list: {}".format(joined))
print("")




