import sys, math, pygame
from PlayerShip import *



class Missile(Ship):

    def __init__(self, image="rocket.move.png", speed=5, startPos=[0,0]):
        Ship.__init__(self,  image, speed, startPos)
        self.kind = "Missile"
        self.lives = 1
        self.goal = [0,0] 
    
    
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
