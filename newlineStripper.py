'''
pyscripts/newlineStripper.py
----------------------------
strip whitespace & newlines out of
text files and copies the single-
line string to a new, plaintext
file.
-fixed most issues.
 my goal was to just make this
 script achieve desired results,
 which is does, however sloppily.
 also to fix any fatal bugs that
 would cause python to crash;
 those have all been resolved.
 ugly under the hood, but a
 smooth experience for the user.

brianc2788@gmail.com
github.com/user5260
'''
import os
import re

globPath = ' '
bGoodPath = False
bGoodFile = False

while not bGoodPath & bGoodFile:
    usrInput = input('enter the full/relative path of your plaintext file: ')
    if not os.path.isdir(os.path.dirname(usrInput)):
        print('invalid directory/directories.')
        bGoodPath = False
    else:
        bGoodPath = True
        if not os.path.isfile(usrInput):
            print('invalid file/file not found.')
            bGoodFile = False
        else:
            bGoodFile = True
            globPath = usrInput

stripper = re.compile(r'[\S]+')
rFile = open(globPath, mode='r')

# if rFile.closed():
#     print('unable to open file.')

fullString = rFile.read()
rFile.close()

validChars = stripper.findall(fullString)
cutString = ''
for n in validChars:
    cutString += n

# this works for now, because I'm using a very small
# plantext file for testing.
print('ORIGINAL:\n'+fullString+'\n--- END ORIGINAL ------------')
print('RECOVERED:\n'+cutString+'\n--- END RECOVERED -----------')

newFilePath = globPath + '.stripped'

bFileExists = True
while bFileExists:
    if not os.path.isfile(newFilePath):
        bFileExists = False
    else:
        newFilePath += '.stripped'

wFile = open(newFilePath,mode='x') # can omit 'mode=' for just 'x'/'r'/'w'
if not wFile.writable():
    print('file not writable. aborting.')
    wFile.close()
else:
    wFile.write(cutString)
    wFile.close()
    if os.path.isfile(newFilePath):
        print('created file: '+newFilePath+'\n# EXITING APPLICATION -------------------')

''' # UNUSED GARBAGE
# extRegex = re.compile(r'([\S])+\.([\S]+)')
cutString = ''
for n in fullString:
    if fullString[n] == '\\n':
        continue
    else:
        cutString += fullString[n]
print(cutString)
'''
