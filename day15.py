# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 11:15:57 2022

@author: Simon
"""
import re
import numpy as np
from tqdm import tqdm
import timer
from joblib import Parallel, delayed, cpu_count

with open('day15_input.txt', 'r') as f:
    c = f.read()[:-1]


c2 = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""


timer.start()
#%% part 1

# def calc_row_brute_force(sensors, beacons, y, xmin=-8000000, xmax=8000000):
#     """this was a stupid, brute force approach, but now I'm smarter"""
#     def manhatten_dist(a, b):
#         # assert a.ndim==2
#         # assert b.ndim==2
#         # assert a.shape[1]==2
#         # assert b.shape[1]==2
#         dist = np.abs(a-b).sum(1)
#         return dist
#     row = np.vstack([np.arange(xmin, xmax), 
#                      np.ones((xmax-xmin), dtype=int)*y]).T
    
#     max_dists = manhatten_dist(sensors, beacons).astype(int)
    
#     reached = np.zeros((xmax-xmin), dtype=bool)
#     dists = cdist(row, sensors, metric='cityblock')
#     reached = (dists<=max_dists).sum(1)>0
#     beacons_row = beacons[(beacons[:, 1]==y) & 
#                           (beacons[:, 0]<xmax) &
#                           (beacons[:, 0]>xmin), :] 
    
#     for beacon in beacons_row:
#         reached[beacon[0]+abs(xmin)] = False
#     return reached
def calc_row(sensors, radius, y_row):
    """this time, do it smarter: each beacon intersects the current
    row at a specific x value, we only need to calculate those intersects"""
    # first calculate the 'blocking' radius that each sensor has
    # create indicator for current row where a sensor can reach
    intersections = []
    for (x, y), r in zip(sensors, radius):
        # calculate the distance between the sensor and the row
        y_dist = abs(abs(y)-y_row)
        # only if the y distance is smaller than the reach we need to calculate
        if y_dist<r:
            # manhatten can go r in the y direction
            # what is left is how much we can go in either x direction
            xspan = abs(r-y_dist)
            intersections.append([x-xspan, x+xspan])
    return intersections

# today we need to use vectorization, else we'll go crazy
# some mix and match to parse this stuff
   
sx = [int(re.search(r"Sensor at x=(\d+)", line)[1]) for line in c.split('\n')]
sy = [int(re.search(r"y=(\d+): closest", line)[1]) for line in c.split('\n')]
bx = [int(re.search(r"beacon is at x=(.*),", line)[1]) for line in c.split('\n')]
by = [int(line.rsplit('=', 1)[-1]) for line in c.split('\n')]
    
y_row = 2000000
sensors = np.vstack([sx, sy]).T
beacons = np.vstack([bx, by]).T
radius = np.abs(sensors-beacons).sum(1)
xmin = -y_row*3
xmax = y_row*3
intersections = calc_row(sensors, radius, y_row)
# now calculate the absolute position vector of this row
reached = np.zeros((xmax-xmin), dtype=bool)
for x1,x2 in intersections:
    reached[x1-xmin:x2-xmin] = True
# don't forget to filter out all points on the row where a beacon is
# beacons_row = beacons[(beacons[:, 1]==y_row)] 
for beacon in beacons:
    if beacon[1]==y_row:
        reached[beacon[0]] = False
print(reached.sum())

#%% party 2 

def ranges_dont_overlap(ranges):
    """a helper function that checkes if a list of ranges is overlapping"""
    ranges = sorted(ranges, key=lambda x:x.start)
    while len(ranges)>1:
        r1 = ranges.pop()
        for i, r2 in enumerate(ranges):
            if (r2.start<=r1.start<=r2.stop) | (r2.start<=r1.stop<=r2.stop):
                ranges[i] = range(min(r1.start, r2.start), max(r1.stop, r2.stop))
                break
        else:
            return True
    return False

def calc_with_exception(sensors, radius, min_row, max_row):
    # reached = np.zeros(4000000, dtype=bool)
    for y_row in tqdm(list(range(min_row, max_row))):
        intersections = calc_row(sensors, radius, y_row)
        
        ranges = [range(x, y) for x,y in intersections]
        if ranges_dont_overlap(ranges):
            x = np.unique(np.hstack([list(x) for x in ranges]))
            x = x[(x>=0) & (x<=4000000)]
            x = np.where(np.diff(x)>1)[0][0]+2
            print(ranges)
            return f'found at {x=}+{y_row=} => {x*4000000+y_row=}'
    return ''

max_row = 4000000

# yep, we're using multiprocessing for this one.
splitter = np.linspace(0, max_row, cpu_count()).astype(int)
res = Parallel(-1)(delayed(calc_with_exception)(sensors, radius, splitter[i], splitter[i+1])
              for i in range(len(splitter)-1))

print(''.join(res))
# couple of off-by-one errors....
 # and actually an off-by-two error at line 127 -.-
# found at x=2960217+y_row=3211051 => 11840871211051 too low
# found at x=2960218+y_row=3211051 => 11840875211051 ???
# found at x=2960217+y_row=3211051 => 11840879211051 YESSSS finally
# found at x=2960217+y_row=3211051 => 12844206960217 too high
# found at x=2960217+y_row=3211051 => 12844206960218 too high

# print(calc_with_exception(sensors, radius, 3211051, max_row))
timer.stop()

