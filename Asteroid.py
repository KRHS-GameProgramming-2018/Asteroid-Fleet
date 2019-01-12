import pygame, sys, math, random


class Asteroid():
    def __init__(self, width):
        files = ["Asteroid/images/Asteroid1.png",
             "Asteroid/images/Asteroid2.png",
             "Asteroid/images/Asteroid3.png",
             "Asteroid/images/Asteroid4.png"]
        image = files[random.randint(0,len(files)-1)]
        
        self.image = pygame.transform.scale(pygame.image.load(image),[149,121])
        self.rect = self.image.get_rect(center=[random.randint(0,width),-25])
        self.speedx = 0
        self.speedy = random.randint(1,2)
        self.speed = [self.speedx, self.speedy]
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.didBounceX = False
        self.didBounceY = False
        self.living = True
    
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
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def bounceWall(self, size):
        width = size[0]
        height = size[1]
        if self.rect.bottom > height:
            if not self.didBounceY:
                self.living = False
            
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
