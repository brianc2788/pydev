#!/usr/bin/env python3
'''
lookup - python3 script
------------------------
Modified version of 'lookup' to work better
with the Qt Python3 Interpreter from 3-Labs
for Android.
Basically, I haven't found a convenient way in
the app to pass command-line arguments to python
modules, so I'm adding a prompt. The user now
enters their desired word interactively.
# TODO:
    - **Still throwing an exception in the try block.**
    - Proper Android app?
    - Android app containing 1 or 2 "Activities" - easy?
    - Use uname or similar to detect OS and take
      the appropriate course of action; CLI args or prompt.

Authored by: brianc2788@gmail.com
'''
from bs4 import BeautifulSoup
import requests,sys

""" Request URL and soupify. Print Definition(s). """
def main():
    """ Prompt user for a word to look up. """
    lookupWord = input('Enter: ')
    webAddr = 'https://www.merriam-webster.com/dictionary/'+lookupWord+'/'
    '''
        Handle exception in case of no internet connection.
        socket.gaierror (get address info error); name resolution failure.
        Presumably, the first thing these modules try to do is resolve
        the domain name through the dns. Raises an exception & breaks the loop.
    '''
    try:
        getRequest = requests.get(webAddr)
    except Exception:
        print('An error has occurred while trying to establish a connection with the internet.')
        sys.exit(1)
    # Soupify; create soup object & designate the python built-in html parser.
    soup = BeautifulSoup(getRequest.text,'html.parser')
    # Create list of CSS class attributes
    # Tag is <span class="dtText"><\span>
    resultList = soup.select('.dtText')
    # Print the word & its definition(s).
    entryNum = 1
    print('*',lookupWord.upper(),sep='')
    if len(resultList) == 0:
        print('No dictionary entries found.')
    else:
        for r in resultList:
            print(entryNum,r.getText())
            entryNum += 1
    
print('\nPowered by Merriam-Webster.com\nAuthored by brianc2788@gmail.com')

if __name__ == '__main__':
    main()
