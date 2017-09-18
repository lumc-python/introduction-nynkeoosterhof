#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:29:34 2017
@author: nynkeoosterhof
"""


#Remember the previous exercise of finding unique substrings of length 3.
# Make a function from your implementation.
# Have k as an argument to the function.

unit1 = 'ACGT'
unit2 = 'TTATT'
sequence1 = 3 * unit1 + 5 * unit2
sequence2 = unit1 + unit2 * 2 + unit1 * 5
sequence3 = unit2 * 3 + unit1 + unit2

def find_substrings2(s, k):
    unique_elements = set()
    for i in s:
        if (len(s) > k - 1):
            unique_elements.add(s[0:k])
        s = s[1:]
    return unique_elements

print 'sequence1', find_substrings2(sequence1, 3)
print 'sequence2', find_substrings2(sequence2, 3)
print 'sequence3', find_substrings2(sequence3, 3)

# Modify your function to use a dictionary with substring counts.

def find_substrings(s, k):
    """Make dictionary of k-mer counts in a sequence"""
    copy_s = s
    unique_elements = find_substrings2(copy_s, k)
    dict_sequence = {}
    for i in unique_elements:
        dict_sequence.update({i:s.count(i)})
    return dict_sequence

print 'sequence1', find_substrings(sequence1, 3)
print 'sequence1_2', find_substrings(sequence2, 3)
print 'sequence2', find_substrings(sequence3, 3)
print 'sequence2_2', find_substrings(sequence1, 4)
print 'sequence3', find_substrings(sequence1, 4)
print 'sequence3_2', find_substrings(sequence1, 4)




    
    



