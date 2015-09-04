#!/usr/bin/env python


"""

String surfer is a collection of functions for manipulating strings.

If I didn't write it check the comment above for credit.

"""

__author__		= "Leo Mahon"
__copyright__	= "Copyright 2015, Leo Mahon"


# Find all sub strings
# Credit Karl Knechtel and Pratik Deoghare 
# http://stackoverflow.com/questions/4664850/find-all-occurrences-of-a-substring-in-python
def find_all(sub , a_str):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) 


# Find all sub strings including overlaps
def find_all_overlap(sub, a_str):
	start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1