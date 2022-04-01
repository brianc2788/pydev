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
BRregex = re.compile(r'''(	# Group 0 - Full match
	(\d+\/\d+)				# Group 1 - Date
	\t
	(\d{1,2}:\d{1,2})		# Group 2 - Time
	\t
	(\d)					# Group 3 - B. Recieved
	\t
	(\d)					# Group 4 - B. Returned
	\t
	(LEFT|MID|RIGHT)		# Group 5 - Window
	\t
	([\w\s]+)				# Notes. Goes up to newline char.
	)''',re.VERBOSE)

filename = "mock-br.txt"
ftext = None

with open(filename,mode='r') as txtfile:
	ftext = txtfile.read()

matchList = BRregex.findall(ftext)

print("matchList: ",len(matchList))
for n in matchList:
	print(n)

# TODO:
# - create a list or use a module (csv,pandas,etc) to create
#   an object for writing a new csv file.
# - use matchObj to get regex groups to assign variables
#   when writing the new csv file(?).

matchObj = BRregex.search(ftext)