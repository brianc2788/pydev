'''
# dirserve 0.2 #
builds some-what on my earlier "httpserv-droid.py" script;
mostly just the new class (httpserve).
simple http server. using stdio for easier use on droid.
tested on "qpython" (qpy3l) and "python3 ide". should be
working now, but had issues with some builtins (format strings,
some socketserver methods, etc.). again, all issues seem to be fixed.
android sucks, by the way. especially version 12.
https://brianc2788.github.io/
'''
__author__ = 'brianc2788'

# Standard Python Libs.
import os, sys, socketserver, http.server
# Third-party libraries.
import requests

class httpserve(object):
    def __init__(self, ip4='', port=80):
        self.ip4 = '' #Defaults to localhost (127.0.0.1).
        self.port = 8080 #must be above 1024 on droid.
        self.rhandler = http.server.SimpleHTTPRequestHandler
        self.server = socketserver.TCPServer( (self.ip4, self.port), self.rhandler)

def main():
    rootdir = os.getcwd()
    targetdir = rootdir + '/'
    s = httpserve()
    
    print(' '.join(('Current directory: ', rootdir)))

    target_exists = False
    while not target_exists:
        userdir = input('Enter: ')
        if os.path.exists(os.path.join(rootdir, userdir)):
            targetdir = os.path.join(rootdir, userdir)
            target_exists = True
        else:
            print('Couldn\'t find {0}.\nCurrent dir: {1}'.format(userdir, rootdir))

    os.chdir(targetdir)

    print('Serving '+targetdir+' on '+s.ip4+str(s.port)+'.')
    print('Use ctrl+c to stop...')
    try:
        s.server.serve_forever()
    except:
         if KeyboardInterrupt:
             print('Server QUIT requested by user...')
             s.server.shutdown()
             sys.exit(0)
         else:
            s.server.shutdown()
            sys.exit(1)

if __name__ == '__main__':
    main()
