import sys, math, pygame

class Missile(pygame.sprite.Sprite):
    def __init__(self, startPos, goal):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.baseImage = pygame.image.load("PowerUps/GuidedMissile/images/rocket.move.png")
        self.explodeImages = [pygame.transform.scale(pygame.image.load("Enemy Ship/enemy1.png"),[200,200]),
                             pygame.transform.scale(pygame.image.load("Enemy Ship/enemy1.png"),[200,200]),
                             pygame.transform.scale(pygame.image.load("Enemy Ship/enemy1.png"),[200,200])]
        
        self.image = pygame.transform.rotate(self.baseImage, 0)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(startPos)
        self.angle = 0
        self.maxSpeed = 7
        self.headTo(goal)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        self.didBounceX = False
        self.didBounceY = False
        self.living = True
        self.wasliving = True
        explode = False
        self.goal = goal
        self.lives = 1
        self.kind = "missile"
        
    def collideAsteroid(self, other):
        if not(self == other):
            self.living = False 
          


    def animate(self):
        
        
        if self.aniTimer < self.aniTimerMax:
            self.aniTimer += 1
        else:
            self.aniTimer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.kill()
            self.image = self.images[self.frame]
    
    
    def setPos(self, pos):
        self.rect.center = pos
        
    def getDist(self, pt):
        x1 = self.rect.centerx
        y1 = self.rect.centery
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x2-x1)**2 + (y2-y1)**2)
        
    def rotateImage(self, point):
        rot_image = pygame.transform.rotate(self.baseImage, self.angle)
        rot_rect = self.rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect)
        self.image = rot_image
        
        
    def update(*args):
        self = args[0]
        self.move()
        if not self.living:
            self.maxSpeed = 0
            if self.wasliving:
                self.images = self.explodeImages
                self.frame = 0;
                self.maxFrame = len(self.images)-1
                self.aniTimer = 0
                self.aniTimerMax = 60/10
                self.wasliving = False
            
            self.animate()
        
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
        ready = True
        
   
    
