import pygame, sys, math

class Ship():
    def __init__(self, image, speed = [1,1], startPos=[0,0]):
		
    #Essential  
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.speedx = speed[0]
        self.speedy = speed[1]
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(startPos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.living = True

    #Animation  
        self.images = self.baseImage
        self.frame = 0;
        self.maxFrame = len(self.images)-1
        self.aniTimer = 0
        self.aniTimerMax = 60/10
			
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    
    def animate(self):
        if self.aniTimer < self.aniTimerMax:
            self.aniTimer += 1
        else:
            self.aniTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
            self.image = self.images[self.frame]
    
    def alive(self, lives):
        if self.lives <= 0:
            self.living = False
   
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
                    
    def update(self, size):
        self.teleportX = False
        self.didBounceY = False
        self.move()
        self.bounceWall(size)
        #self.activateShip()             
                    
    def bounceWall(self,size):
		width = size[0]
		height = size[1]
		if self.rect.top < 0 or self.rect.bottom > height:
			if not self.didBounceY:
				self.speedy = -self.speedy
				self.didBounceY = True

    def collide(self, other):

            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.radius + other.radius > self.getDist(other.rect.center):
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
            
            
    def collideAsteroid(self, other):
        if self.rect.right > other.rect.left:
			if self.rect.left < other.rect.right:
				if self.rect.top < other.rect.bottom:
					if self.rect.bottom > other.rect.top:
						if self.radius + other.radius > self.getDist(other.rect.center):      
							self.lives -= 1
							print self.lives
                        return True
        return False

    
    def collideShield(self, other):
        if self.rect.right > other.rect.left:
			if self.rect.left < other.rect.right:
				if self.rect.top < other.rect.bottom:
					if self.rect.bottom > other.rect.top:
						if self.radius + other.radius > self.getDist(other.rect.center):      
							self.lives -= 1
							print self.lives
                        return True
        return False

