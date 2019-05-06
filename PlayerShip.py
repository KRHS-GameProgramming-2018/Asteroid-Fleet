import pygame, sys, math
from Ship import *
from Asteroid import *
from Missile import *
from PowerShield import *

class PlayerShip(Ship):
    def __init__(self, speed = 1, startPos=[0,0]):
        
        #Base
        self.baseImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.png"), [117,105])]
        self.baseMove = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.move.png"), [117,128])]
        self.shieldImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.shield.png"), [142,129])]
        self.shieldMoveImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.shield.move.png"), [147,138])]
        self.HyperImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.powerup.png"), [117,105])]
        self.HyperMoveImage = [pygame.transform.scale(pygame.image.load("Ship/images/ship1.powerup.move.png"), [117,128])]
        
     
     
     
        
       
        Ship.__init__(self, "Ship/images/ship1.png",[0,0], startPos=[350,650])
        self.goal = [0,0]    
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = speed
        #Sounds 
        self.LevelUpSound = pygame.mixer.Sound("Ship/sounds/powerup sound.wav")                  #8-bit Spaceship Startup via JapanYoshiTheGamer at Freesound.org
        self.ability = False
        self.hyper = False
        
        
        #Health
        self.living = True
        self.lives = 4
        print self.lives
        
        self.missiles = 3
        
    def alive(self, lives):
        if self.lives <= 0:
            self.living = False
    
    def setPos(self, pos):
        self.rect.center = pos

    def go(self, d):
        if d == "north":
            self.speedy = -self.maxSpeed
            if self.ability:
                self.images = self.shieldMoveImage
            if self.hyper:
                self.images = self.HyperMoveImage
            self.images = self.baseMove
                
        if d == "south":
            self.speedy = self.maxSpeed
            if self.ability:
                self.images = self.shieldMoveImage
            if self.hyper:
                self.images = self.HyperMoveImage
            self.images = self.baseMove
                
        if d == "west":
            self.speedx = -self.maxSpeed
            if self.ability:
                self.images = self.shieldMoveImage
            if self.hyper:
                self.images = self.HyperMoveImage
            self.images = self.baseMove
                
        if d == "east":
            self.speedx = self.maxSpeed
            if self.ability:
                self.images = self.shieldMoveImage
            if self.hyper:
                self.images = self.HyperMoveImage
            self.images = self.baseMove
            
        if d == "northU":
            self.speedy = 0
            if self.ability:
                self.images = self.shieldImage
            if self.hyper:
                self.images = self.HyperImage
            self.images = self.baseImage    
            
        if d == "southU":
            self.speedy = 0
            if self.ability:
                self.images = self.shieldImage
            if self.hyper:
                self.images = self.HyperImage
            self.images = self.baseImage
            
        if d == "westU":
            self.speedx = 0
            if self.ability:
                self.images = self.shieldImage
            if self.hyper:
                self.images = self.HyperImage
            self.images = self.baseImage
            
        if d == "eastU":
            self.speedx = 0
            if self.ability:
                self.images = self.shieldImage
            if self.hyper:
                self.images = self.HyperImage
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

    def update(*args):
        self = args[0]
        size = args[1]
    
        if self.ability:
            self.baseImage = self.shieldImage
            self.baseMove = self.shieldMoveImage
        else:
            self.baseImage = self.baseImage
            self.baseMove = self.baseMove
            
        if self.hyper:
            self.baseImage = self.HyperImage
            self.baseMove = self.HyperMoveImage
        else:
            self.baseImage = self.baseImage
            self.baseMove = self.baseMove    
            
        
        Ship.update(self, size)
        self.animate()
        self.teleportX = False
        self.didBounceY = False
        self.move()
        self.alive(self.lives)
        self.bounceWall(size)
        #self.animate()
        self.teleportShip(size) 
    
