import pygame, sys, math
from Ship import *


class PlayerShip(Ship):
    def __init__(self, maxSpeed, startPos=[]):
        self.baseImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.png"), [117,105])]
        self.imagesB = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.move.png"), [117,128])]
        Ship.__init__(self, "Ship/images/ship1.png", [0,0], startPos=[500,0])
        self.goal = [0,0]    
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

    def headTo(self, pos):
        self.goal = StartPos
        if self.rect.centerx > pos[0]:
            self.speedx = -self.maxSpeed
        elif self.rect.centerx < pos[0]:
            self.speedx = self.maxSpeed
        else:
            self.speedx = 0
            
        if self.rect.centery > pos[1]:
            self.speedy = -self.maxSpeed
        elif self.rect.centery < pos[1]:
            self.speedy = self.maxSpeed
        else:
            self.speedy = 0
            
        #print self.speedx, self.speedy
            
    def move(self):
        if self.goal[0]-self.maxSpeed <= self.rect.centerx <= self.goal[0]+self.maxSpeed:
            self.speedx = 0
        if self.goal[1]-self.maxSpeed <= self.rect.centery <= self.goal[1]+self.maxSpeed:
            self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
