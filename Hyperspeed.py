import pygame, sys, math, random
from Ship import *
width = 1100
height = 900

class Hyperspeed(pygame.sprite.Sprite):
    def __init__(self, image, startPos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(pygame.image.load(image),[50,50])
        self.rect = self.image.get_rect(center=[random.randint(50,width-50),(700)])
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.living = True  
        self.kind = "hype"
    
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
  
    def collideShip(self, other):
        if not(self == other):
            self.living = False
                                
    def update(*args):
        self = args[0]
        size = args[1]
