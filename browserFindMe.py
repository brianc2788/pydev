#! /usr/bin/env python3
'''
browserFindMe.py
----------------
Overall, opens a webrowser and makes 3 requests
in 3 separate tabs. These 3 URIs request my
Facebook profile, my github user page, and a
Google search of a common username that I use.
Also opens the user's default MIME application
to compose an e-mail to my gmail account.

brianc2788@gmail.com
'''
import webbrowser

# FB Page.
webbrowser.open('https://www.facebook.com/brianc2788')
# GitHub.
webbrowser.open_new_tab('https://www.github.com/user5260')
# Open google with a search for my username.
webbrowser.open_new_tab('https://www.google.com/search?q="brianc2788"')

# Opens the user's mail client; for me, that's Thunderbird.
webbrowser.open('mailto:brianc2788@gmail.com')
