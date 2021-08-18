'''
dirSize.py
----------
Prints the total size of the
current working directory and
each of the files contained
within it (seems to have a
problem with hidden dirs,
e.g. '../.hiddenrc/'.

[Comments]
Would like to display sizes in
MB rather than bytes. An easy
fix.
-done

brianc2788@gmail.com
github.com/user5260/pyscripts
'''
import os

# total size; accumulated and printed at the end.
sizeofcwd = 0
# number the 'items' (files/folders) in the dir.
itemCount = 1

for file in os.listdir(os.getcwd()):
    print(str(itemCount) + " " + file + ", " + str(os.path.getsize(os.path.join(os.getcwd(),file))) + ' bytes')
    sizeofcwd += os.path.getsize(os.path.join(os.getcwd(),file))
    print(str(sizeofcwd / 100000)+' MegaBytes\n')
    itemCount += 1

print('Total Dir Size: ' + str(sizeofcwd) + ' bytes')
