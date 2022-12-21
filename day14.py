# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 08:40:24 2022

@author: Simon
"""
import re
import timer
import numpy as np 

with open('day14_input.txt', 'r') as f:
    c = f.read()[:-1]
# c = '498,4 -> 498,6 -> 496,6\n503,4 -> 502,4 -> 502,9 -> 494,9'
    
#%% part 1

timer.start()
instructions = c.split('\n')

cave = np.full([1000, 1000], ' ', dtype='str')

formations = []
for instr in instructions:
    # i reverse the instructions, as Python uses rows first, but instructions
    # are in column first. This is done via [::-1]
    formation = [list(map(int, xy.split(','))) for xy in instr.split(' -> ')]
    formations.append(formation)
    
xmin = min([min([rock[0] for rock in formation]) for formation in formations])
xmax = max([max([rock[0] for rock in formation]) for formation in formations])
ymin = min([min([rock[1] for rock in formation]) for formation in formations])
ymax = max([max([rock[1] for rock in formation]) for formation in formations])
    
for formation in formations:
    for (x1, y1), (x2, y2) in zip(formation, formation[1:]):
        dy = slice(min(x1, x2), max(x1, x2)+1)
        dx = slice(min(y1, y2), max(y1, y2)+1)
        cave[dx, dy] = '#'

# cave = cave[0:cave_ymax+1, cave_xmin:cave_xmax+1]

#%% the actual sand simulation
space_left = True
while space_left:
    # print((cave=='o').sum())
    # position of current sand kernel
    x = 0
    y = 500
    if cave[x, y]=='o':
        break
    while True:
        if (y<=xmin) or (y>=xmax) or x>=ymax:
            space_left = False
            break
        # input('...')
        # cave2 = cave.copy()
        # cave2[x, y] = 'X'
        # print(x, y)
        # print(cave2[0:ymax+1, xmin:xmax+1])
        if cave[x+1, y]==' ':
            x+=1
            continue
        if cave[x+1, y-1]==' ':
            x+=1
            y-=1
            continue
        elif cave[x+1, y+1]==' ':
            x+=1
            y+=1 
            continue
        else:
            # print('place o')
            cave[x, y] = 'o'
            break

        
print('Number of sand:', (cave=='o').sum())


#%% the actual sand simulation
cave[cave=='o'] = ' '  # reset cave
cave[ymax+2, :] = '#'

space_left = True
while space_left:
    # print((cave=='o').sum())
    # position of current sand kernel
    x = 0
    y = 500
    if cave[x, y]=='o':
        break
    while True:
        
        # if (y<=xmin) or (y>=xmax):
        #     space_left = False
        #     break
        # # input('...')
        # cave2 = cave.copy()
        # cave2[x, y] = 'X'
        # print(x, y)
        # print(cave2[0:ymax+1, xmin:xmax+1])
        if cave[x+1, y]==' ':
            x+=1
            continue
        if cave[x+1, y-1]==' ':
            x+=1
            y-=1
            continue
        elif cave[x+1, y+1]==' ':
            x+=1
            y+=1 
            continue
        elif y==0:
            space_left = False
            break
        else:
            # print('place o')
            cave[x, y] = 'o'
            break

timer.stop()      
print('Number of sand for path 2:', (cave=='o').sum())
