# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 06:11:11 2022

@author: Simon
"""

import timer


with open('day10_input.txt', 'r') as f:
    c = f.read()
    
#%% Part 1
timer.start()
commands = c.split('\n')[:-1]

# pretend the register is a list, so we can easier keep track of what happened
X = [1]

# loop through commands
for command in commands:
    match command.split(' '):
        case ['noop']:
            X.append(X[-1])  # repeat previously register value
        case ['addx', n]:
            X.append(X[-1])  # repeat previously register value
            X.append(X[-1] + int(n))  # only add in second cycle

# the index has to be -1 as we already start with one value in the register
signal_strength = [X[i-1]*i for i in range(20, len(X), 40)]
print('\nsignal_strength is', sum(signal_strength), signal_strength)

# prints: signal_strength is 14560 [420, 1260, 2100, 2380, 3780, 4620]

#%% Part 1

n_rows = 6
n_cols = 40

CRT = '\n'

for r in range(n_rows):
    for c in range(n_cols):
        sprite_pos = r*n_cols +c
        sprite_val = X[sprite_pos]
        # if sprite is overlapping with current cycle position: print char
        if abs(c-sprite_val)<2:
            CRT += '█'  # use block char for better readability
        else:
            CRT += ' '
    CRT += '\n'
    
    
print(CRT)

# this apparently prints
# █  █ █   █ ██   ██
# █ █  █   █ █ █ █
# ██   █   █ ██   █ 
# █ █  █   █ █     █
# █ █  █   █ █     █
# █  █ ███ █ █   ██
# seriously. you don't believe me?
timer.stop()