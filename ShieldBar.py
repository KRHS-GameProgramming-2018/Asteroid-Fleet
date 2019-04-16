import pygame, sys, math, random
from PlayerShip import *
from PowerShield import *
width = 1100
height = 900

class ShieldBar(pygame.sprite.Sprite):
    def __init__(self, protection, startPos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.images = [pygame.image.load("Screen Display/HUD/HealthBar/images/shield.full.png"),
                       pygame.image.load("Screen Display/HUD/HealthBar/images/shield.full.png")]
        
        self.image = self.images[protection]
        self.rect = self.image.get_rect(center=startPos)
     
    def update(*args):
        self = args[0]
        protection = args[4]
        self.image = self.images[protection]
