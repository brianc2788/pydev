#! /usr/bin/env python3
'''
celsius-conv.py
brianc2788@gmail.com
'''
bRun = True

def f_conversion(celsius):
    return (float(celsius) * (9/5) + 32)

print('Enter a temperature in Celsius or 0 (zero) to quit.')

while bRun:
    tempInput = float(input('Enter Celsius: '))

    if tempInput == 0:
        bRun = False
        print('Ok, I love you. Bye-bye.')
        break
    
    print(str(f_conversion(tempInput)))
