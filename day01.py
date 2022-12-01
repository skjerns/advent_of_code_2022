# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 08:32:27 2022

@author: Simon Kern @skjerns
"""

with open('day01_input.txt', 'r') as f:
    c = f.read()
    
elves = c.split('\n\n')
elves = [elve.strip().split('\n') for elve in elves]

calories = [sum([int(n) for n in elve]) for elve in elves]
calories = sorted(calories)

print(calories[-1])         # star 1
print(sum(calories[-3:]))   # star 2
