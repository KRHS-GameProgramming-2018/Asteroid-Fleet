import pygame, sys, math

class HeadsUpDisplay():
    def __init__(self, image, pos):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

    def setPos(self, pos):
        pos = [550,600]

HUD = HeadsUpDisplay("Screen Display/HUD/HealthBar/images/health.100%.png", [350,600])
