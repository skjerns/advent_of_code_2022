# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 08:32:29 2022

@author: Simon
"""

# I dedicate these comments to Gordon Feld, who 
with open('day05_input.txt', 'r') as f:
    c = f.read()
    
    basestack, instructions = c.split('\n\n')
    basestack = basestack.split('\n')
    instructions = instructions.split('\n')[:-1]  # last line is empty
    
    
#%% Part 1
# we solve this problem with stacks using ... a STACK
# well, at least we're using a list and pretending that it's a stack
# actually, python lists are stacks, just in reverse ;-)

n_positions = 9
dock = [list() for _ in range(n_positions)]

# first build up the base dock. for this we need to walk through the basestack
# in reverse order, to build it upside down. [::-1] is a neat trick to 
# reverse any iterable in python. Furthermore, -2 skips the last row

for row in basestack[-2::-1]:
    # walk through the row, the crate alphabet is at distance 4 from each
    for i, stack_i in enumerate(row[1::4]):
        if stack_i.strip()=='':
            # we can't stack air, so skip if the current position is empty
            continue
        dock[i].append(stack_i)
        
# now we have our dock in the base layout that we want. next step is to
# perform the actions that are requested of us

for instr_str in instructions:
    # extract the instructions
    instr = instr_str.split(' ')[1::2]
    # convert to int
    n_items, from_i, to_i = [int(x) for x in instr]
    
    #  repeat n_items of times
    for _ in range(n_items):
        # we need to subtract -1, as python indexing starts at 0
        item = dock[from_i-1].pop()
        dock[to_i-1].append(item)
print('the upper item for each stack is', ''.join([stack[-1] for stack in dock]))


# %% part 2

n_positions = 9
dock = [list() for _ in range(n_positions)]

# again build up the base dock.
for row in basestack[-2::-1]:
    # walk through the row, the crate alphabet is at distance 4 from each
    for i, stack_i in enumerate(row[1::4]):
        if stack_i.strip()=='':
            # we can't stack air, so skip if the current position is empty
            continue
        dock[i].append(stack_i)
        
# now we have our dock in the base layout that we want. next step is to
# perform the actions that are requested of us

for instr_str in instructions:
    # extract the instructions
    instr = instr_str.split(' ')[1::2]
    # convert to int
    n_items, from_i, to_i = [int(x) for x in instr]
    
    # take n items from this stack, all at once
    items = [dock[from_i-1].pop() for _ in range(n_items)]
    
    # again use the reversing trick to put them in in the same order
    # as the were in the stack that they were taken from
    for item in items[::-1]:
        dock[to_i-1].append(item)
        
print('the upper item for each stack is', ''.join([stack[-1] for stack in dock]))
