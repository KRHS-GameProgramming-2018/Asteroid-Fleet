import pygame, sys, math
from Ship import *
from Asteroid import *
from Missile import *
from PowerShield import *

class PlayerShip(Ship):
    def __init__(self, speed = 1, hyper = False):
        
        #Base
        self.baseImage = pygame.transform.scale(pygame.image.load("Ship/images/ship1.png"), [117,105])
        self.baseMove = pygame.transform.scale(pygame.image.load("Ship/images/ship1.move.png"), [117,128])
        self.shieldImage = pygame.transform.scale(pygame.image.load("Ship/images/ship1.shield.png"), [142,129])
        self.shieldMoveImage = pygame.transform.scale(pygame.image.load("Ship/images/ship1.shield.move.png"), [147,138])
        self.HyperImage = pygame.transform.scale(pygame.image.load("Ship/images/ship1.powerup.png"), [117,105])
        self.HyperMoveImage = pygame.transform.scale(pygame.image.load("Ship/images/ship1.powerup.move.png"), [117,128])
        self.hitImage = pygame.transform.scale(pygame.image.load("Ship/images/broken.png"), [117,105])
        self.hitMoveImage = pygame.transform.scale(pygame.image.load("Ship/images/broken.move.png"), [117,110])
        self.miniImage = pygame.image.load("PowerUps/Shrink/images/mini.broken.png")
        self.miniMoveImage = pygame.image.load("PowerUps/Shrink/images/mini.broken.move.png")
        
        
        Ship.__init__(self, "Ship/images/ship1.png",[0,0], startPos=[350,650])
        self.goal = [0,0] 
        self.hyper = hyper   
        
        if self.hyper:
            self.image = self.HyperImage
            
        #self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.maxSpeed = speed
        #Sounds 
        self.LevelUpSound = pygame.mixer.Sound("Ship/sounds/powerup sound.wav")                  #8-bit Spaceship Startup via JapanYoshiTheGamer at Freesound.org
        self.ability = False
        self.hyper = False
        self.hit = False
        self.small = False
        self.key = False
        
        
        #Health
        self.living = True
        self.lives = 4
        print self.lives
        
        self.missiles = 3
        self.nukes = 1
        
    def alive(self, lives):
        if self.lives <= 0:
            self.living = False

    def ready(self, nukes):
        if self.nukes <= 0:
            self.living = False


    def setPos(self, pos):
        self.rect.center = pos

    def go(self, d):
        if d == "north":
            self.speedy = -self.maxSpeed
            self.image = self.baseMove
            if self.ability:
                self.image = self.shieldMoveImage
            if self.hyper:
                self.image = self.HyperMoveImage
            if self.hit:
                self.image = self.hitMoveImage
            if self.small and self.key:
                self.image = self.miniMoveImage
                
        if d == "south":
            self.speedy = self.maxSpeed
            self.image = self.baseMove
            if self.ability:
                self.image = self.shieldMoveImage
            if self.hyper:
                self.image = self.HyperMoveImage
            if self.hit:
                self.image = self.hitMoveImage
            if self.small and self.key:
                self.image = self.miniMoveImage
                
        if d == "west":
            self.speedx = -self.maxSpeed
            self.image = self.baseMove
            if self.ability:
                self.image = self.shieldMoveImage
            if self.hyper:
                self.image = self.HyperMoveImage
            if self.hit:
                self.image = self.hitMoveImage
                
            if self.small and self.key:
                self.image = self.miniMoveImage
                
        if d == "east":
            self.speedx = self.maxSpeed
            self.image = self.baseMove
            if self.ability:
                self.image = self.shieldMoveImage
            if self.hyper:
                self.image = self.HyperMoveImage
            if self.hit:
                self.image = self.hitMoveImage
                
            if self.small and self.key:
                self.image = self.miniMoveImage   
            
        if d == "northU":
            self.speedy = 0
            self.image = self.baseImage 
            if self.ability:
                self.image = self.shieldImage
            if self.hyper:
                self.image = self.HyperImage
            if self.hit:
                self.image = self.hitImage
            if self.small and self.key:
                self.image = self.miniImage
            
        if d == "southU":
            self.speedy = 0
            self.image = self.baseImage
            if self.ability:
                self.image = self.shieldImage
            if self.hyper:
                self.image = self.HyperImage
            if self.hit:
                self.image = self.hitImage
            if self.small and self.key:
                self.image = self.miniImage
            
        if d == "westU":
            self.speedx = 0
            self.image = self.baseImage
            if self.ability:
                self.image = self.shieldImage
            if self.hyper:
                self.image = self.HyperImage
            if self.hit:
                self.image = self.hitImage
            if self.small and self.key:
                self.image = self.miniImage
            
        if d == "eastU":
            self.speedx = 0
            self.image = self.baseImage
            if self.ability:
                self.image = self.shieldImage
            if self.hyper:
                self.image = self.HyperImage
            if self.hit:
                self.image = self.hitImage
            if self.small and self.key:
                self.image = self.miniImage
            
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
    
        Ship.update(self, size)
        self.rect = self.image.get_rect(center = self.rect.center)
        #self.animate()
        self.teleportX = False
        self.didBounceY = False
        self.move()
        self.alive(self.lives)
        self.bounceWall(size)
        self.teleportShip(size) 
    
        # if self.ability:
            # self.image  = self.shieldImage
            # self.image  = self.shieldMoveImage
       
            
        # if self.hyper:
            # self.image = self.HyperImage
            # self.image = self.HyperMoveImage
        
        # if self.hit:
            # self.images = self.hitImage
            # self.image = self.hitMoveImage 
        
        # if self.small:
            # self.image = self.miniImage
            # self.image = self.miniMoveImage
        
