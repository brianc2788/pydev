'''
br-format.py
-------------------------
Parse & extract data from "BR" files.
In the future, be sure not to use commas
in the "DETAILS" column when recording
new data.
Overall, very satisfied with this.
-------------------------
Authored by brianc2788@gmail.com
'''
import os,sys,re

'''
Parse cmdline args.
'''
nArglen = len(sys.argv)
if nArglen != 2:
	print("Usage: $ python BR-formatter.py <BR-file>")
	sys.exit(1)
else:
	filename = sys.argv[1]
	if not os.path.isfile(os.path.join(os.getcwd(),filename)):
		print("File not found.\nExiting...")
		sys.exit(1)

'''
Declare Regex w/groupings.
'''
BRregex = re.compile(r'''(	# Group 0 - Full line containing the match.
	(\d+\/\d+)				# Group 1 - Date
	\s
	(\d{1,2}:\d{1,2})		# Group 2 - Time
	\s
	(\d)					# Group 3 - B. Recieved
	\s
	(\d)					# Group 4 - B. Returned
	\s
	(LEFT|MID|RIGHT)		# Group 5 - Window
	\s
	(.+)					# Group 6 - Details; without passing re.DOTALL, doesnt include newline chars.
	)''',re.VERBOSE)

'''
Prepare a list and readlines() from the br file.
'''
fileList = []				# list of lines to be read from file.

with open(filename,mode='r') as iFile:
	if not iFile.readable():
		print('Failed to open file for reading. Aborting execution...')
		sys.exit(1)
	else:
		fileList = iFile.readlines()

'''
Create a list a re.match objects. Create a final list object
made of 
'''
searchList = []
for line in fileList:
	if BRregex.search(line) != None:
		searchList.append(BRregex.search(line))

# Create final list object to pass to fileObject.writelines().
writeList = []
writeList.append("DATE,TIME,BRETURNED,BRECIEVED,WINDOW,DETAILS\n")	# First line of CSV format - table columns.

# Group indices that we want from the re.match object.
nGroupFirst = 2
nGroupLast = 8

for matchObj in searchList:
	csvString = ''
	for groupnum in range(nGroupFirst,nGroupLast):
		# switch the order of BRECV and BRETRN. A matter of preference.
		if groupnum == 4:
			csvString += matchObj.group(groupnum+1)
		elif groupnum == 5:
			csvString += matchObj.group(groupnum-1)
		else:
			csvString += matchObj.group(groupnum)

		if groupnum != (nGroupLast-1):
			csvString += ','
		else:
			csvString += '\n'
	writeList.append(csvString)

# Using a slice of the original filename string; sans extension.
newFileName = filename[:-3]
newFileName += 'csv'

# Create/write operation.
with open(newFileName,mode='w') as fOut:
	if not fOut.writable():
		print("Couldn't create/open file for writing. Aborting operations...")
		sys.exit(1)
	else:
		fOut.writelines(writeList)

sys.exit(0)