import pygame, sys, math
from Ball import *
pygame.init()

clock = pygame.time.Clock()

width = 800
height = 800
size = width, height

screen = pygame.display.set_mode(size)

ball1 = Ball("ball.png", [5,5])
ball2 = Ball("ball.png", [3,3], [90,90])
ball3 = Ball("ball.png", [4,7], [300,100])
ball4 = Ball("ball.png", [7,2], [400,300])
ball5 = Ball("ball.png", [1,6], [600,100])

bgColor = 0,0,0

while True:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
            
    ball1.update(size)
    ball2.update(size)
    ball3.update(size)
    ball4.update(size)
    ball5.update(size)
    
    ball1.collide(ball2)        
    ball1.collide(ball3)        
    ball1.collide(ball4)        
    ball1.collide(ball5)   
         
    ball2.collide(ball1)
    ball2.collide(ball3)
    ball2.collide(ball4)
    ball2.collide(ball5)
    
    ball3.collide(ball1)
    ball3.collide(ball2)
    ball3.collide(ball4)
    ball3.collide(ball5)
    
    ball4.collide(ball1)
    ball4.collide(ball2)
    ball4.collide(ball3)
    ball4.collide(ball5)
    
    ball5.collide(ball1)
    ball5.collide(ball2)
    ball5.collide(ball3)
    ball5.collide(ball4)

    
    screen.fill(bgColor)
    screen.blit(ball1.image, ball1.rect)
    screen.blit(ball2.image, ball2.rect)
    screen.blit(ball3.image, ball3.rect)
    screen.blit(ball4.image, ball4.rect)
    screen.blit(ball5.image, ball5.rect)
    pygame.display.flip()
    clock.tick(60)
    print clock.get_fps()
