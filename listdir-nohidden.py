'''
listdir-nohidden.py
lists my home directory and
filters out the hidden files/dirs.
'''
import os

print('-------------------------------------------------\n'
     +'listing files/folders in your home directory...\n'
     +'(excludes hidden files)\n'
     +'-------------------------------------------------')
for n in os.listdir('/home/userone'):
    if n[0] != '.':
        print(n)
