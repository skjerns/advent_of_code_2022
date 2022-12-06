# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:33:23 2022

@author: Simon
"""
import time
_start = [None]

def _print_time(seconds):    
    if seconds > 7200:
        hours   = seconds//3600
        minutes = seconds//60 - hours*60
        return "{:.0f}:{:02.0f} hours".format(hours, minutes)
    elif seconds > 180:
        minutes = seconds//60
        seconds = seconds%60
        return "{:.0f}:{:02.0f} min".format(minutes , seconds)
    elif seconds >= 1:
        return "{:02.1f} sec".format(seconds)
    elif seconds > 0.01:
        return "{} ms".format(int(seconds*1000))
    elif seconds > 0.001:
        return "{:.1f} ms".format(seconds*1000)
    elif seconds > 0.0001:
        return "{:.1f} μs".format(seconds*100000)
    else:
        return "{} nanoseconds".format(int(seconds*1e-9))
   

def start():
    _start[0] = time.time()

def stop(x=''):
    elapsed = time.time()-_start[0]
    print(f'took {_print_time(elapsed)}')
    return elapsed