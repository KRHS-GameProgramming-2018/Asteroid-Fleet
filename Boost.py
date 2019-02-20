import pygame, sys, math, random
from Ship import *
width = 1100
height = 900

class Boost():
    def __init__(self, image, startPos = [0,0]):
        self.image = pygame.transform.scale(pygame.image.load(image),[50,50])         #FIX THIS SIZING
        self.rect = self.image.get_rect(center = startPos)
