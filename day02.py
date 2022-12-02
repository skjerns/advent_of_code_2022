# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 08:35:46 2022

@author: Simon
"""

scores = {x:i+1 for i, x in enumerate(['rock', 'paper', 'scissors'])}

mapping1 = {'A': 'rock',
            'B': 'paper',
            'C': 'scissors',
            'X': 'rock',
            'Y': 'paper',
            'Z': 'scissors'}

with open('day02_input.txt', 'r') as f:
    matches = [l.strip() for l in f.readlines()]    


#%% part 1
points = 0
for match in matches:
    signs = match.split(' ')
    # print(signs)
    points += ord(signs[1])-87 # add 1 for rock, 2 for paper 3 for scissor
    
    sign1, sign2 = mapping1[signs[0]], mapping1[signs[1]]
    
    if sign1==sign2:
        points += 3

    elif sign1=='paper' and sign2=='scissors':
        points += 6
        
    elif sign1=='scissors' and sign2=='rock':
        points += 6

    elif sign1=='rock' and sign2=='paper':
        points += 6

#%% Part 2
mapping2 = {'X': {'rock': 'scissors',
                  'paper': 'rock',
                  'scissors': 'paper'},
            'Y': {x:x for x in ['rock', 'paper', 'scissors']},
            'Z': {'rock': 'paper',
                  'paper': 'scissors',
                  'scissors': 'rock'}}

points = 0
for match in matches:
    signs = match.split(' ')
    # print(signs)
    
    sign1 = mapping1[signs[0]]  
    need_to_play = mapping2[signs[1]][sign1]
    
    points += scores[need_to_play]
