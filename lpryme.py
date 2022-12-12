#!/usr/bin/env python3
'''
genpryme.py
-----------
outputs a list of prime numbers (sep by \n), given
the ceiling specified by the user on the cmdline.
https://brianc2788.github.io/
'''
import sys

try:
	from ispryme import isPrime
	#import ispryme
except ImportError:
	print('Requires ispryme.py. See source for info.')
	sys.exit(1)

def main():
	if len(sys.argv) < 2:
		usage()

	arglist = []
	for arg in sys.argv[1:]:
		arglist.append(int(arg))

	for nMax in arglist:
		if nMax > 99999999999:
			print('saving you from yourself... abort.')
			sys.exit(1)
		buf = nMax
		while buf > 0:
			try:
				prime = isPrime(buf)
				if prime == False:
					buf = buf-1
				elif prime == True:
					print(buf)
					break
			except KeyboardInterrupt:
				print(f'\nUser abort.\nCeiling before break: {buf}')
				break

def usage():
	print('enter ceiling for testing primes.')
	sys.exit(1)

if __name__ == '__main__':
	main()
