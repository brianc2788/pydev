'''
CalObj.py
---------
Calendar object class.
Authored by brianc2788@gmail.com
'''

'''
CalObj - Calendar Object.
'''
class CalObj:
    def __init__(self,month,year):
        self.month = month
        self.year = year
        self.FirstWeekday = ''
        self.leapyear = False

    def f1(self):
        print('function 1')