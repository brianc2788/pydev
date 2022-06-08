#-*-coding:utf8;-*-
#qpy:console
'''
simple http server for file sharing.
because i intend on using this with
qpython on my android, i've decided
to take input rather than parse sys-
tem arguments. other design choices
may apply.
authored by brianc2788@gmail.com
http://www.github.com/user5260
'''
from sys import exit
from os import path, chdir
#from os import chdir
import http.server
import socketserver

port = 8000
rhandler = http.server.SimpleHTTPRequestHandler

server = socketserver.TCPServer(
         ("", port),
         rhandler
         )

""" Get a target dir from the user. Check for valid target. """
'''
I don't much like this setup, but I really
wanted to use a python while loop. thanks.
'''
rdir = '/storage/emulated/0/'
tdir = ''
fdir = ''

while not path.exists(fdir):
    tdir = input('Enter dir: {}'.format(rdir))
    fdir = rdir + tdir

try:
    chdir(fdir)
except BaseException:
    print('Encountered a problem. You may lack user priviledges.\nExiting...')
    exit()

""" Run the server until the user quits. """
try:
    server.serve_forever()
    print('Listening for HTTP requests on port {}...'.format(port))
except BaseException:
    if KeyboardInterrupt:
        exit(0)
    else:
        print('an error has occurred. exiting...')
        exit()
