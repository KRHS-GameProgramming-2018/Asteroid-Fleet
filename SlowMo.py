import pygame, sys, math, random
from Ship import *
width = 1100
height = 900

class SlowMo(pygame.sprite.Sprite):
    def __init__(self, image, startPos = [0,0]):
            pygame.sprite.Sprite.__init__(self, self.containers)
            self.image = pygame.transform.scale(pygame.image.load(image),[50,50])
            self.rect = self.image.get_rect(center=[random.randint(0,width),(50)])
            self.radius = (self.rect.width/2 + self.rect.height/2)/2
            self.living = True  
            self.kind = "matrix"
            self.speedx = 0
            self.speedy = 3 #random.randint(0,2)
            self.speed = [self.speedx, self.speedy]

            if self.speed == 0:
                self.living = False
    
    
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
  
    def collideShip(self, other):
        if not(self == other):
            self.living = False
   
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)  
     
                                
    def update(*args):
        self = args[0]
        size = args[1]
        self.move()
