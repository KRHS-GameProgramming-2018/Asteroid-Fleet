import sys, math, pygame

class Missile():
    def __init__(self, startPos, goal):
        
        self.baseImage = pygame.image.load("PowerUps/GuidedMissile/images/rocket.move.png")
        self.image = self.baseImage
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(startPos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        
        self.living = True
        
        self.maxSpeed = speed
        self.goal = goal
        self.headTo(self.goal)
        
        
    def setPos(self, pos):
        self.rect.center = pos
        
    def headTo(self, pos):
        self.goal = pos
        self.angle = #math
        self.speedx = #math
        self.speedy = #math
        self.speed = [self.speedx, self.speedy]
        #self.rotateImage()
            
    def move(self):
        if self.goal[0]-self.maxSpeed <= self.rect.centerx <= self.goal[0]+self.maxSpeed:
            self.speedx = 0
        if self.goal[1]-self.maxSpeed <= self.rect.centery <= self.goal[1]+self.maxSpeed:
            self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
       

        
        self.lives = 1
        self.living = True
        self.kind = "Missile"
       
    
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
   
   
   
    # def collide(self, other):

        # if self.rect.right > other.rect.left:

            # if self.rect.left < other.rect.right:

                # if self.rect.top < other.rect.bottom:

                    # if self.rect.bottom > other.rect.top:

                        # if self.radius + other.radius > self.getDist(other.rect.center):

                            # self.living = False

        # return False
