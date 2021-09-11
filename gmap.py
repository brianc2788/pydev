'''
gmap.py
-------
if the user posseses a
valid address in their
clipboard, running this
script will launch
google maps in a browser;
centered at, of course,
the given address.
'''
import os,re,pyperclip

addrRegex = re.compile(r'''(
	(\d)+				# street num
	([a-zA-Z0-9])+		# street name
	([a-zA-Z]{2,3})		# ave, rd, etc.
	)''',re.VERBOSE)

testStr = input('enter addr: ')

resultsL = addrRegex.findall(testStr)

for n in resultsL:
	print(str(n.groups()))
