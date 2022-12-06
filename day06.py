# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 08:42:19 2022

@author: Simon
"""
import timer


with open('day06_input.txt', 'r') as f:
    c = f.read()

timer.start()
#%% part 1
# this one is so short, I'm not writing any comments. lol.
# Today's non-comments are dedicated to Juli Nail.
# check back in tomorrow for more comments

quadrupels = [set(c[i:i+4]) for i in range(len(c))] 
length = [len(quad) for quad in quadrupels] 

# ok there is one comment. I lied.
# +1 for python offset and +3 for the chars themselve
idx_start = length.index(4) + 1 + 3

print(f'Communication starts at {idx_start}')

#%% part 2
quattuordecimtuples = [set(c[i:i+14]) for i in range(len(c))] 
length = [len(quad) for quad in quattuordecimtuples] 

idx_start = length.index(14) + 1 + 13
print(f'Message starts at {idx_start}')

timer.stop()
