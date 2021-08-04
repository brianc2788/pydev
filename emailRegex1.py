# emailRegex1.py
'''
[Description]
Practicing regular expressions with Python.
[Comments]
Had something like,
rawExpr = r'[a-zA-Z_{.}@a-zA-Z\d{.}\.a-zA-Z{.}]'
That wasn't it, but it was close to that
(I think the original even had more errors);
it didn't work, so I went with the expression
currently present.
I think my original expression needed
something like a nested square-bracket pair.
I'm sure there's other approaches as well.
This one works, so I like it.
[Contact]
brianc2788@gmail.com
'''
import re

rawExpr = r'[\w{.}@\w{.}.\D{.}]'
emailRegex = re.compile(rawExpr)

testStr = input('enter: ')

print(str(emailRegex.findall(testStr)))
