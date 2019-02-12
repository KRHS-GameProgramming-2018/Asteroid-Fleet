import pygame, sys, math
width = 1100
height = 900

class HealthBar():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.image100 = pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.100%.png"),[200,50])
        self.image75 = pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.75%.png"),[200,50])
        self.image50 = pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.50%.png"),[200,50])
        self.image25 = pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.25%.png"),[200,50])
        self.image0 = pygame.transform.scale(pygame.image.load("Screen Display/HUD/HealthBar/images/health.0%.png"),[200,50])
        
    
    #Animation
        # self.images = self.image100
        # self.frame = 0;
        # self.maxFrame = len(self.images)-1
        # self.aniTimer = 0
        # self.aniTimerMax = 60/10
        # self.rect = self.image100.get_rect(center = startPos)
        # self.image = self.images[self.frame]
        # self.rect = self.image.get_rect(center = self.rect.center)
    # def animate(self):
        # if self.aniTimer < self.aniTimerMax:
            # self.aniTimer += 1
        # else:
            # self.aniTimer = 0
            # if self.frame < self.maxFrame:
                # self.frame += 1
            # else:
                # self.frame = 0
            # self.image = self.images[self.frame]   
   
   # def update(self, size):
	#	self.animate() 
		
        
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
