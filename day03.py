# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 08:31:24 2022

@author: Simon
"""


# some code annotation, especially for you, Gordon! :P
with open('day03_input.txt', 'r') as f:
    c = f.read()
    # convert to rucksack, last line is empty, so skip
    rucksacks = c.split('\n')[:-1]

#%% Part 1
# create map of priorities
priority_map = ({chr(i+96):i for i in range(1, 27)} |
                {chr(i+38):i for i in range(27, 53)})

priority_sum = 0

# loop over all rucksacks
for rucksack in rucksacks:
    
    #  extract compartment 1&2
    part1 = rucksack[len(rucksack)//2:]
    part2 = rucksack[:len(rucksack)//2]
    
    # sanity check that both compartments have the same amount of items
    assert len(part1)==len(part2)
    
    # convert to set and look for joint parts
    item_double = set(part1) & set(part2)
    
    # sanity check that only one item has been found
    assert len(item_double)==1

    # add priority of double item to priority sum
    priority_sum += priority_map[item_double.pop()]
    
print(f'Part 1 priority sum is {priority_sum}')


#%% Part 2
priority_sum = 0
#  walk through rucksacks in steps of three
for i in range(0, len(rucksacks), 3):
    group = rucksacks[i:i+3]
    
    #  use set theory to form intersection of all three elve's rucksacks
    elve1, elve2, elve3 = [{*items} for 
                           items in group]
    same_item = elve1 & elve2 & elve3
    # sanity check that only one item has been found
    assert len(same_item)==1
    
    # add priority of double item to priority sum
    priority_sum += priority_map[same_item.pop()]
    
print(f'Part 2 priority sum is {priority_sum}')
