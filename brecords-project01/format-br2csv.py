'''
format-br2csv.py
-------------------------
Parse "Bottle-Record" text files & convert
to csv format.

TODO:
	- finished BRregex. Works well; found all entries in BR-mar2022.txt.
-------------------------
Authored by brianc2788@gmail.com
'''
import os,sys,re,csv

'''
status:
test RE with test bottle-record.
'''

# Regex w/groupings
BRregex = re.compile(r'''(
	(\d+\/\d+)				# Date
	\t
	(\d{1,2}:\d{1,2})		# Time
	\t
	(\d)					# B. Recieved
	\t
	(\d)					# B. Returned
	\t
	(LEFT|MID|RIGHT)		# Window
	\t
	([\w\s]+)				# Notes. Goes up to newline char.
	)''',re.VERBOSE)

filename = "mock-br.txt"
ftext = None

with open(filename,mode='r') as txtfile:
	ftext = txtfile.read()

matches = BRregex.findall(ftext)

print("matches: ",len(matches))
for n in matches:
	print(n)