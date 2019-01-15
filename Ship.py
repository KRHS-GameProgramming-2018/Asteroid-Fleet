import pygame, sys, math

class Ship():
    def __init__(self, image, speed=[1,1], startingPos):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move([startingPos])
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.didBounceY = False
        self.teleportX = False
        self.damageShip = False
    
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
            
    def update(self, size):
        self.didBounceX = False
        self.didBounceY = False
        self.move()
        self.bounceWall(size)
        #self.activateShip()
        self.teleportShip(size)
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
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
                     
    def bounceWall(self,size):
		width = size[0]
		height = size[1]
		if self.rect.top < 0 or self.rect.bottom > height:
			if not self.didBounceY:
				self.speedy = -self.speedy
				self.didBounceY = True
                
    def warp(self, speed=[0,0], pos=[0,0]):
        #self.image = pygame.image.load("Ship/images/ship1.png")
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.kind = "warp"
  
  
    # class HealthBar():
        # def __init__(self, image, startPos=[0,0]):
            # self.image = pygame.image.load(image)
            # self.rect = self.image.get_rect()
 
    def collide(self, other):
        if not(self == other):
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.radius + other.radius > self.getDist(other.rect.center):
                                if not self.didBounceX:
                                    
                                    if self.speedx > 1: #right
                                        if self.rect.centerx < other.rect.centerx:
                                            self.speedx = -self.speedx
                                            self.damageShip = True 
                                            
                                    if self.speedx < 1: #left
                                        if self.rect.centerx > other.rect.centerx:
                                            self.speedx = -self.speedx
                                            self.damageShip = True
                                            
                                if not self.didBounceY:
                                    
                                    if self.speedy > 1: #down
                                        if self.rect.centery < other.rect.centery:
                                            self.speedy = -self.speedy
                                            self.damageShip = True
                                            
                                    if self.speedy < 1: #up
                                        if self.rect.centery > other.rect.centery:
                                            self.speedy  = -self.speedy
                                            self.damageShip = True

                                return True
        return False

   
    def asteroidcollide(self, other):
        if not(self == other):
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.radius + other.radius > self.getDist(other.rect.center):
                                if not self.didBounceX:
                                    
                                    if self.speedx > 1: #right
                                        if self.rect.centerx < other.rect.centerx:
                                            self.speedx = -self.speedx
                                            self.damageShip = True 
                                            
                                    if self.speedx < 1: #left
                                        if self.rect.centerx > other.rect.centerx:
                                            self.speedx = -self.speedx
                                            self.damageShip = True
                                            
                                if not self.didBounceY:
                                    
                                    if self.speedy > 1: #down
                                        if self.rect.centery < other.rect.centery:
                                            self.speedy = -self.speedy
                                            self.damageShip = True
                                            
                                    if self.speedy < 1: #up
                                        if self.rect.centery > other.rect.centery:
                                            self.speedy  = -self.speedy
                                            self.damageShip = True

                                return True
        return False
        
        
        
        
        
