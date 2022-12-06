# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:33:23 2022

@author: Simon
"""
import timeit
_start = [None]


def nanoseconds_to_human_readable(seconds: int) -> str:
    nanoseconds = seconds*10**9
    microseconds = nanoseconds / 1000
    if microseconds < 1000:
        return f"{microseconds:.0f} µs"
    
    millisecond = microseconds / 1000
    if millisecond < 1000:
        return f"{microseconds:.0f} ms"
       

    seconds = microseconds / 1000
    if seconds < 60:
        return f"{seconds:.2f} sec"

    minutes = seconds / 60
    if minutes < 60:
        leftover_seconds = seconds % 60
        return f"{minutes:.0f} minutes, {leftover_seconds:.0f} seconds"

    hours = minutes / 60
    leftover_minutes = minutes % 60
    return f"{hours:.0f} hours, {leftover_minutes:.0f} minutes"

def start():
    _start[0] = timeit.default_timer()

def stop(x=''):
    elapsed = timeit.default_timer()-_start[0]
    print(f'took {nanoseconds_to_human_readable(elapsed)}')
    return elapsed