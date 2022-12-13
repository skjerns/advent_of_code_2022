# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 09:25:46 2022

@author: Simon
"""

import timer
import json
import numpy as np
import pysnooper

# some code annotation, especially for you, Gordon! :P
with open('day13_input.txt', 'r') as f:
    c = f.read()[:-1]

    
timer.start()    
#%% part 1
# seems like some simple parsing again
# and we'll also use the `match` statement of Python

# ok this list comprehension is a bit of an abomination, but it does the job.
packets = [[json.loads(data) for data in pair.split('\n')] for pair in c.split('\n\n')]

# this calls for some recursion to happen
# @pysnooper.snoop(normalize=True)
def compare(left, right):
    
    match (left, right):
        case [], []:
            return np.nan
        case [], _:
            return True
        case _, []:
            return False
        
        case list(), list():
            for l, r in zip(left, right):
                res = compare(l, r)
                # if sublists were not able to make a decision, continue
                if np.isnan(res):
                    continue
                # sublist returned either False or True, so propagate up
                return res
            # however, if the loop finished and no decision was made,
            # we need to make a decision based on the list lengths
            if len(left) < len(right):
                return True
            elif len(left) > len(right):
                return False
            else:
                return np.nan
        
        case list(), int() :
            # only need to compare the first item
            return compare(left, [right])
        
        case int(), list():
            # only need to compare the first item
            return compare([left], right)
        
        case int(), int():
            if left==right:
                # if it's nan we cannot make a decision
                return np.nan
            elif left<right:
                # if left is smaller, list is in right order
                return True
            else: 
                # right is smaller, so list is not in right order
                return False
            
        case other:
            raise Exception(f'no match: {other}')
            
in_order = []
for i, pair in enumerate(packets, 1):
    if compare(*pair):
        in_order.append(i)
    # break
# 5697 too high
print(f'sum of in-order pairs {in_order} is {sum(in_order)}')

#%% part 2:
packet_list = [[[2]],[[6]]]

for pair in packets:
    packet_list.extend(pair)
    
# sanity check, make sure no duplicate packages are present
assert len(packet_list)==len(set([str(x) for x in packet_list]))

# brute force sorting, lol
is_smaller = np.full([len(packet_list), len(packet_list)], np.nan)
for a in range(len(packet_list)):
    for b in range(len(packet_list)):
        is_smaller[a, b] = compare(packet_list[a], packet_list[b])
# how often was each packet smaller than the previous one? sort accordingly
sortkey = np.nansum(is_smaller, 0)
sorted_packets = [x for x, _ in sorted(zip(packet_list, sortkey), key=lambda x:x[1])]

idx1 = sorted_packets.index([[2]])+1
idx2 = sorted_packets.index([[6]])+1

print(f'dividers are at {idx1} and {idx2}, product is {idx1*idx2}')

timer.stop()
