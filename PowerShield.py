import pygame, sys, math, random
from Ship import *
width = 1100
height = 900

class PowerShield(pygame.sprite.Sprite):
    def __init__(self, image, startPos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(pygame.image.load(image),[50,50])
        self.rect = self.image.get_rect(center=[random.randint(50,width-50),(500)])
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.living = True  
        self.kind = "shield"
        self.images = [pygame.transform.scale(pygame.image.load("PowerUps/Shield/images/shield.png"),[50,50]),
                       pygame.transform.scale(pygame.image.load("PowerUps/Shield/images/shield2.png"),[50,50])]
                       
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.aniTimer = 0
        self.aniTimerMax = 180/10
    
    
    
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
  
  
    def animate(self):
        if self.aniTimer < self.aniTimerMax:
            self.aniTimer += 1
        else:
            self.aniTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]
            
  
  
    def collideShip(self, other):
        if not(self == other):
            self.living = False
                                
    def update(*args):
        self = args[0]
        size = args[1]
        self.animate()
