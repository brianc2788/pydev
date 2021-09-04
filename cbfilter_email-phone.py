'''
phone-email-cb-extractor.py
---------------------------
from 'Automating the Boring Stuff..'
filters all text out of the clupboard
except for phone numbers and emails.
going by the book;
not how i would do it.

-works mostly as advertised, but
 the emailRegex was a serious
 problem and crashed the
 interpreter, so for now, it
 just extracts phone numbers.

github.com/user5260/pyscripts
'''
import re
import pyperclip

#my bad regex
#phoneExpr = re.compile(r'(\d\d\d)?-?(\d\d\d)-(\d\d\d\d)')
#the good regex from the book -- verbose format
phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				# area code, if present
	(\s|-|\.)?						# ac seperator, if present
	(\d{3})							# 1st three digits
	(\s|-|\.)						# seperator
	(\d{4})							# final four digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?	# extension
	)''', re.VERBOSE)

# Email Regex -- better than mine, but don't like the characters
#				 included for the usernames, etc. also, odd groupings.
# will match most, typical email/email-formats
# emailRegex = re.compile(r'''(
# 	[a-zA-Z0-9._-+%]+			# username
# 	@							# @ seperator
# 	[a-zA-Z0-9.-]+				# domain name
# 	(\.[a-zA-Z]{2,4})			# top-level-domain name
# 	)''', re.VERBOSE)

# Finding matches in the clipboard
cbText = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(cbText):
	phoneNum = '-'.join([groups[1],groups[3],groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)
# for groups in emailRegex.findall(cbText):
# 	matches.append(groups[0])

# Copy results back to the clipboard.
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('the following matches were found and pasted to the clipboard: ')
	print('\n'.join(matches))
else:
	print('no matches')
