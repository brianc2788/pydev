'''
just to help me remember how to get output
from a child process with the subprocess module.
'''
import sys,subprocess
cmd1 = ['ls','-lh'] #list directory w/human-readable nums.
proc1 = subprocess.Popen(cmd1,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
rawOutput = proc1.stdout.read()
strOutput = rawOutput.decode('utf-8')
print(strOutput)
#sys.stdout.write(rawOutput.decode('utf-8')
#sys.stdout.flush()
