'''
Test Module #2
This test module calls 'print_title()' when imported.
I was wondering why the constructor doesn't work in
testmod.py, and now I think it's because, '__init__'
has to be defined. If print_title() was called in the
__init__ definition, I think it would print when an
object is created, as I was expecting earlier.
Had a hard time putting that into words and
feeling a little tired; hope that made sense.
Probably just finish the chapter before jumping
to conclusions and wasting too much time, like this.
'''
def print_title():
    print('Test Module #2')

print_title()