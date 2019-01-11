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
            

