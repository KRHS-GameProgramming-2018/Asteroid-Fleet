import pygame, sys, math

class Ship(pygame.sprite.Sprite):
    def __init__(self, image, speed = [1,1], startPos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
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
        boomsound = pygame.mixer.Sound("Asteroid/sounds/boom.wav") 
        LevelUpSound = pygame.mixer.Sound("Ship/sounds/powerup sound.wav")                  #8-bit Spaceship Startup via JapanYoshiTheGamer at Freesound.org
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
                    
    def update(*args):
        self = args[0]
        size = args[1]
        self.teleportX = False
        self.didBounceY = False
        self.move()
        self.bounceWall(size)            
                    
    def bounceWall(self,size):
        width = size[0]
        height = size[1]
        if self.rect.top < 0 or self.rect.bottom > height:
            if not self.didBounceY:
                self.speedy = -self.speedy
                self.didBounceY = True

    def collide(self, other):
        if not (self, other):
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
        boomsound = pygame.mixer.Sound("Asteroid/sounds/boom.wav") 
        if self.ability:
            self.ability = False
        elif other.living:
           # self.lives -= 1
            boomsound.play(1);
            boomsound.fadeout(1000)
        print self.lives
        return True


    def collideEndLine(self, other):
        mode = "finish"
        return True
        
    def collideShield(self):
        self.ability = True
        return True

    
    def collideHP(self):
        self.hyper = True
        mode = "ready2"
        return True

    def collideSlowMo(self):
        pass


    def colliderepair(self):
        if not (self):
            print "hit dude"
            player1.lives = 4
            LevelUpSound.play(1);
            LevelUpSound.fadeout(1200)
            return True
        return False 

