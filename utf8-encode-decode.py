'''
encoding and decoding strings
to/from unicode.
'''

string1 = 'hello'
bytes1 = string1.encode('utf-8')
print('printing a bytes object with its decode method.')
print(bytes1.decode('utf-8'),end='')

