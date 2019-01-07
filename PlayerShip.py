import pygame, sys, math
from Ship import *


class PlayerShip(Ship):
    def __init__(self, maxSpeed, startPos=[0,0]):
        self.baseImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.png"), [116,105])]
        self.imagesB = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.move.png"), [116,105])]
		#self.images = [pygame.image.load
        Ship.__init__(self, "Ship/images/ship1.png", [0,0], startPos)
     
       
        self.images = self.baseImage
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.aniTimer = 0
        self.aniTimerMax = 60/10
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        
     
        
        self.maxSpeed = maxSpeed
    
        
    def setPos(self, pos):
        self.rect.center = pos

    def go(self, d):
        if d == "north":
            self.speedy = -self.maxSpeed
            self.images = self.imagesB
        if d == "south":
            self.speedy = self.maxSpeed
            self.images = self.imagesB
        if d == "west":
            self.speedx = -self.maxSpeed
            self.images = self.imagesB
        if d == "east":
            self.speedx = self.maxSpeed
            self.images = self.imagesB
            
        if d == "northU":
            self.speedy = 0
            self.images = self.baseImage
        if d == "southU":
            self.speedy = 0
            self.images = self.baseImage
        if d == "westU":
            self.speedx = 0
            self.images = self.baseImage
        if d == "eastU":
            self.speedx = 0
            self.images = self.baseImage


    def update(self, size):
        Ship.update(self, size)
        self.animate()
        
    def animate(self):
        if self.aniTimer < self.aniTimerMax:
            self.aniTimer += 1
        else:
            self.aniTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]
