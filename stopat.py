'''
stopat.py
---------
[Description]
Program prompts user to enter a number 1-10.
Program generates random numbers between
1 and 10, and stops when randomly-generated
number is a match with the user's selection.

'pyscripts' repository has a lot of little,
mostly useless scripts that I produced while
learning Python; if you couldn't tell by
now.

brianc2788@gmail.com
'''
import random

numIn = input('enter a number 1-10: ')

rand1 = int

while rand1 != int(numIn):
    # set rand1 to a random number and
    # check it against the user's request.
    rand1 = random.randint(1,10)
    print(rand1)
