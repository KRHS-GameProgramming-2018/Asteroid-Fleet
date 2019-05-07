import pygame, sys, math, random
from Ship import *
width = 1100
height = 900

class Nuke(pygame.sprite.Sprite):
    def __init__(self, image, startPos = [0,0]):
        
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(pygame.image.load(image),[50,50])
        self.rect = self.image.get_rect(center=[550,50])
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.living = True  
        self.kind = "nuke"
        self.speedx = 0
        self.speedy = 1 
        self.speed = [self.speedx, self.speedy]
        
        self.explodeImages = [pygame.transform.scale(pygame.image.load("Asteroid/images/exp1.png"), [149,121]),
							  pygame.transform.scale(pygame.image.load("Asteroid/images/exp2.png"), [149,121]),
							  pygame.transform.scale(pygame.image.load("Asteroid/images/exp3.png"), [149,121]),
							  pygame.transform.scale(pygame.image.load("Asteroid/images/exp4.png"), [149,121]),
							  pygame.transform.scale(pygame.image.load("Asteroid/images/exp5.png"), [149,121]),
							  pygame.transform.scale(pygame.image.load("Asteroid/images/exp6.png"), [149,121]),
							  pygame.transform.scale(pygame.image.load("Asteroid/images/exp7.png"), [149,121]),
							  pygame.transform.scale(pygame.image.load("Asteroid/images/exp8.png"), [149,121]),
							  pygame.transform.scale(pygame.image.load("Asteroid/images/exp9.png"), [149,121]),
							  pygame.transform.scale(pygame.image.load("Asteroid/images/exp10.png"), [149,121]),
                              pygame.transform.scale(pygame.image.load("Asteroid/images/exp11.png"), [149,121]),
							  pygame.transform.scale(pygame.image.load("Asteroid/images/exp12.png"), [149,121]),
				              pygame.transform.scale(pygame.image.load("Asteroid/images/exp13.png"), [149,121]),
                              pygame.transform.scale(pygame.image.load("Asteroid/images/exp14.png"), [149,121])]
        
        self.explode = False
        self.images = self.explodeImages
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.aniTimer = 0
        self.aniTimerMax = 30/10

        if self.speed == 0:
            self.living = False
    
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
   
   
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)  
     
                                
    def update(*args):
        self = args[0]
        size = args[1]
        self.move()
        if self.explode:
            print "im exploding!"
            self.speedy = 0
            self.animate()

