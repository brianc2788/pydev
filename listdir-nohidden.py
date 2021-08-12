'''
listdir-nohidden.py
lists my home directory and
filters out the hidden files/dirs.
'''
import os

for n in os.listdir('/home/userone'):
    if n[0] != '.':
        print(n)
