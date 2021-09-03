'''
charCounter.py
--------------
Prompts user to enter a plaintext file
path and outputs the number of characters
contained in that file.
characters include the alphabet and digits.
does not include whitespace or punctuation.
-edit: changed the regex to just pick out
       ALL NON-WHITESPACE.
       includes newline chars and carr.
       returns.
github.com/user5260/pyscripts/charCounter.py
'''
import os
import re

# Some global vars
globPath = ''
bGoodPath = False
bGoodFile = False

# RegEx - Valid Characters
#charRegex = re.compile(r'[a-zA-Z0-9_-]')
# [a-zA-Z0-9_./\!@#$%^&*()-]
#sadly, i think this simple expression
#is more practical. why not count all non-whitespace?
charRegex = re.compile(r'[\S]')

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

results = charRegex.findall(fullFileString)

# count
charCount = 0
for n in results:
    charCount += 1

print('''------------------------------------
Total Characters: '''+str(charCount))
