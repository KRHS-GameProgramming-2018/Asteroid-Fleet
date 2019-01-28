import pygame, sys, math, random
from Ship import *
from PlayerShip import *
from Asteroid import *
from Missile import *
pygame.init()

width = 1100
height = 900
size = width, height


player1 = PlayerShip(1)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(True)
missiles = []
for i in range(1):
    missiles += [Missile(width)]



bg = pygame.transform.scale(pygame.image.load("Screen Display/Background/space.png"), [width,height])
bgColor = 0,0,0
mposX = 0
mposY = 0


asteroids = []

for i in range(10):
    asteroids += [Asteroid(width)]


while True:
    for event in pygame.event.get():
       # print event.type
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            player1.fireMissile()         #headTo(event.pos)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                paused = True
                while paused:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT: sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_t:
                                paused = False
                                
            if event.key == pygame.K_w:
                player1.go("north")
            if event.key == pygame.K_a:
                player1.go("west")
            if event.key == pygame.K_s:
                player1.go("south")
            if event.key == pygame.K_d:
                player1.go("east") 
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
        
    for Asteroid in asteroids:
        Asteroid.update(size)
        if not Asteroid.living:
            asteroids.remove(Asteroid)
   
    for Missile in missiles:
        Missile.update(size)
        if not Missile.living:
            missile.remove(Missile)
        
    for hitter in asteroids:
        for hittie in asteroids:
            hitter.collide(hittie)
        hitter.collide(player1)
        player1.collide(hitter)
    
    for Missile in missiles:
        screen.blit(Missile.image, Missile.rect)
    screen.blit(bg, (0,0))
    #screen.fill(bgColor)
    screen.blit(player1.image, player1.rect)
    for asteroid in asteroids:
        screen.blit(asteroid.image, asteroid.rect)
    pygame.display.flip()
    clock.tick(60)
   # print clock.get_fps()
