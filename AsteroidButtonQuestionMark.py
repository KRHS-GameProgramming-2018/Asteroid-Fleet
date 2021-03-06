import pygame, sys, math

class Button(pygame.sprite.Sprite):
    def __init__(self, kind, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if kind == "start":
            self.basicImage = pygame.image.load("Screen Display/Buttons/startbutton.png")
            self.hoverImage = pygame.image.load("Screen Display/Buttons/startbutton2.png")
            self.clickImage = pygame.image.load("Screen Display/Buttons/startbutton3.png")
        elif kind == "hyper":
            self.basicImage = pygame.image.load("Screen Display/Buttons/HyperSpeed1.png")
            self.hoverImage = pygame.image.load("Screen Display/Buttons/HyperSpeed2.png")
            self.clickImage = pygame.image.load("Screen Display/Buttons/HyperSpeed3.png")
        self.image = self.basicImage
        self.rect = self.image.get_rect(center=pos)
        self.radius = (self.rect.width/2 + self.rect.height/2)/2
        
    def collidePt(self, pt):
        if self.rect.right > pt[0]:
            if self.rect.left < pt[0]:
                if self.rect.top < pt[1]:
                    if self.rect.bottom > pt[1]:
                        return True
        return False
        
    def checkHover(self, pt):
        print self.collidePt(pt)
        if self.collidePt(pt):
            self.image = self.hoverImage
        else:
            self.image = self.basicImage
            
    def checkClick(self, pt):
        if self.collidePt(pt):
            self.image = self.clickImage
        else:
            self.image = self.basicImage

    def update(*args):
        pass
