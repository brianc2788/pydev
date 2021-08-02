'''
searching for a substring
'''
banner = 'Some FTP Server'
print('Full string (banner): '+banner)

n1 = banner.find('FTP')
substring1 = ''

while n1 < len(banner):
    substring1 += banner[n1]
    n1 += 1

print('Sub-string: '+substring1)
