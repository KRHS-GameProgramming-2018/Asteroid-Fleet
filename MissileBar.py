import pygame, sys, math, random
from Ship import *
from Missile import *
width = 1100
height = 900

class MissileBar():
    def __init__(self, health, startPos = [0,0]):
        self.images = [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/RocketBar.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/RocketBar.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/RocketBar.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/RocketBar.png"),[200,50]),
                       pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/RocketBar.png"),[200,50])]         
                        
        
        self.image = self.images[health]
        self.rect = self.image.get_rect(center=startPos)

    def update(self, health):
        self.image = self.images[health]
        
         
