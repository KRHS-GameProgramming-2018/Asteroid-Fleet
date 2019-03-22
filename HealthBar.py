import pygame, sys, math, random
from Ship import *
width = 1100
height = 900

class HealthBar(pygame.sprite.Sprite):
    def __init__(self, health, startPos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.0%.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.25%.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.50%.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.75%.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.100%.png"),[200,50])]         
                        
        
        self.image = self.images[health]
        self.rect = self.image.get_rect(center=startPos)

    def update(self, health):
        #self.image = self.images[health]
        pass
        
         
         
        

