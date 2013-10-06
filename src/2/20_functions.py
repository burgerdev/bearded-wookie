#!/usr/bin/env python

# Function Definition
# ===================
#


# Excercises
# ==========
#
# Try to fill in your own code at the [CODE] markers. 


###################################################################
# a) A function and its usage

def power(x,n):
	'''
	This is a documentation string, which (hopefully) contains 
	helpful information about the function.
	This functions computes the n-th power of x.
	'''
	y = 1
	for i in range(n):
		y = y * x
	return x

# now calculate the 8-th power of 2 and print it

print("a)")

# [CODE]

print("")


###############################
# b) My first function

# Implement the `n!` function: 
#   fac(n) == n*(n-1)*(n-2)*...*2*1

def fac(n):
	return 0 #[CODE] (remember to keep your code indented)

print("b)")
print("fac(5) = {}".format(fac(5)))
print("")
