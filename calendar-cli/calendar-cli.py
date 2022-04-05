'''
calendar-printer.py
-------------------
Description:
Use CLI to prompt user for month & year. Print calendar (character string).

Authored by brianc2788@gmail.com
https://github.com/user5260/pyscripts/calendar-printer
'''
from CalObj import CalObj

def main():
	co1 = CalObj(4,2022)
	print('got month: ',co1.month,'\ngot year: ',co1.year,end='\n')

if __name__ == '__main__':
	main()