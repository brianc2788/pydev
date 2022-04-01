'''
format-br2csv.py
-------------------------
Parse "Bottle-Record" text files & convert
to csv format.

TODO:
	- Everything is functioning, but
	  need to add i/o.
-------------------------
Authored by brianc2788@gmail.com
'''
import os,sys,re

# Regex w/groupings
BRregex = re.compile(r'''(	# Group 0 - Full line containing the match.
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
	(.+)				# Group 6 - Notes. Goes up to newline char unless re.DOTALL is used. Was using '[\w\s]+' but missed some notes.
	)''',re.VERBOSE)

filename = "mock-br.txt"	# hardcoded filename - for now.
fileList = []				# list of lines to be read from file.

with open(filename,mode='r') as iFile:
	if not iFile.readable():
		print('Failed to open file for reading. Aborting execution...')
		sys.exit(1)
	else:
		fileList = iFile.readlines()

searchList = []
for line in fileList:
	if BRregex.search(line) != None:
		searchList.append(BRregex.search(line))

# Create final list object to pass to fileObject.writelines().
writeList = []
writeList.append("DATE,TIME,BRETURNED,BRECIEVED,WINDOW,DETAILS\n")	# First line of CSV format - table columns.

nGroupFirst = 2
nGroupLast = 8

for matchObj in searchList:
	csvString = ''
	for groupnum in range(nGroupFirst,nGroupLast):
		csvString += matchObj.group(groupnum)
		if groupnum != (nGroupLast-1):
			csvString += ','
		else:
			csvString += '\n'
	writeList.append(csvString)

newFileName = filename[:-3]
newFileName += 'csv'

with open(newFileName,mode='w') as fOut:
	if not fOut.writable():
		print("Couldn't create/open file for writing. Aborting operations...")
		sys.exit(1)
	else:
		fOut.writelines(writeList)

print("Saved file ",newFileName," to disk.\nExiting...")