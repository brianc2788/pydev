#!/usr/bin/env python3
#-*-coding:utf8;-*-
#qpy:console
"""
droid_explorer.py
-----------------
i hate mobile OSes - lol.
just going to wrap up a few
methods from python's os & sys
modules in some functions for
*more convenient* means of
traversing android's filesystem.
brianc2788@gmail.com
http://user5260.github.io
http://github.com/user5260/pydev
"""
__author__ = 'http://user5260.github.io, brianc2788@gmail.com'
__copyright__ = 'Copyright (c) 2022, Brian Chiodo, AKA brianc2788, AKA user5260'
__license__ = 'Apache License, Version 2.0'

import os,sys

""" Global I/O prompts. """
gPromptIn = '[x]'
gPromptOut_s = '[+]'
gPromptOut_f = '[-]'

""" If any args, print usage. """
def parse_args():
    if len(sys.argv) > 0:
        print("Usage:\n>>python3 -m droid_explorer.py")
        sys.exit(0)

""" Main Loop: prompt for commands until quit event. """
def main():
    cmd_in = input(sPrompt)
    #just echo back for now.
    print(cmd_in)

if __name__ == '__main__':
    parse_args()
    main()
