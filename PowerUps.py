import pygame, sys, math, random
from Ship import *
width = 1100
height = 900

class HealthBar():
    def __init__(self, health, startPos = [0,0]):
        self.images = [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.0%.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.25%.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.50%.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.75%.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.100%.png"),[200,50])]         
                        
        
        self.image = self.images[health]
        self.rect = self.image.get_rect(center=startPos)

    def update(self, health):
        self.image = self.images[health]
        
         
         
        

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



class RepairKit():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[50,60])         #FIX THIS SIZING
        self.rect = self.image.get_rect(center = startPos)


class Boost():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[50,50])         #FIX THIS SIZING
        self.rect = self.image.get_rect(center = startPos)
