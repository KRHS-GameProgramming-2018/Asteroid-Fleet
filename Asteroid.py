# Test Jake Bender
#Different sizes/velocities/startPos(random)

import pygame, sys, math, random
from Ship import *
from PlayerShip import *
from getInputAsteroid import *
pygame.init()

clock = pygame.time.Clock()

pygame.mouse.set_visible(True)

width = 800
height = 1100
size = width, height

screen = pygame.display.set_mode(size)


player1 = PlayerShip(5, [width/2, height/2])

while True:
    for event in pygame.event.get():
        #print event.type
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                player1.
