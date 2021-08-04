'''
phoneregex2.py

[Description]
Same as phoneregex1.py (in fact,
it's copy & pasted), but changed
the phoneRegex to find patterns
like: (000)000-0000.

[Comments]
Played with this for a little bit.
Gonna leave this for now and go
re-read some material on
regex.

[On the Web]
github.com/user520/pyscripts
brianc2788@gmail.com
'''
import re

# One of many possible ways to try
# finding phone number patterns
# with a regular expression.
phoneRegex = re.compile(r'[\(\d\d\d\)\d\d\d\-\d\d\d\d]')
digitRegex = re.compile

testString = 'there is ((777)555-6666) a phone number somewhere in this string...'
print('Test string: ' + testString)
print(str(phoneRegex.findall(testString)))

userTry = input('Wanna try? (y/n): ')

if userTry == 'y':
    usrString = input('enter a string with or without a 10-digit phone number: ')
    print('Phone #\'s found:')
    print(str(phoneRegex.findall(usrString)))
    

print('Thanks for playing.')
