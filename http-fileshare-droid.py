#-*-coding:utf8;-*-
#qpy:console
'''
simple http server for file sharing.
honestly, i made this for my android
because i couldn't figure out how to run
modules with qpython.
authored by brianc2788@gmail.com
http://www.github.com/user5260
'''

import sys
import http.server
import socketserver

port = 8000
rhandler = http.server.SimpleHTTPRequestHandler

server = socketserver.TCPServer(
         ("", port),
         rhandler
         )

""" Run until user exits """
try:
    server.serve_forever()
except BaseException:
    if KeyboardInterrupt:
        sys.exit(0)
    else:
        print('an error has occurred. exiting...')