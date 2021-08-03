'''
regex2.py
brianc2788@gmail.com
- Might use the comments to
  create an informative
  jupyter notebook.
- Comments would be
  adapted to Markdown.
'''

import re

# Create a raw string of a regex.
rawRegex = r'[a-zA-Z\d_]'

# Use the raw version to create a RegEx object.
# This regular expression will match the
# characters specified
regex1 = re.compile(rawRegex)

testStr1 = 'regex1 will match this string with anything alpha-numeric (upper and lower case) and underscores (_). Not the parentheses, though.'
matchList = regex1.findall(testStr1)

print('testStr1 = ' + testStr1)
print(matchList)