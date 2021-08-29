#! /usr/bin/env python3
'''
portscan-regex.py
-----------------
This is incomplete.
For now, it just connects to my
raspberry pi, reads the banner,
filters banner through a regular
expression.
-----------------
'''
import re
import socket

# protocolRegex = re.compile(r'[ftp{3}FTP{3}http{4}HTTP{4}ssh{3}SSH{3}]')
protocolRegex = re.compile(r'[ftp|FTP|https|HTTPS|ssh|SSH|mysql|MYSQL]{1,4}')

sock1 = socket.socket()
sock1.settimeout(10)

target1 = '192.168.1.215'
sshport = 22

sock1.connect((target1,sshport))
serverBanner = str(sock1.recv(1024))
print('--------------------------------------------')
print('Downloaded Banner:\n'+serverBanner)
print('--------------------------------------------')
print('Protocol RegExp. results (list):\n'+str(protocolRegex.findall(serverBanner)))
# try:
#     serverBanner = str(sock1.recv(1024))

# print('RESULTS:\n--------')
# for n in protocolRegex.findall(serverBanner):
#     print(n)
