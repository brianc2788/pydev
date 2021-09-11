'''
charCounter2.py
--------------
this is an improved version of
the original charCounter.py.
Rid of some redundancies and
more informative final results.

UPDATE: appears to work; have done
some manual counting and other work
to verify the results of this script
and, although not a very rigorous
verification thus far, it appears
to work. fingers crossed.
UPDATE: Total Character results are accurate.
UPDATE: Cleaned up the code a bit and added
'whitespace chars' to the final report.

github.com/user5260/pyscripts/charCounter.py
'''
import os
import re

# Some global vars
globPath = ''
bGoodPath = False
bGoodFile = False

# Various groups of character expressions.
totalRegex = re.compile(r'[\S]') # everything but whitespace
alphaRegex = re.compile(r'[a-zA-Z]') # just alphabetical
digitRegex = re.compile(r'[\d]') # just digits
puncRegex = re.compile(r'[^a-zA-Z0-9\s]') # just punctuation/other
wspaceRegex = re.compile(r'[\s]')

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

# create a read-only file object/open the file. store the text in a string. close the file.
rFileObj = open(globPath, mode='r')
fullFileString = rFileObj.read()
rFileObj.close()

print('''------------------------------------
Total Characters: '''+str(len(totalRegex.findall(fullFileString)))+'''
Total Chars (w/wspace&eof): '''+str(len(totalRegex.findall(fullFileString))+len(wspaceRegex.findall(fullFileString)))+'''
-----------------------------------------'''+'''
Alpha Characters: '''+str(len(alphaRegex.findall(fullFileString)))+'''
Digit Characters: '''+str(len(digitRegex.findall(fullFileString)))+'''
Punctuation Chars: '''+str(len(puncRegex.findall(fullFileString)))+'''
Whitespace (not counted in total): '''+str(len(wspaceRegex.findall(fullFileString)))+'''
-------------------------------------''')
