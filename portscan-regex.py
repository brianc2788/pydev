#! /usr/bin/env python3
'''
portscan-regex.py
-----------------
Trying to remember some socket stuff
from Python 2. Combining that with
Regular Expressions.

[Comments]
This script is incomplete as there is something
wrong with how I'm defining protocolRegex.
Can see why Python is so popular with
pentesting.
-----------------
clone this repo for more, practical examples.
git clone github.com/user5260/pyscripts
'''
import re
import socket

protocolRegex = re.compile(r'[ftp{3}FTP{3}http{4}HTTP{4}ssh{3}SSH{3}]')

sock1 = socket.socket()
sock1.settimeout(10)
sock1.connect(('192.168.1.215',22))

serverBanner = str(sock1.recv(1024))

print(str(protocolRegex.findall(serverBanner)))
