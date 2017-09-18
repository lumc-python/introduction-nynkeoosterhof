#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:29:34 2017
@author: nynkeoosterhof
"""


#Remember the previous exercise of finding (unique) substrings of length 3.
# Make a function from your implementation.
# Have k as an argument to the function.

unit1 = 'ACGT'
unit2 = 'TTATT'
sequence1 = 3 * unit1 + 5 * unit2
sequence2 = unit1 + unit2 * 2 + unit1 * 5
sequence3 = unit2 * 3 + unit1 + unit2

def find_substrings(s, k):
    unique_elements = set()
    for i in s:
        if (len(s) > k - 1):
            print s[0:k]
            unique_elements.add(s[0:k])
        s = s[1:]
    print unique_elements

# Test the function on several input strings.
find_substrings(sequence1, 3)
find_substrings(sequence2, 3)
find_substrings(sequence3, 3)

# Modify your function to use a dictionary with substring counts.

def find_substrings(s, k):
    """Make dictionary of k-mer counts in a sequence"""
    unique_elements = set()
    copy_s = s
    for i in copy_s:
        if (len(copy_s) > k - 1):
            print copy_s[0:k]
            unique_elements.add(copy_s[0:k])
        copy_s = copy_s[1:]
    dict_sequence = {}
    for i in unique_elements:
        dict_sequence.update({i:s.count(i)})
    return dict_sequence

dict_sequence1 = find_substrings(sequence1, 3)
dict_sequence2 = find_substrings(sequence2, 3)
dict_sequence3 = find_substrings(sequence3, 3)
dict_sequence1_2 = find_substrings(sequence1, 4)
dict_sequence2_2 = find_substrings(sequence1, 4)
dict_sequence3_2 = find_substrings(sequence1, 4)

print dict_sequence1
print dict_sequence1_2
print dict_sequence2
print dict_sequence2_2
print dict_sequence3
print dict_sequence3_2


    
    



