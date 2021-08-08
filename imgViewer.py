'''
imgViewer.py
displays an image specified
by the user.
Uses pygame module.

eventually, may use 'os' library
to show all images or thumbnails
in a directory.

brianc2788@gmail.com
'''
import os
from sys import exit
import pygame

pyScreen = pygame.display.set_mode((1200,750))

imgPath = input('enter path to img: ')
os.chdir(imgPath)
imgName = input('enter img filename: ')

imgSurface = pygame.image.load(os.path.join(imgPath,imgName)).convert()
pyScreen.blit(imgSurface,(0,0))
pygame.display.update()
