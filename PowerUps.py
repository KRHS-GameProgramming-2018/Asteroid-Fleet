import pygame, sys, math, random
from Ship import *
width = 1100
height = 900

class HealthBar():
    def __init__(self, image, startPos = [0,0]):
        self.images4 = [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.100%.png"),[200,50])]
        self.images3 = [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.75%.png"),[200,50])]
        self.images2 = [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.50%.png"),[200,50])]
        self.images1 = [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.25%.png"),[200,50])]
        self.images0 = [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.0%.png"),[200,50])]         
                        
        self.frame = 0;
        self.images = self.images4
        self.maxFrame = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        
        self.aniTimer = 0
        self.aniTimerMax = 60/10
       
    
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

    def shipHit(self, size):
        if Ship.lives == 3:
            self.images = self.images3
        
         
         
health = HealthBar("Screen Display/HUD/HealthBar/images/health.100%.png", startPos=[200,800])
        

class PowerShield():
    def __init__(self):
        self.living = True
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[50,50])
        self.rect = self.image.get_rect(center=[random.randint(50,width-50),(500)])

    def collideShip(self, other):
        if not(self == other):
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.radius + other.radius > self.getDist(other.rect.center):
                                self.living = False

shield = PowerShield("PowerUps/Shield/images/shield.png", startPos=[550,500])


class RepairKit():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[50,60])         #FIX THIS SIZING
        self.rect = self.image.get_rect(center = startPos)
repair = RepairKit("PowerUps/Repair Kit/images/repairkit.png", startPos=[600,200])


class Boost():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[50,50])         #FIX THIS SIZING
        self.rect = self.image.get_rect(center = startPos)
lightspeed = Boost("PowerUps/Boost/images/powerup.png", startPos=[600,600])
