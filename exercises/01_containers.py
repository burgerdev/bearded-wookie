#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


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


###############################################################################
# a) Assign your own list of at least 4 integers to a variable `container`, 
#    print it.

print("a)")

container = [1,3,2,5,4,7,6]
print(container)

print("")


###############################################################################
# b) Print out the length of the list (NOT: print(4)).

print("b)")
print("Length of the variable `container`:")

print(len(container))

print("")


###############################################################################
# c) Sort the list and print it.

print("c)")
print("The list after sorting:")

container.sort()
print(container)

print("")


###############################################################################
# d) Look at the following lines of code. What will the list look like at the
#    end? Assign your guess to the variable `guess`.

lst = ["blood", "sugar", "sex", "magick"]
lst.sort()  # blood magick sex sugar
lst.reverse()  # sugar sex magick blood
lst.insert(2, "smurfs")  # sugar sex smurfs magick blood
lst.pop(1) # sugar smurfs magick blood

guess = ["sugar", "smurfs", "magick", "blood"]  # [CODE]


# don't worry about the stuff below right now, it just checks your result
print("d)")

if len(guess) > 0:
    assert len(guess) == len(lst), \
        "FAIL: Your list is too {} to be correct".format(
            "short" if len(guess) < len(lst) else "long")
    for g, i in zip(lst, guess):
        assert g == i, "FAIL: First incorrect item of your list: {}".format(i)
    print("CORRECT: Your guess is correct!")
