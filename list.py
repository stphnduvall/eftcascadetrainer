#!/usr/local/bin/python3

import sys
from os import listdir
from os.path import isfile, join

myname = sys.argv[1]
mypath = sys.argv[2]

if len(sys.argv) != 3:
    print(f'This command takes exactly two arguments')
    print(f'./list.py output dir/to/list')

output = open(myname + '.txt', 'w')

for f in listdir(mypath):
    file = join(mypath, f)
    if isfile(file):
        print(file)
        output.write(f'{file}\n')

output.close()

print(f'{myname}.txt')

