'''
read_csv_pw_manager.py
----------------------
quick little script to read my
usernames and passwords for a
password generator/reader.
hopefully use some good
encryption modules (using real
algorithms) in the script later.

for now, using csv file that was
exported from firefox browser
with around 7 entries that had
their usernames and passwords
replaced with false ones.

github.com/user5260/pyscripts
brianc2788@gmail.com
'''
import sys
import pandas as pd

# blank obj; None type.
# to become panda csv obj.
csv1 = None

# read the file & parse with pandas.
with open('special1.csv',mode='rb') as file1:
	if not file1.readable():
		print('Error: file not found.\n',end='')
		del file1
		sys.exit()
	else:
		csv1 = pd.read_csv(file1)

# my lack of python skills shows
# but so does my bg in c/cpp - lol.
rownum = len(csv1['username'])
for n in range(rownum):
	un = csv1['username'][n]
	pw = csv1['password'][n]
	print(un,end='')
	for n in range(30-len(un)):
		print(' ',end='')
	print(pw,end='\n')