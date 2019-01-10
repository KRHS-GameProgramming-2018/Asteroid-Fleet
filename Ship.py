import pygame, sys, math
#testing my push from home...

class Ship():
    def __init__(self, image, speed=[5,5], startPos=[0,0]):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(startPos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.didBounceX = False
        self.didBounceY = False
        #self.teleportX = False
        #self.didBounceY = False
    
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
     #   self.teleportShip(size)
    
    def move(self, warp=[0,0]):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    # def teleportShip(self, size):
        # width = size[0]
        # height = size[1]
        # if self.rect.left < 0 or self.rect.right > width:   Within edges of screen
            # if not self.teleportX:                          #if not within screen
                # self.teleportX = True
                # Ship.warp(self,[0,0])
        
    # def bounceBottom(self, size):  
        # if self.rect.bottom > height:             Within bottom of screen
            # if not self.didBounceY:               if not within bottom
                # self.speedy = -self.speedy
                # self.didBounceY = True
                
    def bounceWall(self,size):
		width = size[0]
		height = size[1]
		if self.rect.left < 0 or self.rect.right > width:
			if not self.didBounceX:
				#self.move(self,[180,100])
				self.didBounceX = True
		if self.rect.top < 0 or self.rect.bottom > height:
			if not self.didBounceY:
				self.speedy = -self.speedy
				self.didBounceY = True
    # def warp(self,  pos=[0,0]):
        # self.image = pygame.image.load("Ship/images/ship1.png")
        # self.rect = self.image.get_rect(center=pos)
        # self.radius = (self.rect.width/2 + self.rect.height/2)/2
        # self.kind = "warp"
  
  
  # class HealthBar():
    # def __init__(self, image, startPos=[0,0]):
        # self.image = pygame.image.load(image)
        # self.rect = self.image.get_rect()
 
  
  
  
  
    # def collide(self, other):
        # if not(self == other):
            # if self.rect.right > other.rect.left:
                # if self.rect.left < other.rect.right:
                    # if self.rect.top < other.rect.bottom:
                        # if self.rect.bottom > other.rect.top:
                            # if self.radius + other.radius > self.getDist(other.rect.center):
                                # if not self.didBounceX:
                                    # if self.speedx > 1: #right
                                        # if self.rect.centerx < other.rect.centerx:
                                            # self.speedx = -self.speedx
                                            # self.didBounceX = True
                                    # if self.speedx < 1: #left
                                        # if self.rect.centerx > other.rect.centerx:
                                            # self.speedx = -self.speedx
                                            # self.didBounceX = True
                                            
                                # if not self.didBounceY:
                                    # if self.speedy > 1: #down
                                        # if self.rect.centery < other.rect.centery:
                                            # self.speedy = -self.speedy
                                            # self.didBounceY = True
                                    # if self.speedy < 1: #up
                                        # if self.rect.centery > other.rect.centery:
                                            # self.speedy  = -self.speedy
                                            # self.didBounceY = True

                                # return True
        # return False
