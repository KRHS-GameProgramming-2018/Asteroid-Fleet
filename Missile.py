import sys, math, pygame
from Ship import *



class Missile(Ship):
    def __init__(self, image, speed= [1,1], startPos=[0,0]):
        self.image = pygame.image.load("PowerUps/GuidedMissile/images/rocket.move.png")
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(startPos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.lives =1
        self.living = True
        self.kind = "Missile"
        self.goal = [0,0]    
        # self.image = self.images[self.frame]
        # self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = speed
        
        #Animation
        # self.images = self.baseImage
        # self.frame = 0;
        # self.maxFrame = len(self.images)-1
        # self.aniTimer = 0
        # self.aniTimerMax = 60/10
    
    
    
    
    
    
    def setPos(self, pos):
        self.rect.center = pos
        
    def headTo(self, pos):
        self.goal = pos
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
   
    def collide(self, other):

        if self.rect.right > other.rect.left:

            if self.rect.left < other.rect.right:

                if self.rect.top < other.rect.bottom:

                    if self.rect.bottom > other.rect.top:

                        if self.radius + other.radius > self.getDist(other.rect.center):

                            self.living = False

        return False
