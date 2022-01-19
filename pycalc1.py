#! /usr/bin/env python3
# pycalc1

def Calculate(num1,op1,num2):
    num1 = int(num1)
    num2 = int(num2)
    if op1 == '+':
        return str(num1+num2)
    elif op1 == '-':
        return str(num1-num2)
    elif op1 == '*':
        return str(num1*num2)
    else:
        try:
            return str(num1/num2)
        except ZeroDivisionError:
            print('cant divide by zero.')

print(
'''
Enter your operation and press return.
Example: '2+2','12/3',etc...
''')

while 1:
    string1 = input('ENTER: ')
    Num1 = ''
    Num2 = ''
    CalcOp = ''

    for x in string1:
        if x.isdigit():
            Num1 += x
        elif x == '/':
            CalcOp = '/'
        else:
            CalcOp = x
            break

    Num2 = string1[string1.find(CalcOp)+1:]

    print(Calculate(Num1,CalcOp,Num2))
