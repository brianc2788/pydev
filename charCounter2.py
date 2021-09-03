'''
charCounter2.py
--------------
this is an improved version of
the original charCounter.py.
Rid of some redundancies and
more informative final results.

update: appears to work; have done
some manual counting and other work
to verify the results of this script
and, although not a very rigorous
verification thus far, it appears
to work. fingers crossed.

github.com/user5260/pyscripts/charCounter.py
'''
import os
import re

# Some global vars
globPath = ''
bGoodPath = False
bGoodFile = False

# RegEx - Valid Characters
totalRegex = re.compile(r'[\S]') # everything but whitespace
alphaRegex = re.compile(r'[a-zA-Z]') # just alphabetical
digitRegex = re.compile(r'[\d]') # just digits
puncRegex = re.compile(r'[^a-zA-Z0-9]') # just punctuation/other

# Introduction/Title & Seperator
print('''character counter - python script
----------------------------------''')

# Check user input -- Validate file path & file name.
while not bGoodPath & bGoodFile:
    usrInput = input('enter full/relative path to a plaintext file: ')
    if not os.path.isdir(os.path.dirname(usrInput)):
        print('---directory not found---')
        bGoodPath = False
    else:
        bGoodPath = True
        if not os.path.isfile(usrInput):
            print('---file not found---')
            # thought it might be helpful to list
            # the contents of the user's dir (if good).
            print('---files in given dir:---')
            os.system('ls '+str(os.path.dirname(usrInput)))
            bGoodFile = False
        else:
            bGoodFile = True
            globPath = usrInput

# create a read-only file object/open the file.
rFileObj = open(globPath, mode='r')
fullFileString = rFileObj.read()
rFileObj.close()

results = totalRegex.findall(fullFileString)

print('''------------------------------------
Total Characters: '''+str(len(results))+'''
Alpha Characters: '''+str(len(alphaRegex.findall(fullFileString)))+'''
Digit Characters: '''+str(len(digitRegex.findall(fullFileString)))+'''
Punctuation Chars: '''+str(len(puncRegex.findall(fullFileString)))+'''
-------------------------------------''')
