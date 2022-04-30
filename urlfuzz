#!/usr/bin/env python3
'''
Just a crappy little fuzzer to help familiarize
myself with the requests module.
"Http requests for humans"
Nice!
Actually, not too bad; for a first attempt.

TODO:	- Add performance timer.
		- Various code clean-up, including better
		  parsing and processing of args.

Authored by brianc2788@gmail.com
'''
import sys,requests

if len(sys.argv) == 1:
	print('Usage: >$ urlfuzz <url>')
	print("Enter <url> in the form 'protocol://host.tld/")
	print('Be sure to include a trailing forward slash (/).')
else:
	base_url = sys.argv[1]

#test_str = 'index.htm'

def main():
	r = requests.get(base_url)

	if r.status_code != requests.codes.ok:
		print(r.status_code)
		sys.exit(0)
	else:
		print('Got response from domain; starting fuzzer.\nCtrl+C to cancel...')

	# Main loop.
	try:
		for n in range(99999):
			req = requests.get(base_url+str(n),timeout=1.0)

			if req.status_code == requests.codes.ok:
				print('\n{0}{1} - Code {2}'.format(req.url,n,req.status_code))
				if n % 50 != 0:
					print("\n",end='')
			else:
				print('.',end='')
	except:
		if KeyboardInterrupt:
			print('Fuzz aborted by the user.')
			sys.exit(0)
		else:
			print('An error has occurred.')
			sys.exit(1)

if __name__ == '__main__':
	main()
