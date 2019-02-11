import pygame, sys, math
width = 1100
height = 900

class HealthBar():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[200,50])
        self.rect = self.image.get_rect(center = startPos)
health = HealthBar("Screen Display/HUD/HealthBar/images/health.100%.png", startPos=[350,500])


class PowerShield():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[50,50])
        self.rect = self.image.get_rect(center = startPos)
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
