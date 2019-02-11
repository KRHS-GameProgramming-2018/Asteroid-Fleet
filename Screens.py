import pygame, sys, math
width = 1100
height = 900

class HealthBar():
    
    def __init__(self, image, pos):
        self.images = [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.75%.png"), [117,105])],
        [[pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.50%.png"), [117,128])],
        [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.25%.png"), [117,105])],
        [pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.0%.png"), [117,105])]]
        self.rect = self.image.get_rect()
    self.image = pygame.transform.scale(pygame.image.load(image),[200,50])
       #Animation
        # self.images = self.baseImage
        # self.frame = 0;
        # self.maxFrame = len(self.images)-1
        # self.aniTimer = 0
        # self.aniTimerMax = 60/10




    def setPos(self, pos):
        pos = [600,200]

Health = HealthBar("Screen Display/HUD/HealthBar/images/health.100%.png", pos = [600,200])


