import pygame, sys, math, random
width = 1100
height = 900

class Countdown(pygame.sprite.Sprite):
    def __init__(self):
        currentImage = 0
        countImages = [pygame.image.load ("Screen Display/Background/images/3.png"),
                       pygame.image.load ("Screen Display/Background/images/2.png"),
                       pygame.image.load ("Screen Display/Background/images/1.png"),
                       pygame.image.load ("Screen Display/Background/images/1.png")]
        image = countImages[currentImage]
        rect = image.get_rect(center = [width/2, height/2])
        lastImage = len(countImages)-1
        print "done"
        aniTimer = 0
        aniTimerMax = 60/1
    
    def update(*args):
        self = args[0]
        size = args[1]
        
        if aniTimer < aniTimerMax:
            aniTimer += 1
        else:
            aniTimer = 0
            if currentImage < lastImage:
                currentImage += 1
            else:
                currentImage = 0
            image = countImages [currentImage]
            
        if image == countImages[3]:
            print "images changed"
            mode = "secret"
    
