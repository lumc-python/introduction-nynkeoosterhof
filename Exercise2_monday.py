#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 12:55:27 2017

@author: nynkeoosterhof
"""


# Make a short tandem repeat that consists of three "ACGT" units and five "TTATT" units.
unit1 = 'ACGT'
unit2 = 'TTATT'
sequence = 3 * unit1 + 5 * unit2

# Print all suffixes of the repeat structure.
for i in sequence:
    print sequence
    sequence = sequence[1:]

# Print all substrings of length 3
sequence = 3 * unit1 + 5 * unit2

for i in sequence:
    if (len(sequence) > 2):
        print sequence[0:3]
    sequence = sequence[1:]

# Print all unique substrings of length 3
sequence = 3 * unit1 + 5 * unit2

unique_elements = set()

for i in sequence:
    if (len(sequence) > 2):
        unique_elements.add(sequence[0:3])
    sequence = sequence[1:]
print unique_elements


