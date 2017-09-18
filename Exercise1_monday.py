# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

list1 = range(10)
list1.reverse()

for i in list1:
    if i == 0:
        print """No more bottles of beer on the wall, no more bottles of beer. 
        Go to the store and buy some more, 99 bottles of beer on the wall."""
    else:
        print i, 'bottles of beer on the wall,', i, """bottles of beer.
        Take one down and pass it around,""", i - 1, 'bottles of beer on the wall.'

