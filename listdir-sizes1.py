'''
listdir-sizes1.py
https://github.com/user5260/pyscripts/listdir-sizes1.py
----------------
another method of printing normal
files and directories with the os
module.

-ignores hidden files, for now.

brianc2788@gmail.com
'''
import os

print('----------------------\n'+'Directory: '+str(os.getcwd())+'\n----------------------')

for n in os.listdir():
    if n[0] != '.':
        print('item: '+n+'\n'+str(os.path.getsize(n))+' bytes, '+str(os.path.getsize(n)/1000)+' KB\n----------------------')
