import pygame, sys, math
width = 1100
height = 900

class HeadsUpDisplay():
    def __init__(self, image, pos):
        self.image = pygame.transform.scale(pygame.image.load(image),[200,50])
        self.rect = self.image.get_rect()

    def setPos(self, pos):
        pos = [600,200]

HUD = HeadsUpDisplay("Screen Display/HUD/HealthBar/images/health.100%.png", pos = [600,200])




class StartScreen():
    def __init__(self, image, pos):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def setPos(self, pos):
        pos = [550,600]

Start = StartScreen("Screen Display/StartScreen/images/startscreen.png", [width, height])
 
