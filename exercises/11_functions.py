#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


# Excercises
# ==========
#
# Try to fill in your own code at the [CODE] markers.


###############################################################################
# a) A function and its usage

def power(x, n):
    '''
    This is a documentation string, which (hopefully) contains
    helpful information about the function.
    This functions computes the n-th power of x. You can compare
    the results by calculating `x**n` (yes, python has its own
    `power` implementation).
    '''
    y = 1
    for i in range(n):
            y = y * x
    return y

# now calculate the 8-th power of 2 and print it

print("a)")

# [CODE]

print("")


###############################################################################
# b) My first function
#
# Implement the `n!` function:
#   fac(n) == n*(n-1)*(n-2)*...*2*1
#
# Hint: There are two main ways to implement the factorial function, you can try
# both!
#       - recursive: fac(1) = 1, fac(n+1) = (n+1)*fac(n)
#       - iterative: a `for` loop

def fac(n):
    f = 1

    #[CODE]

    return f

print("b)")
print("fac(5) = {}".format(fac(5)))
print("")

###############################################################################
# c) More functions
#
# Welcome back to the email address program. Create a function `isEmailAddress()`
# that returns a boolean value for an input string. The value should only be
# `True` if
#       - the address contains exactly one '@' sign
#       - the '@' sign is not the first character of the string
#       - the address ends in one of the TLDs listed in variable `tlds`
# Can you think of other requirements regarding email address validity?
# Check your function on the example email addresses, and feel free to add more
# examples that you would like to check.

tlds = ['de', 'com', 'org', 'uk', 'at', 'ch', 'net']

example_addresses = ['mail@example.org',  # valid
                     'me@test.invalid',  # invalid
                     'http://google.com',  # invalid
                     'another@one.de',  # valid
                     '@test.ch',  # invalid
                     ]

#[CODE]

