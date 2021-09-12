'''
gmap.py
-------
prompts the user for an address.
the regex used to find an address
is not perfect, but will find most
addresses in a format akin to:
'## Street Name, City NY'
opens google maps in a new browser.
if the expression doesn't like the
address you inputted, it won't try
to open a browser.
-other notes-
city must be limited to one word, unfortunately.
'''
import re,webbrowser

# address for just street addresses with city & state,
# e.g. '99 Something Drive, Buffalo NY'
addrRegex = re.compile(r'\d+\s\w+\s\w+\,\s\w+\s[A-Z]{2}')
# tried verbose format regex; failed.
# addrRegex = re.compile(r'''(
# 	([\d]+)			# street num
# 	(\s) 			# space
# 	([a-zA-Z0-9]+ 	# street name
# 	)''',re.VERBOSE)

testStr = input('enter addr: ')

resultsList = addrRegex.findall(testStr)


if not len(resultsList) > 0:
	print('couldn\'t detect a valid street address in your input.')
else:
	searchStr = 'https://google.com/maps/place/'
	for n in resultsList[0]:
		if n == ' ':
			searchStr += '+'
		else:
			searchStr += n
	#DEBUG: printing searchStr to make sure the loop formatted it correctly
	print(searchStr)
	webbrowser.open_new(searchStr)
