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

result = calc(5, 17)
print(result)


print("")
print("Scope")

# You have to be careful with variables that are declared inside of functions. 
# The visibility of the variable is called its 'scope'. If you assign to a 
# variable inside a function for the first time, it is only visible within the 
# function.

def fun():
    a = 2
    print(a)

# The following results in an error (NameError: name 'a' is not defined). 
# >>> print(a) 

# If the variable name was also used outside of the function, its contents are 
# unchanged by assignments inside a function.

print("")

a = 1

def myPrint():
    a = 2
    print(a)

print(a)  # this prints 1
myPrint()  # this prints 2
print(a)  # this still prints 1, the original a is left unchanged by the function

# Scope is unidirectional, you can use variables that are defined outside of a
# function in the function itself. Note however, that this is in most situations
# considered bad style. Try to use function arguments for that.

a = 1

def myPrint():
    print(a)

print(a)
myPrint()

# Be careful when using mutable types, they can be changed inside of functions!

print("")
print("Mutable Types")

lst = [0,1,2]

def screwList(lst):
    lst[0] = "HAHA!"
    lst.pop(1)

print(lst)
screwList(lst)
print(lst)

