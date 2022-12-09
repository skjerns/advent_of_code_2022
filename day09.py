# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 10:41:25 2022

@author: Simon
"""
from dataclasses import dataclass
import timer
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

with open('day09_input.txt', 'r') as f:
    c = f.read()

def list_snake(head):
    yield head
    while hasattr(head, 'tail'):
        head = head.tail
        yield head
        
def roundup(x):
    return int(np.ceil(x / 50.0)) * 50

def plot_grid(head, pause=0.01):
    """helper function to visualize the current grid"""

    
    snake = list(list_snake(head))
    max_pos = max([max(e.pos_history) for e in snake])
    size = max(roundup(max(abs(max_pos.x), abs(max_pos.y)))*2, 50)+1
    grid = np.zeros([size, size])
    n_tails = len(snake)

    # first plot the history, as then it can be overwritten
    for pos in set(snake[-1].pos_history[:-1]):
        grid[pos.x+size//2, pos.y+size//2] = 0.05
            
    for i, element in enumerate(snake[::-1]): 
        # however, don't overwrite if there is a larger element there
        color_i = (i+1)/n_tails
        # print(color_i)
        if grid[element.pos.x+size//2, element.pos.y+size//2] < color_i:  
            # print(color_i, element.pos.x, element.pos.y)
            grid[element.pos.x+size//2, element.pos.y+size//2] = color_i
    
    ax = plt.gca()
    ax.clear()    
    ax.imshow(grid, cmap='CMRmap', vmax=1, origin='lower')
    # ax.set_xlim(5, 0)  # decreasing time
    plt.pause(pause)
    
    return grid
        


#%% part 1 
# this sound like fun!!
# I liked using OOP in the last exercise, to let's do it again


@dataclass(frozen=True)
class Position():
    x:int = 0
    y:int = 0
    
    def __mod__(self, pos):
        """calculate euclid distance"""
        return sqrt((self.x-pos.x)**2 + (self.y-pos.y)**2)
    
    def __add__(self, pos):
        return Position(self.x+pos.x, self.y+pos.y)
    
    def __hash__(self):
        return hash(self.x)+ hash(self.y)
    
    def __eq__(self, pos):
        if self.x==pos.x and self.y==pos.y:
            return True
        return False
    
    def __gt__(self, pos):
        if (abs(self.x) > abs(pos.x)) :
            return True
        if (abs(self.y) > abs(pos.y)):
            return True 
    
class Tail():
    def __init__(self):
        self.pos = Position(0,0)
        self.pos_history = [self.pos]
        
    def attach(self, tail):
        self.tail = tail
        
    def move(self, front):
        dist = self.pos % front.pos
        if dist>=2:
            dx = 0
            dy = 0
            # if head is still in the same row, simply move there.
            if (front.pos.x==self.pos.x):
                dy = [1, -1][front.pos.y<self.pos.y]
                self.pos += Position(dx, dy)  

            # if head is still in the same column, simply move there.
            elif (front.pos.y==self.pos.y):
                dx = [1, -1][front.pos.x<self.pos.x]
                self.pos += Position(dx, dy)  

            # however, if it's diagonally, we need to perform a diagonal move
            # as well
            else:
                dx = [1, -1][front.pos.x<self.pos.x]
                dy = [1, -1][front.pos.y<self.pos.y]
                self.pos += Position(dx, dy)  

            # print(dist)
        # else:
            # print('nomove', dist)
        self.pos_history += [self.pos]
        if hasattr(self, 'tail'):
            self.tail.move(self)
        # print(sel)
        # plot_grid(head)      
            
            
class Head(Tail):
    
    def move(self, cmd):
        
        direction, n = cmd.split(' ')
        dx = 0
        dy = 0
        n = int(n)
        
        match direction :
            case 'R':
                dy = 1
            case 'D':
                dx = -1
            case 'L':
                dy = -1
            case 'U':
                dx = 1
        for step in range(n):
            self.pos = self.pos + Position(dx, dy)
            self.pos_history += [self.pos]
            self.tail.move(self)
            # plot_grid(head)


head = Head()  # create a head
tail = Tail()  # attach a tail to the head
head.attach(tail)

for cmd in c.split('\n')[:-1]:
    head.move(cmd)
grid = plot_grid(head)

print(len(set(tail.pos_history)))
# asd
#%% part 2
 # 4707 too high
head = Head()  # create a head

# c='R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20\n'  # test input
curr_end = head
for _ in range(9):
    
    tail = Tail()
    curr_end.attach(tail)
    curr_end = tail

for i, cmd in enumerate(c.split('\n')[:-1]):
    # if i==3:
        # plt.figure()
        # grid = plot_grid(head)
        # break
    head.move(cmd)
    s
    plot_grid(head)



