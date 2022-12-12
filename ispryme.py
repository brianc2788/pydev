#!/usr/bin/env python3
'''
# ispryme.py #
--------------
Tests the primality of each positional argument given.
https://brianc2788.github.io/
'''
import sys

def main():
	if len(sys.argv) < 2:
		usage()

	nlist = sys.argv[1:]
	for a in range(len(nlist)):
		testnum = int(nlist[a])
		if isPrime(testnum):
			print(f'{testnum} is prime.')
		else:
			print(f'{testnum} not prime.')

def usage():
	print(f'''Need numbers to test primality.
		cmdline$ {sys.argv[0]} num [[num1] [num2] [...]]''')

""" Returns True or False based on primality of input (int). """
def isPrime(numIn):
	p = True

	if numIn <= 1:
		return False

	for n in range(2,numIn):
		if numIn % n == 0:
			p = False

	return p

if __name__ == '__main__':
	main()
