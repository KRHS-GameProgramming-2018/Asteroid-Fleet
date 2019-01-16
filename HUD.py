import pygame, sys, math

#HealthBar and Power Ups 
class GameDisplay():
        def __init__(self, image, startPos=[0,0]):
            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()
    


class Shield():
    def __init__(self, width):
        image = "PowerUps/Shield/images/shield.png"
        self.rect = self.image.get_rect(center=[random.randint(0,width),-25])
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.appear = True
    
    
    
    
    
    
    
    
    
    
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
                                            self.didBounceX = True
                                            
                                    if self.speedx < 1: #left
                                        if self.rect.centerx > other.rect.centerx:
                                            self.speedx = -self.speedx
                                            self.didBounceX = True
                                            
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
           
