import pygame, sys, math, random
from Ship import *
from PlayerShip import *
from Asteroid import *
pygame.init()

width = 1100
height = 900
size = width, height


player1 = PlayerShip(2,[200,0])
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(True)


bgColor = 0,0,0
mposX = 0
mposY = 0


asteroids = []
for i in range(5):
    asteroids += [Asteroid(width)]


while True:
    for event in pygame.event.get():
       # print event.type
        if event.type == pygame.QUIT:
            sys.exit()
        
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
            if event.key == pygame.MOUSEBUTTONDOWN:
                self.shoot()
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
        if not asteroid.living:
			asteroids.remove(asteroid)
   
        
    for hitter in asteroids:
        for hittie in asteroids:
            hitter.collide(hittie)
        hitter.collide(player1)
        player1.collide(hitter)
    
    screen.fill(bgColor)
    screen.blit(player1.image, player1.rect)
    for asteroid in asteroids:
        screen.blit(asteroid.image, asteroid.rect)
    pygame.display.flip()
    clock.tick(60)
   # print clock.get_fps()
    
