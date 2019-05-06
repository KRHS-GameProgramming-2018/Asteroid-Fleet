import pygame, sys, math, random
width = 1100
height = 900

class Countdown(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.currentImage = 0
        self.countImages = [pygame.image.load ("Screen Display/Background/images/3.png"),
                       pygame.image.load ("Screen Display/Background/images/2.png"),
                       pygame.image.load ("Screen Display/Background/images/1.png"),
                       pygame.image.load ("Screen Display/Background/images/1.png")]
        self.image = self.countImages[self.currentImage]
        self.rect = self.image.get_rect(center = [550,350])
        self.lastImage = len(self.countImages)-1
        self.aniTimer = 0
        self.aniTimerMax = 60/1
        self.done = False
        
    def update(*args):
        self = args[0]
        if self.aniTimer < self.aniTimerMax:
            self.aniTimer += 1
        else:
            self.aniTimer = 0
            if self.currentImage < self.lastImage:
                self.currentImage += 1
                self.image = self.countImages [self.currentImage]
            else:
                self.done = True
                print "images changed"
            
        
    
