import sys, math, pygame

class Missile(pygame.sprite.Sprite):
    def __init__(self, startPos, goal, image, fast = False):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.baseImage = pygame.image.load(image)
        self.image = pygame.transform.rotate(self.baseImage, 0)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(startPos)
        self.angle = 0
        self.maxSpeed = 6
        if fast == True:
            self.maxSpeed = 15
        
        self.headTo(goal)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.living = True
        self.goal = goal
        self.lives = 1
        self.kind = "missile"
       
    def collideAsteroid(self, other):
        if not(self == other):
            self.living = False 

    def setPos(self, pos):
        self.rect.center = pos
        
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
    def rotateImage(self, point):
        self.living = True
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
        
        
    def update(*args):
        self = args[0]
        self.move()
        
    def headTo(self, pos):
        pointPosPlayerX = pos[0] - self.rect.center[0]
        pointPosPlayerY = pos[1] - self.rect.center[1]
        self.angle = ((math.atan2(pointPosPlayerY, pointPosPlayerX))/math.pi)*180
        self.angle = -self.angle
        self.speedx = self.maxSpeed*math.cos(math.radians(self.angle))
        self.speedy = -self.maxSpeed*math.sin(math.radians(self.angle))
        self.speed = [self.speedx, self.speedy]
        self.rotateImage(pos)
            
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
       
        
   
    
