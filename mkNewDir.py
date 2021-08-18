'''
mkNewDir.py
--------------------------
reading and writing files.
--------------------------
didn't finish this chapter on
files. Stopped after creating
a new dir/folder.
'''
import os

print('--------------------------------------------------\n'
     +'!! CREATING A NEW DIRECTORY !!')

newDir = input('New DIR/FOLDER name: ')
os.mkdir(newDir)

print('!! PRINTING CONTENTS OF: !!\n'+os.getcwd()+'\n'
     +'----------------------------------------')

for files in os.listdir():
    print(files)

print('--------------------------------------------------\n'
     +'created your directory/folder.\n'
     +'exiting...\n'
     +'--------------------------------------------------')
