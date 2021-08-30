'''
listdir-sizes1.py
https://github.com/user5260/pyscripts/listdir-sizes1.py
----------------
another method of printing normal
files and directories with the os
module.

-ignores hidden files.

brianc2788@gmail.com
'''
import os
from sys import argv

if len(argv) < 2:
    print('----------------------\n'+'Directory: '+str(os.getcwd())+'\n----------------------')
    for n in os.listdir():
        if n[0] != '.':
            print('item: '+n+'\n'+str(os.path.getsize(n))+' bytes, '+str(os.path.getsize(n)/1000)+' KB\n----------------------')
else:
    if os.path.isdir(argv[1]):
        print('----------------------\n'+'Directory: '+str(argv[1])+'\n----------------------')
    for n in os.listdir(argv[1]):
        if n[0] != '.':
            print('item: '+n+'\n'+str(os.path.getsize(os.path.join(argv[1],n)))+' bytes, '+str(os.path.getsize(os.path.join(argv[1],n))/1000)+' KB\n----------------------')
