# practicing regular expressions
# with python
# [Comments]
# Leaving this file as-is, for now.
# Script works and will find and print
# any patterns that match the regex
# in strings that are passed to the
# member .findall().
import re

testStr = 'test string, this is.'

# This regex will match patterns of anything containing:
# a-z = lowercase 'a' through 'z', alphabet.
# A-Z = Uppercase, same as above.
# \d = any digit character, 0-9
# _ = also, the underscore (_) character.
regex1 = '[a-zA-Z\d_]'

# Turn it into a regex object/type.
regex1 = re.compile(regex1)

# Compare and find the regex pattern in the test string.
print(regex1.findall(testStr))
