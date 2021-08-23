'''
vowelCounter.py
---------------
User enters a path (absolute) of a plaintext
file to have the vowels counted and reported
back by the application.
'''
import re
import os

VowelRegex = re.compile(r'[aeiouAEIOU]')
txtPath = ' '

#check if dir and file exists.
#checking for both to be more informative.
ValidPath = False
ValidFile = False
while not ValidPath & ValidFile:
    txtPath = input('Enter the absolute path of your plaintext file: ')
    
    if not os.path.isdir(os.path.dirname(txtPath)):
        print('invalid directory.')
        ValidPath = False
    else:
        ValidPath = True
        
        if not os.path.isfile(txtPath):
            print('file not found.')
            ValidFile = False
        else:
            ValidFile = True

txtFile = open(txtPath)
# what's the python equivalent to is_open()?
# file.closed()?

txtContents = txtFile.read()
txtFile.close()

VowelList = VowelRegex.findall(txtContents)

print('''Vowel Count: -------
A: '''+str(VowelList.count('a')+VowelList.count('A'))+'''
E: '''+str(VowelList.count('e')+VowelList.count('E'))+'''
I: '''+str(VowelList.count('i')+VowelList.count('I'))+'''
O: '''+str(VowelList.count('o')+VowelList.count('O'))+'''
U: '''+str(VowelList.count('u')+VowelList.count('U'))+'''
TOTAL: '''+str(len(VowelList)))

print('''------------------------------
Thanks for playing.''')
