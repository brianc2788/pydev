#! /usr/bin/env python3

# FactorFinderI[mproved] (slightly)
# Build 71721
# brianc2788@gmail.com
# copied the code from version
# i wrote on my desktop (from screenshot)
#
# brianc2788@gmail.com
# DEV NOTE:
# I suspect there is still
# a problem if the user enters
# a character or string of
# characters (non-numeric).

def findfactors(int):
    Lfactors = []
    for x in range(1,int,1):
        if int % x == 0:
            print('factor:',x)
            Lfactors.append(x)
    if len(Lfactors) < 2:
        print('Is prime.')

bRun = 1
while bRun:
    stringIn = input('enter number to find factors or \'/quit\': ')
    if stringIn == '':
        stringIn = '/quit'
    if stringIn != '/quit':
        findfactors(int(stringIn))
    else:
        bRun = 0
