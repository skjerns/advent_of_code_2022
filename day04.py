# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 09:56:00 2022

@author: Simon
"""
import timer
# I dedicate these comments to my supervisor Gordon Feld, the vigorous defender
# of open science and devourer of protein puddings.

with open('day04_input.txt', 'r') as f:
    lines = f.readlines()

def x():
    timer.start()
    # split lines into elve pairs
    pairs = [line.strip().split(',') for line in lines]
    
    
    #%% Part1
    n_total_overlap = 0
    for elve1, elve2 in pairs:
        # once again we use set theory to see if there is overlap
        # turn the range of sections for each elve into a set
        section1 = set(range(int(elve1.split('-')[0]), int(elve1.split('-')[1])+1))
        section2 = set(range(int(elve2.split('-')[0]), int(elve2.split('-')[1])+1))
        
        # if the union of the two sets is larger than the larger of the two sets
        # then there is a total overlap of both sets
        if len(section1 | section2) <= max([len(section1), len(section2)]):
            n_total_overlap += 1
    
    #%% Part2
    n_any_overlap = 0
    for elve1, elve2 in pairs:
        # once again we use set theory to see if there is overlap
        # turn the range of sections for each elve into a set
        section1 = set(range(int(elve1.split('-')[0]), int(elve1.split('-')[1])+1))
        section2 = set(range(int(elve2.split('-')[0]), int(elve2.split('-')[1])+1))
        
        # if the union of the two sets is larger than sum of the two sets
        # then there is a partial overlap of both sets
        if len(section1 | section2) < sum([len(section1), len(section2)]):
            n_any_overlap += 1
            
    print(f'{n_total_overlap=}, {n_any_overlap=}')
    return timer.stop()

t = []
while True:
    t += [x()]
