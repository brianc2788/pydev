'''
clipboardReader.py
------------------
just quickly trying out the pyperclip module.
-prints the contents of the clipboard to stdout.
-i think i will add code to have it also print
 the number of newlines/carriage returns and
 number of characters.
'''
import pyperclip
#import re

print('''----------------------
	clipboard contents:
	------------------------''')
print(pyperclip.paste())
