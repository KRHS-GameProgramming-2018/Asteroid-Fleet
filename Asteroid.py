import pygame, sys, math, random
from Ship import *
from PlayerShip import *
from Asteroid import *
from Missile import *
from HealthBar import *
from EndLine import *
from RepairKit import *
from PowerShield import *
from Boost import * 
from MissileBar import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, width, asteroids, speed = 3):
        pygame.sprite.Sprite.__init__(self, self.containers)
        files = ["Asteroid/images/Asteroid1.png",
                 "Asteroid/images/Asteroid2.png",
                 "Asteroid/images/Asteroid3.png",
                 "Asteroid/images/Asteroid4.png"]
        image = files[random.randint(0,len(files)-1)]
        
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
        
        
        
        
        
        
        self.image = pygame.transform.scale(pygame.image.load(image),[149,121])
        self.rect = self.image.get_rect(center=[random.randint(0,width),-50])
        self.speedx = 0
        self.speedy = speed #random.randint(0,2)
        self.speed = [self.speedx, self.speedy]
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.didBounceX = False
        self.didBounceY = False
        self.living = True
        self.kind = "boom"
        self.explode = False
        self.images = self.explodeImages
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.aniTimer = 0
        self.aniTimerMax = 30/10
        
        selfHitAsteroids = pygame.sprite.spritecollide(self, asteroids, False)
        if len(selfHitAsteroids) > 1:
            self.kill()

        if self.speed == 0:
            self.living = False
    
    def animate(self):
        print "yah"
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
    
    def hyperspeed(self):
        self.speedx = 0
        self.speedy = 3
        self.speed = [self.speedx, self.speedy]
    
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
            
    def update(*args):
        self = args[0]
        size = args[1]
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.bounceWall(size)
        
        if self.explode:
            self.speedy = 0
            self.animate()
           
          
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def bounceWall(self, size):
        width = size[0]
        height = size[1]
        if self.rect.bottom > height:
            if not self.didBounceY:
                self.kill()
            
    def collideAsteroid(self, other):
        if not(self == other):
            if not self.didBounceX:
                if self.speedx > 1: #right
                    if self.rect.centerx < other.rect.centerx:
                        self.speedx = -self.speedx
                        self.didBounceX = True
                if self.speedx < 1: #left
                    if self.rect.centerx > other.rect.centerx:
                        self.speedx = -self.speedx
                        self.didBounceX = True
                        
            if not self.didBounceY:
                if self.speedy > 1: #down
                    if self.rect.centery < other.rect.centery:
                        self.speedy = -self.speedy
                        self.didBounceY = True
                if self.speedy < 1: #up
                    if self.rect.centery > other.rect.centery:
                        self.speedy  = -self.speedy
                        self.didBounceY = True
                        return True
        return False
           

    def collideShip(self, other):
        if not(self == other):
			print "bro"
			self.explode = True
			print "sfsdgsdg"
			self.living = False
       
    def collideMissile(self, other):
        if not(self == other):
			self.explode = True
			self.living = False
    
