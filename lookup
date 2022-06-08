#!/usr/bin/env python3
'''
lookup - python3 script
------------------------
I had written a version of this
script earlier this year that just
stopped working one day.
Rather than debug/troubleshoot, I
decided to change the design to use
BeautifulSoup4.
Once again, this script can be called
from the commandline and takes an arg
of the user's word to scrape and print
a definition gotten from the merriam-
webster online dictionary.

Authored by: brianc2788@gmail.com
'''
from bs4 import BeautifulSoup
import requests,sys

""" Request URL and soupify. Print Definition(s). """
def main():
    """ Print usage if no words/args. """
    if len(sys.argv) == 1:
        print('USAGE:\n$> lookup <word1> <word2> <...>')
    
    else:
        nArgs = 1
        while nArgs < len(sys.argv):
            """ Request the URL; pass text to bs4. """
            lookupWord = sys.argv[nArgs]
            webAddr = 'https://www.merriam-webster.com/dictionary/'+lookupWord+'/'
            '''
             Handle exception in case of no internet connection.
             socket.gaierror (get address info error); name resolution failure.
             Presumably, the first thing these modules try to do is resolve
             the domain name through the dns. Raises an exception & breaks the loop.
            '''
            try:
                req = requests.get(webAddr)
            except Exception:
                print('An error has occurred while trying to establish a connection with the internet.')
                break
            # Soupify; create soup object & designate the python built-in html parser.
            soup = BeautifulSoup(req.text,'html.parser')
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
            nArgs += 1
        
    print('\nPowered by Merriam-Webster.com\nAuthored by brianc2788@gmail.com')

if __name__ == '__main__':
    main()
