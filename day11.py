#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 09:43:14 2022

@author: simon.kern
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 08:11:40 2022

@author: Simon
"""
import operator
import numpy as np
import timer

with open('day11_input.txt', 'r') as f:
    c = f.read()
    
timer.start()

#%% once again some OOP, I just like it a lot
# keep track of which monkey gets which item (edit: was a deadend)
monkey_history = [[] for _ in range(40)]
# keep track of what operations are performed (edit: was a deadend)
operations = [[] for _ in range(40)]


class Item():
    """I've re-implemented INT type to keep track of where items are
    being passed. However, that was a deadend, I'll still leave it here"""
    item_count = 0
    
    def __init__(self, number, item_number=None):
        self.number = number
        if item_number is None:
            item_number = Item.item_count
            Item.item_count += 1
        self.item_number = item_number
   
    def __add__(self, item):
        number =  item if isinstance(item, int) else item.number
        operations[self.item_number] += [f'+{number}']
        return Item(self.number + number, self.item_number)  
    
    def __mul__(self, item):
        number =  item if isinstance(item, int) else item.number
        operations[self.item_number] += [f'*{number}']
        return Item(self.number * number, self.item_number)  
    
    def __floordiv__(self, item):
        number =  item if isinstance(item, int) else item.number
        operations[self.item_number] += [f'//{number}']
        return Item(self.number // number, self.item_number)  
    
    def __truediv__(self, item):
        number =  item if isinstance(item, int) else item.number
        operations[self.item_number] += [f'/{number}']
        return Item(self.number / number, self.item_number)   
  
    def __iadd__(self, item):
        number =  item if isinstance(item, int) else item.number
        operations[self.item_number] += [f'+{number}']
        self.number = self.number + number
        
    def __imul__(self, item):
        number =  item if isinstance(item, int) else item.number
        operations[self.item_number] += [f'*{number}']
        self.number = self.number * number
        
    def __ifloordiv__(self, item):
        number =  item if isinstance(item, int) else item.number
        operations[self.item_number] += [f'//{number}']
        self.number = self.number // number
        
    def __itruediv__(self, item):
        number =  item if isinstance(item, int) else item.number
        operations[self.item_number] += [f'/{number}']
        self.number = self.number / number
            
    def __mod__(self, item):
        number =  item if isinstance(item, int) else item.number
        operations[self.item_number] += [f'test if %{number} -> {self.number % number==0}']
        return self.number % number
        
    def __repr__(self):
        return f'Item({self.number})'
    
    def copy(self):
        return Item(self.number, self.item_number)           
            
class Monkey():
    monkey_count = 0
    
    def __init__(self):
        self.n_inspected = 0      
        self.monkey_number = Monkey.monkey_count
        # this function will be overwritten later in part 2
        self.worry_div = lambda x: x//3
        Monkey.monkey_count += 1 
        self.item_history = []
        
    def __repr__(self):
        n_inspected = self.n_inspected
        return f'Monkey{self.monkey_number}(n={n_inspected})'

    
    def inspect(self, old):
        # this some no-no: use eval to evaluate the string that was in the
        # description of the monkey. Very hacky.
        try:
            number = int(self.action.rsplit(' ')[-1])
        except ValueError:
            number = old

        match self.action[4]:
            case '+':
                op = operator.add
            case '*':
                op = operator.mul
            case _:
                raise Exception('unknown op: {self.action[4]}')
                
        new = op(old, number)
        # then integer divide, but only if necessary (part 2 disables it)
        new = self.worry_div(new)      
        
        # is item not divisible?
        if new%self.div:
            self.monkey_false.items += [new]
            operations[new.item_number].append(f'pass to monkey {self.monkey_false}')
        # else item is divisible by div
        else:
            self.monkey_true.items += [new]
            operations[new.item_number].append(f'pass to monkey {self.monkey_true}')
        monkey_history[old.item_number].append(self.monkey_number)
    
        self.n_inspected += 1 
    
    def turn(self):
        currently_holding = sorted([item.item_number for item in self.items])
        self.item_history.append(currently_holding)
        # print(self.monkey_number, self.items)
        while len(self.items)>0:
            item = self.items.pop(0)
            self.inspect(item)
        
    def reset(self):
        self.item_history = []
        self.n_inspected = 0
        self.items = self._items_orig.copy()
        
    def assign(self, items, action, div, m_true, m_false):
        self.items = items
        self._items_orig = [item.copy() for item in items]
        self.action = action
        self.div = div
        self.monkey_true = m_true
        self.monkey_false = m_false
    
    


# now parse the monkey input
monkeys = [Monkey() for _ in range(c.count('\n\n')+1)]

all_items = []
                                   
for i, monkey_desc in enumerate(c.split('\n\n')):
    settings = monkey_desc.split('\n')
    items = [Item(int(x)) for x in settings[1][17:].split(',')]
    all_items.extend(items)
    action = settings[2][19:]
    div = int(settings[3].rsplit(' ', 1)[1])
    m_true =  monkeys[int(settings[4].rsplit(' ', 1)[1])]
    m_false =  monkeys[int(settings[5].rsplit(' ', 1)[1])]
    monkeys[i].assign(items, action, div, m_true, m_false)


for i in range(20):
    for monkey in monkeys:
        monkey.turn()

monkeys = sorted(monkeys, key=lambda x:x.n_inspected)
print(f'Monkey product of two most active monkeys: {monkeys[-2:]}')


# def get_cycle_length(history):
#     asd

#%% part 2
monkeys = sorted(monkeys, key=lambda x:x.monkey_number)

# first reset our monkeys
lcm = int(np.prod([monkey.div for monkey in monkeys]))

for monkey in monkeys:
    monkey.reset()
    monkey.worry_div = lambda x: Item(x % lcm, 0)

n_inspected_monkeys = [[monkey.n_inspected for monkey in monkeys]]
for monkey in monkeys:
    monkey.reset()
    
for roundi in list(range(10000)):
    for monkey in monkeys:
        monkey.turn()

print(f'Active monkeys: {monkeys}')
monkeys = sorted(monkeys, key=lambda x:x.n_inspected)
print(f'Monkey product of two most active monkeys: {monkeys[-1].n_inspected*monkeys[-2].n_inspected}')

timer.stop()

# plt.plot(n_inspected_monkeys)

# Attempt 1: Interpolating the values
#  DOES NOT WORK, interpolation is not accurate enough (thought so already)

# n_inspected_monkeys = np.array(n_inspected_monkeys)
# f = interpolate.interp1d(np.arange(99, 198), n_inspected_monkeys[0,1:],
#                           fill_value = "extrapolate")

# Attempt 2: look at the idx of the items
# DOES NOT WORK - there is no predictable pattern in the cycles, even though
# we check if there is a repeating pattern in the monkey
# passing, kind of like a markov model, so the n_inspected increases 
# predictably
# and indeed it seems like there is. Once we find out about the pattern,
# we can simply extrapolate from this pattern
# it seems to at first

# for item in range(10):
#     hist = monkey_history[item][::-1]
#     # look for cycles of length i
#     # start at the end to remove first burn-in samples
#     for i in range(1,200): 
#         pattern = hist[:i]
#         matches = []
#         for j in range(0, len(hist), len(pattern)):
#             match = hist[j:j+len(pattern)]==pattern
#             matches.append(match)
#         # print(sum(matches), j)
        