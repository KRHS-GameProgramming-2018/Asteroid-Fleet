import pygame, sys, math
width = 1100
height = 900

class EndLine():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[width,50])
        self.rect = self.image.get_rect(center = startPos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2

    def collidePlayer(self, other):
        if not(self == other):
            if self.rect.right > other.rect.left:
                if self.rect.left < other.rect.right:
                    if self.rect.top < other.rect.bottom:
                        if self.rect.bottom > other.rect.top:
                            if self.radius + other.radius > self.getDist(other.rect.center):
                                print "yay"



