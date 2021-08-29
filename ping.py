'''
ping.py - call the ping command.
--------------------------------
host machine pings an address.

github.com/user5260
'''
import subprocess
import sys

cmd_ping = '/bin/ping'
pingParams = '-c 1' # send/count 1 packet.
#if platform.system() == Windows:
#     pingParams = '-n 1'
dest = 'www.google.com'

# using subprocess instead of os.system()
# or call(). This way, we create a child
# process that is easier to work with.
p = subprocess.Popen([cmd_ping,pingParams,dest],shell=False,stderr=subprocess.PIPE)
# output shows in the terminal/logs
out = p.stderr.read(1)
sys.stdout.write(str(out.decode('utf-8')))
sys.stdout.flush()
