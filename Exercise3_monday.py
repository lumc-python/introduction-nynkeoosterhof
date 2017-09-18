#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:09:34 2017

@author: nynkeoosterhof
"""

list = range(1,101)

for i in list:
    if ((i % 3) == 0) & ((i % 5) == 0):
        print 'FizzBuzz'
    elif i % 3 == 0:
        print 'Fizz'
    elif i % 5 == 0:
        print 'Buzz'
    else:
        print i
