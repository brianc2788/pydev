# quick little 'stop at' rng console app.
import random

numIn = input('enter a number 1-10: ')

rand1 = int

while rand1 != int(numIn):
    # set rand1 to a random number and
    # check it against the user's request.
    rand1 = random.randint(1,10)
    print(rand1)
