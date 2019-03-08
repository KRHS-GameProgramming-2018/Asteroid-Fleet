import pygame, sys, math, random
from Ship import *
from PlayerShip import *
from Asteroid import *
from Missile import *
from HealthBar import *
from EndLine import *
from RepairKit import *
from PowerShield import *
from Boost import * 



pygame.init()

size = width, height

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(True)


mode = "ready"
startup = pygame.mixer.Sound("Ship/sounds/startup.wav") 
go = True
opening = pygame.mixer.Sound("Ship/sounds/hailtotheheroes.wav")             #hailtotheheroes from eardeer at Freesound.org
closing = pygame.mixer.Sound("Ship/sounds/powerdown.wav")   				#CP_Power_Down01.aif  from stewdio2003 at Freesound.org
while go:
    startimage = pygame.transform.scale(pygame.image.load("Screen Display/StartScreen/images/startscreen.png"), [width,height])
    deathimage = pygame.transform.scale(pygame.image.load("Screen Display/SplashScreen/images/lost.png"), [width,height])
   #STARTSCREEN
 
    while mode == "ready":
        opening.play(1);
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(1000)
                mode = "play"
                opening.stop()
                pygame.time.delay(500)
                startup.play(1);
                startup.fadeout(2100);
        screen.blit(startimage, (0,0))
        pygame.display.flip()
        clock.tick(60)
        
    while mode == "dead":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(1000)
                mode = "ready"
        screen.blit(deathimage, (0,0))
        pygame.display.flip()
        clock.tick(60)
    
    asteroids = []
    
    missile = None
    
    finishLine = EndLine("Screen Display/Background/images/greenComplete.png", startPos=[width/2,50]) 
    player1 = PlayerShip(1)
    health = HealthBar(player1.lives, [100, height - 25])
    shield = PowerShield("PowerUps/Shield/images/shield.png",[random.randint(50,width-50),(500)])
    repair = RepairKit("PowerUps/Repair Kit/images/repairkit.png",[random.randint(50,width-50),(200)])
    
    #SOUNDS
    LevelUpSound = pygame.mixer.Sound("Ship/sounds/powerup sound.wav")                  #8-bit Spaceship Startup via JapanYoshiTheGamer at Freesound.org
    launch = pygame.mixer.Sound("PowerUps/GuidedMissile/sounds/missile-launch.wav")     #missile_launch_2.wav via smcameron at Freesound.org
    victory = pygame.mixer.Sound("Ship/sounds/victorysound.wav")                        #Badass Victory via PearceWilsonKing at Freesound.org


    while len(asteroids) < 4:
       # print len(asteroids)
        asteroids += [Asteroid(width)]
        for asteroid in asteroids:
            for otherAsteroid in asteroids:
                if asteroid.collideAsteroid(otherAsteroid):
                    asteroids.remove(asteroid)

    
    # while mode == "dead":
        # for event in pygame.event.get():
            # #print event.type
            # if event.type == pygame.QUIT:
                # sys.exit()
            # if event.type == pygame.KEYDOWN:
                # pygame.time.delay(1000)
                # mode = "play"
        # screen.blit(startimage, (0,0))
        # pygame.display.flip()
        # clock.tick(60)
    
    while mode == "play" and player1.lives > 0:
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player1.missiles > 0:
                    missile = Missile(player1.rect.center, event.pos)
                    launch.play(1);
                    launch.fadeout(1200)
                    player1.missiles -= 1
            if event.type == pygame.MOUSEMOTION:
                if missile:
                    missile.headTo(event.pos)
            
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
    
        if len(asteroids)<19:
            if random.randint(0,30) == 0:    #controls how close asteroids spawn together
                asteroids += [Asteroid(width)]
                for otherAsteroid in asteroids:
                    if asteroids[-1].collideAsteroid(otherAsteroid):
                        asteroids[-1].living = False
    
    
    
        player1.update(size)
        health.update(player1.lives)
        
    
        if player1.collideEndLine(finishLine):
            pygame.time.delay(500)
            victory.play(1);
            victory.fadeout(1200)
            finishimage = pygame.transform.scale(pygame.image.load("Screen Display/SplashScreen/images/win.png"), [width,height])
            mode = "finish"
            while mode == "finish":
                screen.blit(finishimage, (0,0))
                for event in pygame.event.get():
                    #print event.type
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        pygame.time.delay(2000)
                        mode = "ready"
                
                pygame.display.flip()
                clock.tick(60)
                
                
        for asteroid in asteroids:
            asteroid.update(size)
            if missile:
                missile.collide(asteroid)
                asteroid.collideMissile(missile)
            if shield:
               player1.collideShield(shield)
               shield.collideShip(player1)  
            if repair:
               player1.colliderepair(repair)
               repair.collideShip(player1)  
            if not asteroid.living:
                asteroids.remove(asteroid)
  
        if missile:
            missile.update()
            if not missile.living:
                missile = None      
        if shield:
            if not shield.living:
                shield = None             
        if repair:
            if player1.colliderepair(repair):
                player1.lives = 4
                LevelUpSound.play(1);
                LevelUpSound.fadeout(1200)
            if not repair.living:
                repair = None        
                
          ############  if missile.collideAsteroid:
            #   missile.remove(Missile)
        
        for hitter in asteroids:
            for hittie in asteroids:
                hitter.collideAsteroid(hittie)
            hitter.collideShip(player1)
            player1.collideAsteroid(hitter)

            
        if player1.lives == 0:
            pygame.time.delay(500)
            closing.play(1);
            closing.fadeout(3000);
            mode = "dead"
        complete = EndLine("Screen Display/Background/images/greenComplete.png", startPos=[width/2,50]) 
        bg = pygame.transform.scale(pygame.image.load("Screen Display/Background/images/space.png"), [width,height])
        screen.blit(bg, (0,0))
        
        if missile:
            screen.blit(missile.image, missile.rect)
        if shield:
            screen.blit(shield.image, shield.rect)
        if repair:
            screen.blit(repair.image, repair.rect)
        
        screen.blit(player1.image, player1.rect)
        for asteroid in asteroids:
            screen.blit(asteroid.image, asteroid.rect)
        screen.blit(health.image, health.rect)
        screen.blit(complete.image, complete.rect)

        pygame.display.flip()
        clock.tick(60)
        # print clock.get_fps()
