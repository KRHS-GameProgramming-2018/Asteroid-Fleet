import pygame, sys, math
from Ship import *
from Asteroid import *
from Missile import *
from PowerUps import *

class PlayerShip(Ship):
    def __init__(self, speed = 1, startPos=[0,0]):
        
        #Base
        self.baseImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.png"), [117,105])]
        self.baseMove = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.move.png"), [117,128])]
        self.boostImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.powerup.png"), [117,105])]
        self.boostMoveImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.powerup.move.png"), [117,128])]
     
       
        Ship.__init__(self, "Ship/images/ship1.png",[0,0], startPos=[350,500])
        self.goal = [0,0]    
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = speed
        
        #Sounds 
        self.moveSound = pygame.mixer.Sound("Ship/sounds/shipenginesound")				#add sound.wav      #freesounds.com  jsounds2019  soundman
        self.moving = False;
        self.playingMoving = False
        
        #Health
        self.living = True
        self.lives = 4
        print self.lives
        
        #Powerups and Abilities
        self.shield = False
    
    def alive(self, lives):
        if self.lives <= 0:
            self.living = False
    
    def setPos(self, pos):
        self.rect.center = pos

    def go(self, d):
        if d == "north":
            self.speedy = -self.maxSpeed
            self.images = self.baseMove
        if d == "south":
            self.speedy = self.maxSpeed
            self.images = self.baseMove
        if d == "west":
            self.speedx = -self.maxSpeed
            self.images = self.baseMove
        if d == "east":
            self.speedx = self.maxSpeed
            self.images = self.baseMove
            
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

    def move(self):
        if self.goal[0]-self.maxSpeed <= self.rect.centerx <= self.goal[0]+self.maxSpeed:
            self.speedx = 0
        if self.goal[1]-self.maxSpeed <= self.rect.centery <= self.goal[1]+self.maxSpeed:
            self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)

    def warp(self, speed=[0,0], pos=[0,0]):
        #self.image = pygame.image.load("Ship/images/ship1.png")
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2

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

    def update(self, size):
        if self.speed != [0,0]:
            self.moving = True
        else:
            self.moving = False
        
        if self.moving and not self.playingMoving:
            self.moveSound.play(1);
            self.playingMoving = True;
        elif not self.moving and self.playingMoving:
            self.moveSound.fadeout(500);
            self.playingMoving = False;
        
        Ship.update(self, size)
        self.animate()
        self.teleportX = False
        self.didBounceY = False
        self.move()
        self.alive(self.lives)
        self.bounceWall(size)
        self.animate()
        self.teleportShip(size) 
    
