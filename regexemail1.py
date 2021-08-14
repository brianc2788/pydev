# emailRegex1.py
'''
[Description]
Practicing regular expressions with Python.
[Comments]
After going back over the chapters on
regular expressions ("Automate the Boring
Stuff with Python"), my expression is
working well. The only thing I might
like to add is maybe seperating the
parts of the email into regex groups.
Other than that, [pretty] happy with
the results.

User is prompted to enter a string and
the program will match any and all e-mail
patterns and output it back to the user.

This pattern accepts almost all symbols
along with the usual alphanumeric chars.
Sometimes can be a problem, for example
if the email address is in parentheses,
like "(email@address.com)", the first
parentheses gets picked up. Some e-mail
addresses can have these symbols, so I'm
inclined to leave it as-is -- certain
case uses will need some modification here.

[Contact]
brianc2788@gmail.com
'''
import re
# first attempt; didn't work at all, really.
# re-read the regex chapter in 'Automate..'
# rawExpr = r'[\w{.}@\w{.}.\D{.}]'
# ^^Was trying to use the '.' as wildcard, but
# didn't use it correctly.
# The following comment regex works as well
rawExpr = r'[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+\.[comnet]{2,3}'
#rawExpr = r'(\S+@\S+\.[comnet]{2,3})'
emailRegex = re.compile(rawExpr)

testStr = input('enter: ')

for n in emailRegex.findall(testStr):
    print('Found an e-mail address: '+n)

