import pygame, sys, math

#HealthBar and Power Ups 
class HealthBar():
        def __init__(self, image, startPos=[0,0]):
            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()
    
