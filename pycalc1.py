#! /usr/bin/env python3
# pycalc1
import string

def Calculate(num1,op1,num2):
    num1 = int(num1)
    num2 = int(num2)
    if op1 == '+':
        return str(num1+num2)
    elif op1 == '-':
        return str(num1-num2)
    elif op1 == '*':
        return str(num1*num2)
    elif op1 == '/' & num2 != 0:
        return str(num1/num2)

string1 = '20+14'
Num1 = ''
Num2 = ''
CalcOp = ''

for x in string1:
    if string1[x] != '+' & string1[x] != '-' & string1[x] != '*' & string1[x] != '/':
        Num1.append(string1[x])
    else:
        CalcOp = string1[x]
        break

for x in string1:
    if string1[x] != CalcOp:
        continue
    else:
        x = x + 1
        Num2.append(string1[x])

print(Calculate(Num1,CalcOp,Num2))
