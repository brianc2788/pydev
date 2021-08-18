# emailRegex1.py
'''
[Description]
Practicing regular expressions with Python.
[Comments]
Copied the script i wrote on my
phone (Qpython) because, I think that
version is the most readable and has
the best regex for emails. Prev version
was verbose and not great overall.

[Contact]
brianc2788@gmail.com
github.com/user5260
'''
import re

emailRegex = re.compile(r'[a-zA-Z0-9_-]{4,20}@[a-zA-Z0-9_-]+\.[com|net|org|eu|ru|aus]{2,3}')
str1 = 'something@something.com,another@thing.net,yetano@gmail.eu'

print('''----------------------------------------
[DESCRIPTION]
Testing a regular expression for emails in a string.
Note this expression itself does not include commas,
which is why it works with a string of CSVs.

[EXPRESSION]
'''+str(emailRegex.pattern)+'''

[TEST VARIABLES]
'''+str(type(str1))+', '+str1+'''
----------------------------------------

[RESULTS]''')
count = 1
for n in emailRegex.findall(str1):
    print(str(count)+'. '+n)
    count += 1
print('[EXITING...]--------------------')
