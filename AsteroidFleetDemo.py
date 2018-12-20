import pygame, sys, math, random
from Ship import *
from PlayerShip import *
#from Asteroid import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 1100
height = 1100
size = width, height

screen = pygame.display.set_mode(size)

bgColor = 100,100,100
mposX = 0
mposY = 0

for i in range(10):
    images = ["ball.png"]
    speed = [random.randint(1,10), 0]
    pos = [random.randint(0,690), 0]
    Asteroid += [Asteroid(images[random.randint(0,0)], speed, pos)]

player1 = PlayerShip(7, [width/4, height/4])

while True:
    for event in pygame.event.get():
        print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.go("north")
            if event.key == pygame.K_a:
                player1.go("west")
            if event.key == pygame.K_s:
                player1.go("south")
            if event.key == pygame.K_d:
                player1.go("east")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1.go("northU")
            if event.key == pygame.K_a:
                player1.go("westU")
            if event.key == pygame.K_s:
                player1.go("southU")
            if event.key == pygame.K_d:
                player1.go("eastU")

    
    player1.update(size)
    screen.fill(bgColor)
    screen.blit(player1.image, player1.rect)
    pygame.display.flip()
    clock.tick(60)
    #print clock.get_fps()
    

