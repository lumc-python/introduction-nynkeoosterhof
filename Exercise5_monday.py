#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:29:34 2017

@author: nynkeoosterhof
"""

def F(x):
    return x * x

# Make a dictionary containing all squares smaller than 100.
dict = {}

x = 1
while (F(x) < 100):
    dict.update({x:F(x)})
    x += 1

# Print the content of this dictionary in english, e.g., "4 is the square of 2".
for i in dict.keys():
    print ('{} is the square of {}'.format(dict[i],i))

