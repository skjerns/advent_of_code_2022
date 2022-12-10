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

X = [1]

for command in commands:
    match command.split(' '):
        case ['noop']:
            X.append(X[-1])
        case ['addx', n]:
            X.append(X[-1])
            X.append(X[-1] + int(n))

# the index has to be -1 as we already start with one value in the register
signal_strength = [X[i-1]*i for i in range(20, len(X), 40)]
print('\nsignal_strength is', sum(signal_strength), signal_strength)

#%% Part 1

n_rows = 6
n_cols = 40

rows = []

CRT = '\n'

X_copy = X[::-1]

for r in range(n_rows):
    for c in range(n_cols):
        sprite_pos = X_copy.pop()
        if abs(c-sprite_pos)<2:
            CRT += '█'  # use block char for better readability
        else:
            CRT += ' '
    CRT += '\n'
    
    
print(CRT)
timer.stop()