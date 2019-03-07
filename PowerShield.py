import pygame, sys, math, random
from Ship import *
width = 1100
height = 900

class PowerShield():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[50,50])
        self.rect = self.image.get_rect(center=[random.randint(50,width-50),(500)])
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.living = True
    
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
  
    def collideShip(self, other):
        if not(self == other):
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.radius + other.radius > self.getDist(other.rect.center):
                                self.living = False
