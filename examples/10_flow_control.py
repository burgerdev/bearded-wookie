#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


# Flow Control
# ============

# At some point during your progress through this tutorial, you might want to 
# handle input depending on its value. Sticking with the email example, you
# might want to send an email only if the address is correct. Or you might only
# want to print a string, if its length is within reasonable bounds. This can 
# be done with so called `if` and `else` statements. But before we do this, we 
# have to talk about whitespace. 

# Unlike most other programming languages, whitespace (tabulators, spaces, line
# feeds) matters in python. The interpreter detects indented blocks (blocks
# that begin with 4 spaces), and executes them as subprograms. You can execute
# an indented block by making use of the `if-else` keywords.

s = "Hallo Welt!"
#s = "abc"*400

if len(s) > 1000:
    print("Your string is too long for printing!")
else:
    print(s)

# Indented blocks can also be nested, and the `else` statement can be omitted
# if you don't want an alternative execution path.

if "Hallo" in s:
    
    if "Welt" in s:
        print("Your string looks familiar...")
    else:
        s = s + " Welt!"
        print("I modified your string to look more like the strings I know.")

# There's also a keyword `elif` as an abbreviation for `else: if`.

if len(s)>5000:
    print("Your string is very long")
elif len(s)>200:
    print("Your string is quite long")
else:
    print("Your string has a nice length.")

        

