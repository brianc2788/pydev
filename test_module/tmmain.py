'''
tmmain.py
-------------------------
Python3 - Test Module
-------------------------
This script will only work if testmod.py is located
in python's import path or the interpreter is run in
the same directory.
If the interpreter run in the root directory, the
statement `from test_module import testmod` would be
required; Or, again, the test_module dir could be loc-
ated in python's import path.
-------------------------
http://brianc2788.github.io/
'''
import testmod
def main():
    testmod.status()
if __name__ == '__main__':
        main()
