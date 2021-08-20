'''
imgViewer.py
displays an image specified
by the user.
Uses pygame module.

[Bug Fixes]
-8/20/2021
Fixed some bugs related to user
input causing crashes.
Redesigned the code layout,
so if errors occur, the program
won't try to continue, as before.
i.e., still prompting for file name
after the directory was proven invalid.

brianc2788@gmail.com
'''
import os
import re
from sys import exit
import pygame

# unused regular expression for image file extensions.
# leaving it, because it works for base file names.
#imgRegex = re.compile(r'\S+\.[bmp|png|jpg|jpeg]{3,4}')

pyScreen = pygame.display.set_mode((1200,750))

imgPath = input('enter path to img: ')

# check if input is a valid directory.
if not os.path.isdir(imgPath):
    print('invalid directory.')
else:
    os.chdir(imgPath)
    imgName = input('enter img filename: ')
    
    # check if filename given is present in the directory.
    dirContents = os.listdir()
    fileFound = False
    for n in dirContents:
        if n == imgName:
            fileFound = True
            break
    
    if fileFound:
        imgSurface = pygame.image.load(os.path.join(imgPath,imgName)).convert()
        pyScreen.blit(imgSurface,(0,0))
        pygame.display.update()
    else:
        print('file not found')
