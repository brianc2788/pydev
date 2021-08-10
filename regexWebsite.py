import re

regex1 = re.compile(r'\.\D{3}')
stringInput = 'something something.net something.com something.org something.eu'
print(regex1.findall(stringInput))

for match in regex1.findall(stringInput):
    print(match)
