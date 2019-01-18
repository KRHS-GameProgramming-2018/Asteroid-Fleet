import pygame, sys, math
from Ship import *
from Asteroid import *
from Missile import *

class PlayerShip(Ship):
    def __init__(self, speed = 1, startPos=[0,0]):
        
        #Base
        self.baseImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.png"), [117,105])]
        self.imagesB = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.move.png"), [117,128])]
        Ship.__init__(self, "Ship/images/ship1.png",[0,0], startPos=[350,600])
        self.goal = [0,0]    
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = speed
        self.facing = "up"
        #Animation
        self.images = self.baseImage
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.aniTimer = 0
        self.aniTimerMax = 60/10
        
        #Health
        self.living = True
        self.lives = 4
        
        #Powerups and Abilities
        self.LaunchTimer = 0
        self.LaunchTimerMax = 60/15
        self.missiles = []
        self.launching = False
        self.shield = False
    
    def alive(self, lives):
        if self.lives <= 0:
            self.living = False
    
     # class HealthBar():
        # def __init__(self, image, startPos=[0,0]):
            # self.image = pygame.image.load(image)
            # self.rect = self.image.get_rect()
    
       
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

    # def headTo(self, pos):
        # self.goal = pos
        # if self.rect.centerx > pos[0]:
            # self.speedx = -self.maxSpeed
        # elif self.rect.centerx < pos[0]:
            # self.speedx = self.maxSpeed
        # else:
            # self.speedx = 0
            
        # if self.rect.centery > pos[1]:
            # self.speedy = -self.maxSpeed
        # elif self.rect.centery < pos[1]:
            # self.speedy = self.maxSpeed
        # else:
            # self.speedy = 0
            
        #print self.speedx, self.speedy
            
    def move(self):
        if self.goal[0]-self.maxSpeed <= self.rect.centerx <= self.goal[0]+self.maxSpeed:
            self.speedx = 0
        if self.goal[1]-self.maxSpeed <= self.rect.centery <= self.goal[1]+self.maxSpeed:
            self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    # def fireMissile(self, image, speed= [1,1], pos=[startPos]):
        # self.image = pygame.image.load("PowerUps/GuidedMissile/images/rocket.move.png")
        # self.facing = "up"
        # self.launching = False
        # self.rect = self.image.get_rect()
        # self.speedx = speed[0]
        # self.speedy = speed[1]
        # self.speed = [self.speedx, self.speedy]
        # self.rect = self.rect.move(startPos)
        # self.radius = (self.rect.width/2 + self.rect.height/2)/2
        # self.lives =1
        # self.living = True
        # if self.launching:
            # pass
        # else:
            # self.launching = True
            # self.LaunchTimer = 0
            # if self.facing == "up":
                # speed = [0,7]
                # image = "PowerUps/GuidedMissile/images/rocket.move.png"
            # return Missile(image, speed, self.rect.center)
    
    def warp(self, speed=[0,0], pos=[0,0]):
        #self.image = pygame.image.load("Ship/images/ship1.png")
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.kind = "warp"

    def teleportShip(self, size):
        width = size[0]
        height = size[1]
        x1 = self.rect.centerx
        y1 = self.rect.centery
        self.teleportX = False
        if self.rect.left < 0:      
            self.teleportX = True       
            if self.teleportX:
                print self.teleportX
                self.warp([0,0], [width-57,y1])
            else:
                self.warp([0,0], [width/2,height-59])
        
        elif self.rect.right > width:
            self.teleportX = True
            if self.teleportX:
                print self.teleportX
                self.warp([0,0], [59,y1])
            else:
                self.warp([0,0], [width/2,height-75])

    def collide(self, other):
        if not(self == other):
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.radius + other.radius > self.getDist(other.rect.center):
                                if other.kind == "Asteroid":
                                    self.lives += -1
                                    print self.lives
                                    
                                    if not self.teleportX:
                                        if self.speedx > 1: #right
                                            if self.rect.centerx < other.rect.centerx:
                                                self.speedx = -self.speedx
                                                self.teleportX = True
                                        if self.speedx < 1: #left
                                            if self.rect.centerx > other.rect.centerx:
                                                self.speedx = -self.speedx
                                                self.teleportX = True
                                                
                                    if not self.didBounceY:
                                        if self.speedy > 1: #down
                                            if self.rect.centery < other.rect.centery:
                                                self.speedy = -self.speedy
                                                self.didBounceY = True
                                        if self.speedy < 1: #up
                                            if self.rect.centery > other.rect.centery:
                                                self.speedy  = -self.speedy
                                                self.didBounceY = True

                                return True
        return False



    def update(self, size):
        Ship.update(self, size)
        self.animate()
        self.teleportX = False
        self.didBounceY = False
        self.move()
        self.alive(self.lives)
        self.bounceWall(size)
        self.animate()
        self.teleportShip(size) 
        self.kind = Asteroid  
    
