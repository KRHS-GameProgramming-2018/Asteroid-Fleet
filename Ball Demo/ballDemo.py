import pygame, sys, math, random
from Ball import *
from PlayerBall import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 800
height = 800
size = width, height

screen = pygame.display.set_mode(size)

balls = []

for i in range(25):
    images = ["Cross.png"]
    speed = [random.randint(1,10), random.randint(1,10)]
    pos = [random.randint(0,690), random.randint(0,690)]
    balls += [Ball(images[0], speed, pos)]

player1 = PlayerBall(5, [width/2, height/2])

bgColor = 0,0,0

mposX = 0
mposY = 0

while True:
    for event in pygame.event.get():
        #print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            player1.headTo(event.pos)
            
    for ball in balls:
        ball.update(size)
    player1.update(size)
        
    for hitter in balls:
        for hittie in balls:
            hitter.collide(hittie)
        hitter.collide(player1)
        player1.collide(hitter)
            

    
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player1.image, player1.rect)
    pygame.display.flip()
    clock.tick(60)
    #print clock.get_fps()
