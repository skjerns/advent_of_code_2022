# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 08:28:53 2022

@author: Simon
"""
import timer

with open('day07_input.txt', 'r') as f:
    c = f.read()
    

#%% part 1
 # today we will be using some object oriented programming
# we will simulate a filesystem. The filesystem has 

timer.start()
class File():
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
    
    def __repr__(self):
        return f'{self.name} - {self.size}'

class Folder():
    def __init__(self, name, parent):
        self.name = name
        self.folders = {}
        self.files = []
        self.parent = parent
        
    def get_size(self):
        size = sum([file.size for file in self.files])
        size += sum([folder.get_size() for folder in self.folders.values()])
        return size

    def add(self, command):
        pre, name = command.split(' ', 1)
        if pre=='dir':
            folder = Folder(name, self)
            self.folders[name] = folder
        elif pre.isnumeric():
            file = File(name, int(pre), self)
            self.files.append(file)
        else:
            raise Exception(f'unknown command: {command}')
    
    def __repr__(self):
        string = f'{self.parent}{self.name}/'
        return string
    
    def __getitem__(self, key):
        return self.folders[key]
    
    def tree(self, indent=2):
        print('-' *(indent-4) + str(self) )
        for file in self.files:
            print('-'*indent + str(file))
        for folder in self.folders.values():
            folder.tree(indent+3)
    
    
    def walk(self):
        subfolders = []
        for folder in self.folders.values():
            subfolders += folder.walk()
        return [self] + subfolders

root = Folder('', '')

# now write a parser that loops through all commands
commands = c.split('\n')
curr_folder = root
# skip first instruction and last empty line
for cmd in commands[1:-1]:
    # print(cmd)
    # this is a command instruction
    if cmd.startswith('$'):
        parts = cmd.split(' ')
        
        # we move into another directory
        if parts[1]=='cd':
            if parts[2]=='..':
                # print(f'{cmd}: moving one up to {curr_folder.parent}')
                curr_folder = curr_folder.parent
            else:
                # print(f'{cmd}: moving into {parts[2]}')
                curr_folder = curr_folder.folders[parts[2]]
        elif parts[1]=='ls':
            # print(f'{cmd}: listing folders of {curr_folder}')
            pass
        else:
            raise Exception(f'unknown command: {cmd}')
    
    else:
        # print(f'{cmd}: adding {cmd} to {curr_folder}')
        curr_folder.add(cmd)


# now walk through all directories and sum up all dirs that are small
sum_small_folders = 0
for folder in root.walk():
    if (size:=folder.get_size())<100000:
        sum_small_folders += size

print(f'Size of all small folders < 100000 is {sum_small_folders}')


#%% part 2


total_space = 70000000
needed_space = 30000000
curr_size = root.get_size()
free_space = total_space-curr_size
needed_space = needed_space-free_space


smallest_possible_freed_space = root.get_size()

for folder in root.walk():
    if (size:=folder.get_size())>=needed_space:
        if size<smallest_possible_freed_space:
            smallest_possible_freed_space= size

print(f'Size of smallest folders that will free up {needed_space} is {smallest_possible_freed_space}')
timer.stop()