import pygame, sys, math, random
from Ship import *
from PlayerShip import *
from Asteroid import *
from Missile import *
from HealthBar import *
from EndLine import *
from RepairKit import *
from PowerShield import *
#from Boost import * 
from MissileBar import *
pygame.init()


size = width, height
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(True)

go = True
mode = "ready"

#MUSIC
startup = pygame.mixer.Sound("Ship/sounds/startup.wav") 
opening = pygame.mixer.Sound("Ship/sounds/hailtotheheroes.wav")             #hailtotheheroes from eardeer at Freesound.org
closing = pygame.mixer.Sound("Ship/sounds/powerdown.wav")                   #CP_Power_Down01.aif from stewdio2003 at Freesound.org
hit = pygame.mixer.Sound("Ship/sounds/impact.wav")                                                                          #8-bit Soft Beep Impact JapanYoshiTheGamer at Freesound.org

while go:
    asteroids = pygame.sprite.Group()
    abilities = pygame.sprite.Group()
    missiles = pygame.sprite.Group()
    screens = pygame.sprite.Group()
    HUD = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
   
    EndLine.containers = (screens, all)
    MissileBar.containers = (HUD, all)
    HealthBar.containers = (HUD, all)
    RepairKit.containers = (abilities, all)
    PowerShield.containers = (abilities, all)
    Missile.containers = (missiles, all)
    Asteroid.containers = (asteroids, all)
    Ship.containers = (all)
    PlayerShip.containers = (all)

    player1 = PlayerShip(2)
    health = HealthBar(player1.lives, [100, height - 25])
    rocket = MissileBar(player1.missiles, [1000, height - 30])
    shield = PowerShield("PowerUps/Shield/images/shield.png",[random.randint(50,width-50),(500)])
    repair = RepairKit("PowerUps/Repair Kit/images/repairkit.png",[random.randint(50,width-50),(200)])
    finishLine = EndLine("Screen Display/Background/images/greenComplete.png", startPos=[width/2,50]) 
   
    missile = None
    startimage = pygame.transform.scale(pygame.image.load("Screen Display/StartScreen/images/startscreen.png"), [width,height])
    hyperspeed = pygame.transform.scale(pygame.image.load("Asteroid/images/hyperspeed.png"), [width,height])
    deathimage = pygame.transform.scale(pygame.image.load("Screen Display/SplashScreen/images/lost.png"), [width,height])
   
    #SOUNDS
    LevelUpSound = pygame.mixer.Sound("Ship/sounds/powerup sound.wav")                  #8-bit Spaceship Startup via JapanYoshiTheGamer at Freesound.org
    launch = pygame.mixer.Sound("PowerUps/GuidedMissile/sounds/missile-launch.wav")     #missile_launch_2.wav via smcameron at Freesound.org
    victory = pygame.mixer.Sound("Ship/sounds/victorysound.wav")                        #Badass Victory via PearceWilsonKing at Freesound.org
    boomsound = pygame.mixer.Sound("Asteroid/sounds/boom.wav")
  
 
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

    while mode == "finish":
                screen.blit(finishimage, (0,0))
                for event in pygame.event.get():
                    #print event.type
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        pygame.time.delay(1000)
                        mode = "ready"
                
                pygame.display.flip()
                clock.tick(60)
   
   #----------GAME START------------------
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
        
        all.update(size)
        
        while len(asteroids) < 4:
           # print len(asteroids)
            asteroids += [Asteroid(width)]
            for asteroid in asteroids:
                for otherAsteroid in asteroids:
                    if asteroid.collideAsteroid(otherAsteroid):
                        asteroids.remove(asteroid)

        if len(asteroids)< 20:
            if random.randint(0,10) == 0:    #controls how close asteroids spawn together
                asteroids += [Asteroid(width)]
                for otherAsteroid in asteroids:
                    if asteroids[-1].collideAsteroid(otherAsteroid):
                        asteroids[-1].living = False
    
        # player1.update(size)
        # health.update(player1.lives)
        # rocket.update(player1.missiles)
        
        if player1.collideEndLine(finishLine):
            pygame.time.delay(500)
            victory.play(1);
            victory.fadeout(1200)
            finishimage = pygame.transform.scale(pygame.image.load("Screen Display/SplashScreen/images/win.png"), [width,height])
            mode = "ready2"
      
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
               # boomsound.play(1);
               # boomsound.fadeout(1000)
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
        
        #--------------------------------BLIT OBJECTS ---------------------------------
        screen.blit(bg, (0,0))
        #screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

        
        
        
        
        
        
        
        
        
        
        
        
 #------------------------SECRET MODE----------------------------------------------------------------------------       
    player1 = PlayerShip(25)   
    while mode == "ready2":
      #  pygame.init()
       # opening.play(1);
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(1000)
                mode = "secret"
                #opening.stop()
                pygame.time.delay(500)
                startup.play(1);
                startup.fadeout(2100);
        screen.blit(hyperspeed, (0,0))
        pygame.display.flip()
        clock.tick(60)    
        
     
    while mode == "secret" and player1.lives > 0:
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
                if event.key == pygame.K_a:
                    player1.go("west")
                if event.key == pygame.K_d:
                    player1.go("east")
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                if event.key == pygame.K_q:
                    pygame.quit()    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    player1.go("westU")
                if event.key == pygame.K_d:
                    player1.go("eastU")
        
        
        while len(asteroids) < 2:
           # print len(asteroids)
            asteroids += [Asteroid(width)]
            for asteroid in asteroids:
                for otherAsteroid in asteroids:
                    if asteroid.collideAsteroid(otherAsteroid):
                        asteroids.remove(asteroid)

        if len(asteroids)< 1:
            if random.randint(0,20) == 0:    #controls how close asteroids spawn together
                asteroids += [Asteroid(width)]
                for otherAsteroid in asteroids:
                    if asteroids[-1].collideAsteroid(otherAsteroid):
                        asteroids[-1].living = False
    
        # player1.update(size)
        # health.update(player1.lives)
        # rocket.update(player1.missiles)
        
        # if player1.collideEndLine(finishLine):
            # pygame.time.delay(500)
            # victory.play(1);
            # victory.fadeout(1200)
            # finishimage = pygame.transform.scale(pygame.image.load("Screen Display/SplashScreen/images/win.png"), [width,height])
            # mode = "finish"
      
        for asteroid in asteroids:
            asteroid.update(size)
            asteroid.charge(size)
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
        
        #--------------------------------BLIT OBJECTS ---------------------------------
        screen.blit(bg, (0,0))
        #screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

