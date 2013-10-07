#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Markus Döring


# Functions
# =========

# Functions are used if you want to use the same code for multiple things. For 
# example, you might want to write a greeting message for some persons, like
# this. 

print("Hello, Markus! Welcome to the tutorial!")
print("Hello, Steve! Welcome to the tutorial!")
print("Hello, Guybrush! Welcome to the tutorial!")
# ...

# Copy-Pasting code like this is not just an effort that you can avoid, it is
# considered bad style. Good thing that python gives us the possibility to wrap
# up reusable code in functions.

def greeting(name):
    s = "Hello, " + name + ". "
    s = s + "Welcome to the tutorial!"
    print(s)

greeting("Markus")
greeting("Steve")
greeting("Guybrush")

# This type of programming not only reduces effort, but it helps you to maintain
# your code with ease. Suppose you want to change the greeting from "Hello" to
# "Howdy". In the first example, you would have to change it at 3 locations, with
# the function definition you hust have to change it once.

# Functions have inputs, like mathematical functions. They are defined in the 
# definition: `def function(input1, input2, input3). You can also define functions
# without inputs.

def greeting2(message, name):
    s = message + ", " + name + ". "
    s = s + " Welcome to the tutorial!"
    print(s)

greeting2("Howdy", "Markus")
greeting2("Ave", "Cesar")

# Functions can also return values. You simply have to tell python to return your
# variable or your statement by using the `return` keyword.

def calc(a, b):
    c = a + b
    return c


