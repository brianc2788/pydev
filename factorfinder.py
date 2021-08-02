#! /usr/bin/env python3

# factorfinder.py

bRun = 1
while bRun:
    facList = []
    str1 = input('enter a number to print factors or 0 to quit: ')
    val1 = int(str1)
    if val1 == 0:
        bRun = 0
        break
    for x in range(1,val1,1):
        if val1 % x == 0:
            facList.append(x)
            print('factor:',x)
    if val1 != 1 & val1 != 2 & len(facList) < 2:
        print('is prime')
        
