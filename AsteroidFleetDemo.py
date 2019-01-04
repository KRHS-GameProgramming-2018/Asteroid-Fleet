import pygame, sys, math, random
from Ship import *
from PlayerShip import *
from Asteroid import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 1100
height = 1100
size = width, height

screen = pygame.display.set_mode(size)

bgColor = 0,0,0
mposX = 0
mposY = 0

asteroids = []

for i in range(10):
    images = ["Asteroid/images/Ball.png"]
    speed = [0, random.randint(1, 9)]
    pos = [random.randint(0,690), 0]
    asteroids += [Asteroid(images[random.randint(0,0)], speed, pos)]

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
            if event.key == pygame.MOUSEBUTTONDOWN:
                player1.shoot("projectile")
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_q:
                pygame.quit()
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
    for asteroid in asteroids:
        asteroid.update(size)
    
    for asteroid in asteroids:
        if not asteroid.living:
            asteroids.remove(asteroid)
    
    screen.fill(bgColor)
    screen.blit(player1.image, player1.rect)
    for asteroid in asteroids:
        screen.blit(asteroid.image, asteroid.rect)
    pygame.display.flip()
    clock.tick(60)
    #print clock.get_fps()
    

