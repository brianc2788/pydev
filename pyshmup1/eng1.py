'''
Engine1 class. Using pygame.

Authored by: brianc2788@gmail.com
'''
import os,pygame

class Engine1():
    def __init__(self,wtitle,screenw,screenh):
        self.pygame = pygame
        self.screen = pygame.display.set_mode((screenw,screenh))
        pygame.display.set_caption(wtitle)
    
    def makeImg(self,img_path):
        if os.path.isfile(img_path):
            return pygame.image.load(img_path).convert()
        else:
            return None
    
    def updateScreen(self):
        pygame.display.update()
    
    def quitPygame(self):
        pygame.quit()