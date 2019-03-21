import pygame, sys, math, random
from PlayerShip import *
from Missile import *
width = 1100
height = 900

class MissileBar(pygame.sprite.Sprite):
    def __init__(self, missiles, startPos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/RocketBar.none.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/RocketBar.1.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/RocketBar.2.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/RocketBar.3.png"),[200,50])]  
        
        self.image = self.images[missiles]
        self.rect = self.image.get_rect(center=startPos)

    def update(self, missiles):
        self.image = self.images[missiles]
        
         
