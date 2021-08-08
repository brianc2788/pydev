'''
browserFindMe.py
----------------
Run this Python script to open your
web browser and find my facebook,
github, and email.
Messing around with webbrowser module;
preparing to use things like this with
Selenium.

In other words,
This app will open the user's browser
with tabs open to my facebook, my github,
and a google search for my username.
Lastly, also opens the user's email client;
for me, that is Thunderbird. Opens a new
draft email composition with my email
address as the reciever.

brianc2788@gmail.com
'''
import webbrowser

# FB Page.
webbrowser.open('https://www.facebook.com/brianc2788')
# GitHub.
webbrowser.open_new_tab('https://www.github.com/user5260')
# Email me. Opens the user's mail client; for me, that's Thunderbird.
webbrowser.open('mailto:brianc2788@gmail.com')

# Open google with a search for my name.
webbrowser.open_new_tab('https://www.google.com/search?q="brianc2788"')
''' kinda surprised at the results here. some of my other accounts come up,
like for kaggle. I guess I shouldnt be surprised; google employs excellent
web crawlers and I use, basically, the same, exact username for most of
my accounts.
Fun Fact: Nope, my dad doesn't live at that address; his brothers kicked him
out right before he got diagnosed and died of cancer.
They sure are great, aren't they? lol. Even better; target my mom, his
very, very estranged wife, and try to get money out of her.
Fuck the Chiodo family, lol. Annoying, because I have to change my name.
'''
