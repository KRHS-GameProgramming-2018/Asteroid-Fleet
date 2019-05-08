import pygame, sys, math

class Background(pygame.sprite.Sprite):
    def __init__(self, image, startPos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect(topleft = startPos)
        self.kind = "Background"
        self.speedx = 0
        self.speedy = 3

    def update(*args):
        self = args[0]
        scrolling = True
        if scrolling:
            self.move()
            if self.rect.top >= 0:
                print ">>>>>>>MOVE>>>>>>"
                self.rect.top = -2700-900
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
