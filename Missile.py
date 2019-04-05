import sys, math, pygame

class Missile(pygame.sprite.Sprite):
    def __init__(self, startPos, goal):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.baseImage = pygame.image.load("PowerUps/GuidedMissile/images/rocket.move.png")
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
    
      
        self.goal = goal
       
       
        self.lives = 1
        self.living = True
        self.kind = "missile"

    
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
        # #Animation
        # # self.images = self.baseImage
        # # self.frame = 0;
        # # self.maxFrame = len(self.images)-1
        # # self.aniTimer = 0
        # # self.aniTimerMax = 60/10
        
        # self.LaunchTimer = 0
        # self.LaunchTimerMax = 60/15
        # self.missiles = []
        # self.launching = False
        
        
    # def update(self):
        # pos = pygame.mouse.get_pos()
        # x = pos[0]
        # y = pos[1]
        # self.rect.x = x
        # self.rect.y = y
   
    # # def fireMissile(self):
        # ready = True
        # if self.launching:
            # pass
        # else:
            # self.launching = True
            # self.LaunchTimer = 0
            # if ready == "True":
                # print "somethings wrong"
                # screen.blit(Missile.image, Missile.rect)
                # speed = [0,7]
                # image = "PowerUps/GuidedMissile/images/rocket.move.png" 
                # print "somethings wrong"
            # #return Missile(image, speed, self.rect.center)
   
