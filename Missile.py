import sys, math, pygame
from Ship import *


class Missile(Ship):
    def __init__(self, image, speed= [1,1], startPos=[0,0]):
        Ship.__init__(self, "PowerUps/GuidedMissile/images/rocket.move.png", [0,0], startPos)
        self.maxSpeed = maxSpeed
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
            
        print self.speedx, self.speedy
            
    def move(self):
        if self.goal[0]-self.maxSpeed <= self.rect.centerx <= self.goal[0]+self.maxSpeed:
            self.speedx = 0
        if self.goal[1]-self.maxSpeed <= self.rect.centery <= self.goal[1]+self.maxSpeed:
            self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
       
       
       
        # self.image = pygame.image.load("PowerUps/GuidedMissile/images/rocket.move.png")
        # self.rect = self.image.get_rect()
        # self.speedx = speed[0]
        # self.speedy = speed[1]
        # self.speed = [self.speedx, self.speedy]
        # self.rect = self.rect.move(startPos)
        # self.radius = (self.rect.width/2 + self.rect.height/2)/2
        # self.lives = 1
        # self.living = True
        # self.kind = "Missile"
        # self.goal = [0,0]    
        # # self.image = self.images[self.frame]
        # # self.rect = self.image.get_rect(center = self.rect.center)
        # self.maxSpeed = speed
        # ready = True
        # #Animation
        # # self.images = self.baseImage
        # # self.frame = 0;
        # # self.maxFrame = len(self.images)-1
        # # self.aniTimer = 0
        # # self.aniTimerMax = 60/10
        
        # self.LaunchTimer = 0
        # self.LaunchTimerMax = 60/15
        # self.missiles = []
        # self.launching = False
        
        
    # def update(self):
        # pos = pygame.mouse.get_pos()
        # x = pos[0]
        # y = pos[1]
        # self.rect.x = x
        # self.rect.y = y
   
    # # def fireMissile(self):
        # ready = True
        # if self.launching:
            # pass
        # else:
            # self.launching = True
            # self.LaunchTimer = 0
            # if ready == "True":
                # print "somethings wrong"
                # screen.blit(Missile.image, Missile.rect)
                # speed = [0,7]
                # image = "PowerUps/GuidedMissile/images/rocket.move.png" 
                # print "somethings wrong"
            # #return Missile(image, speed, self.rect.center)
   
   
   
    # def collide(self, other):

        # if self.rect.right > other.rect.left:

            # if self.rect.left < other.rect.right:

                # if self.rect.top < other.rect.bottom:

                    # if self.rect.bottom > other.rect.top:

                        # if self.radius + other.radius > self.getDist(other.rect.center):

                            # self.living = False

        # return False
