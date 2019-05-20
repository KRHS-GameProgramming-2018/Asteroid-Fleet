import pygame, sys, math, random
from Ship import *
width = 1100
height = 900

class Nuke(pygame.sprite.Sprite):
    def __init__(self, image, startPos = [0,0]):
        
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(pygame.image.load(image),[45,120])
        self.rect = self.image.get_rect()
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.living = True  
        self.kind = "nuke"
        self.speedx = 0
        self.speedy = 0 
        self.rect = self.rect.move(startPos)
        self.speed = [self.speedx, self.speedy]
        self.drop = False
        self.detonate = 1
        if self.drop == True:
            print "INITiATING"
  
        self.explodeImages = [pygame.image.load("Asteroid/images/nukeboom1.png"), 
							  pygame.image.load("Asteroid/images/nukeboom2.png"), 
							  pygame.image.load("Asteroid/images/nukeboom3.png"), 
							  pygame.image.load("Asteroid/images/nukeboom4.png"), 
							  pygame.image.load("Asteroid/images/nukeboom5.png"), 
							  pygame.image.load("Asteroid/images/nukeboom6.png"), 
							  pygame.image.load("Asteroid/images/nukeboom7.png")]
        
        self.explode = False
        self.images = self.explodeImages
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.aniTimer = 0
        self.aniTimerMax = 60/10
      
        if self.speed == 0:
            self.living = False
   
    def go(self, d):
        if d == "drop":
            self.speedy = 3
           # self.rect = self.rect.move(self.speed)  
        if d == "hold":
            self.speedy = 0
           
        
    def animate(self):
        if self.aniTimer < self.aniTimerMax:
            self.aniTimer += 1
        else:
            self.aniTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.kill()
            self.image = self.images[self.frame]
            self.rect = self.image.get_rect(center = self.rect.center)
    
    def exploding(self):
	    pass
    
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
  
    def collideShip(self, other):
        if not(self == other):
            self.living = False
            
    def collideAsteroid(self, other):
        if not(self == other):
            self.living = False

    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)  
                    
    def update(*args):
        self = args[0]
        size = args[1]
        if self.rect.centery >= 450:
            self.detonate = 2
            self.animate()
            
        self.move()
        

