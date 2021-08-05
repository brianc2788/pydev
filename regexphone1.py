'''
phoneregex1.py

[Description]
Practicing regular expressions.
This Python3 script will take a
string from the user and echo
back any 10-digit phone numbers
that were part of the string.

[On the Web]
github.com/user520/pyscripts
brianc2788@gmail.com
'''
import re

# One of many possible ways to try
# finding phone number patterns
# with a regular expression.
phoneRegex = re.compile(r'[\d{3}\-\d{3}\-\d{4}]')
digitRegex = re.compile

testString = 'there is (716-555-6666) a phone number somewhere in this string...'
print('Test string: ' + testString)
print(str(phoneRegex.findall(testString)))

userTry = input('Wanna try? (y/n): ')

if userTry == 'y':
    usrString = input('enter a string with or without a 10-digit phone number: ')
    print('Phone #\'s found:')
    print(str(phoneRegex.findall(usrString)))
    

print('Thanks for playing.')
