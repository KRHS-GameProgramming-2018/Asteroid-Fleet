import pygame, sys, math
width = 1100
height = 900

class EndLine():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[width,50])
        self.rect = self.image.get_rect(center = startPos)
complete = EndLine("Screen Display/Background/images/greenComplete.png", startPos=[width/2,50])


