'''
regex3.py
-----------
Another bite-sized (600 byte-sized?)
python script. For practice with
regular expressions ('re' module).

This time, went with creating a
regular expression that matches
patterns that are formatted like
time; e.g. HH:MM.
--------------------------------------
brianc2788@gmail.com
'''
import re

# raw string.
# save ourselves a variable this time
# and set it equal to the return value
# of re.compile() with itself passed
# by ref.
regex1 = r'\d{2}:\d{2}'
regex1 = re.compile(regex1)

testString = 'Last night, I got home around 10:03. What a crazy evening!'

print(str(regex1.findall(testString)))
