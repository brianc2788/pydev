'''
trackTime1.py
-------------
Prints the system time;
uses 12-hour format.
Just for fun.
-------------
Written with Qpython for Android.
Authored by brianc2788@gmail.com
Github: https://www.github.com/user5260
https://user5260.github.io
'''
import time

""" time.localtime() wrapper. """
def getSysTime():
    return time.localtime()

""" Print local time. """
def printT(timeObj):
    tHours = timeObj.tm_hour
    tMins = timeObj.tm_min
    tSecs = timeObj.tm_sec
    """ Format & print hour(s). """
    if tHours == 0:
        tHours = 12
    elif tHours > 12:
        tHours -= 12
    print(tHours,':',sep='',end='')
    """ Format & print minutes. """
    if tMins < 10:
        print('0',tMins,':',sep='',end='')
    else:
        print(tMins,':',sep='',end='')
    """ Format & print seconds. """
    if tSecs < 10:
        print('0',tSecs,sep='')
    else:
        print(tSecs)

""" main """
def main():
    lcount = 1
    printx = input('Enter seconds to run: ')
    printx = int(printx)
    for lcount in range(printx):
        timeL = getSysTime()
        print(str(lcount+1),end=' - ')
        printT(timeL)
        time.sleep(1)

if __name__ == '__main__':
    main()