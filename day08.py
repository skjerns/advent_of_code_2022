# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 05:54:50 2022

@author: Simon
"""
import timer
import itertools
import numpy as np

with open('day08_input.txt', 'r') as f:
    c = f.read()[:-1]
    
#%% part 1
timer.start()
# this seems like a job for numpy
grid = np.stack([np.fromiter(row, int) for row in c.split('\n')])



# ok, I'll do this the stupid way: just loop over rows and columns
trees_visible = np.zeros(len(grid))

# make a copy, as we will modify this array
grid_rows = [row for row in grid]

trees_visible = 0

# I tried it in a smart way using argmax and could not get it to work 
# within 30 minutes. I think I overcomplicated things a bit.
# Now let's just do it the stupid way and iterate over every tree
for r, c in itertools.product(*[np.arange(len(grid))]*2):
    tree_height = grid[r, c]
    row = grid[r, :].copy()   # create copy to prevent inplace modification
    col = grid[:, c].copy()  # create copy to prevent inplace modification
    
    # subtract each tree height and see if there are trees left to either side
    # that are still higher or equally high
    row -= tree_height
    col -= tree_height

    if all(row[:c]<0) or all(row[c+1:]<0) or \
       all(col[:r]<0) or all(col[r+1:]<0):
           trees_visible += 1
           
print('part 1:', trees_visible)

#%% part 2


grid = grid.astype(float)

# I did not even try to do this in a smart way 
# now let's just do it the stupid way and iterate over every tree

scores = []
for r, c in itertools.product(*[np.arange(len(grid))]*2):
    tree_height = grid[r, c]
    row = grid[r, :].copy()   # create copy to prevent inplace modification
    col = grid[:, c].copy()  # create copy to prevent inplace modification
    
    # subtract each tree height and see if there are trees left to either side
    # that are still higher or equally high
    row -= tree_height
    col -= tree_height
    
    row[row>=0] = np.inf
    col[col>=0] = np.inf

    dists = []
    # going clockwise in each direction from the tree to the outside
    # add a 99 to each end to check if we have reached the end of the board.
    # if not, add 1 to the count, as the blocking tree also counts
    if c<len(grid)-1:
        direction = [*row[c+1:], 99]
        dist = np.argmax(direction)
        if direction[dist]!=99:
            dist+=1
        dists += [dist]
        # print(f'right {dist=}')
    if r<len(grid)-1:
        direction = [*col[r+1:], 99]
        dist = np.argmax(direction)
        if direction[dist]!=99:
            dist+=1
        dists += [dist]
        # print(f'bottom {dist=}')

    if c>0:
        direction = [*row[:c][::-1], 99]
        dist = np.argmax(direction)
        if direction[dist]!=99:
            dist+=1
        dists += [dist]
        # print(f'left {dist=}')

    if r>0:
        direction = [*col[:r][::-1], 99]
        dist = np.argmax(direction)  
        if direction[dist]!=99:
            dist+=1
        dists += [dist]
        # print(f'up {dist=}')


    scenic_score = np.product(dists)
    scores.append(scenic_score)

print('part 2:', max(scores))
timer.stop()