import pygame, sys, math

class Background(pygame.sprite.Sprite):
    def __init__(self,  image):
        width = 1100
        height = 900
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.transform.scale(pygame.image.load(image), [width,height])
        self.rect = self.image.get_rect()
        self.layer = 0

    def update(*args):
        pass
