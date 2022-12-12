# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 08:46:57 2022

@author: Simon
"""
from matplotlib import pyplot, transforms
import numpy as np
import timer
import networkx as nx
import itertools
import matplotlib.pyplot as plt


with open('day12_input.txt', 'r') as f:
    c = f.read()
    
timer.start()

#%% part 1

# I'll be using graph theory to solve this
# does using an external library count as cheating?
# what's the difference of copying an algorithm to the code
# to using a function that implements the algorithm?

cast = {chr(i+97): i for i in range(26)}  # 97 is lower case a
# cast |= {chr(i+65): i+26 for i in range(26)}  # 97 is upper case A
cast |= {'S': 0, 'E':25} # these are special, so they're inf

# grid as char and converted to values
grid_char = np.array([[val for val in row] for row in c.split('\n')])
grid = np.array([[cast[val] for val in row] for row in c.split('\n')])


# build up a directed graph
graph = nx.DiGraph()
for i, j in itertools.product(*[range(x) for x in grid.shape]):
    graph.add_node((i,j), label=grid[i, j])

for i, j in itertools.product(*[range(x) for x in grid.shape]):
    # look at positions up, left, down and right of the current position
    for di, dj in [1, 0], [-1, 0], [0, 1], [0, -1]:
        try:
            diff =  grid[i, j] - grid[i+di, j+dj]
            # out of bounds check
            if i+di<0 or j+dj<0: 
                raise IndexError
            # if the difference is maximum 1 up, add to graph
            if diff>=-1:
                graph.add_edge((i, j), (i+di, j+dj), weight=1)
        except IndexError:
            # out of bounds check
            pass



source = tuple([x[0] for x in np.where(grid_char=='S')])
target = tuple([x[0] for x in np.where(grid_char=='E')])

# am I making it too simple by using a library? well....
shortest_path_length = nx.shortest_path_length(graph, 
                                        source=source,
                                        target=target)
print(f'{shortest_path_length=}')
#%% part 2

# loop over all possible
possible_starts = list(zip(*np.where(grid==0)))
path_lengths = []
for start in possible_starts:
    try:
        shortest_path_x = nx.shortest_path_length(graph, 
                                                 source=start,
                                                 target=target)
        path_lengths.append(shortest_path_x)
    except nx.NetworkXNoPath:
        # no path? that's ok.
        path_lengths.append(np.inf)
    
timer.stop()
print(f'{min(path_lengths)=}')

# also plot the grid for the lulz and debugging

plt.figure(dpi=25, figsize=[400, 40])
pos = {(i, j): (j,-i) for i, j in itertools.product(*[range(x) for x in grid.shape])}
labels = {(i, j): grid_char[i,j] for i, j in itertools.product(*[range(x) for x in grid.shape])}
colors = ['#f55142' if grid_char[node].isupper() else '#1f78b4' for node in graph.nodes]
nx.draw_networkx(graph, pos=pos, labels=labels, node_color=colors)
plt.pause(0.01)
plt.show()
plt.savefig('graph.png', dpi=100)

plt.pause