import pygame, sys, math, random
from Ship import *
from PlayerShip import *
from Asteroid import *
from Missile import *
from HealthBar import *
from EndLine import *
from RepairKit import *
from PowerShield import *
from Background import *
from MissileBar import *
#from ShieldBar import *
from Hyperspeed import *
pygame.init()

width = 1100
height = 900
size = width, height
clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.mouse.set_visible(True)

go = True
mode = "ready"
#-----------------MUSIC---------------------  
startup = pygame.mixer.Sound("Ship/sounds/startup.wav") 
opening = pygame.mixer.Sound("Ship/sounds/hailtotheheroes.wav")             #hailtotheheroes from eardeer at Freesound.org
closing = pygame.mixer.Sound("Ship/sounds/powerdown.wav")                   #CP_Power_Down01.aif from stewdio2003 at Freesound.org
hit = pygame.mixer.Sound("Ship/sounds/impact.wav")                          #8-bit Soft Beep Impact JapanYoshiTheGamer at Freesound.org
hyperspeed = pygame.mixer.Sound("SplashScreen/sounds/hyper-speed.wav")

asteroids = pygame.sprite.Group()
abilities = pygame.sprite.Group()
missiles = pygame.sprite.Group()
limits = pygame.sprite.Group()
HUD = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Background.containers = (backgrounds, all)
PlayerShip.containers = (all)
Ship.containers = (all)
Asteroid.containers = (asteroids, all)
Missile.containers = (missiles, all)
PowerShield.containers = (abilities, all)
RepairKit.containers = (abilities, all)
EndLine.containers = (limits, all)
MissileBar.containers = (HUD, all)
#ShieldBar.containers = (HUD, all)
HealthBar.containers = (HUD, all)
Hyperspeed.containers = (abilities, all)

while go:
    #SOUNDS----------------NEEDS TO BE MOVED TO OBJECT FILES?
    LevelUpSound = pygame.mixer.Sound("Ship/sounds/powerup sound.wav")                  #8-bit Spaceship Startup via JapanYoshiTheGamer at Freesound.org
    launch = pygame.mixer.Sound("PowerUps/GuidedMissile/sounds/missile-launch.wav")     #missile_launch_2.wav via smcameron at Freesound.org
    victory = pygame.mixer.Sound("Ship/sounds/victorysound.wav")                        #Badass Victory via PearceWilsonKing at Freesound.org
    boomsound = pygame.mixer.Sound("Asteroid/sounds/boom.wav")
    repairkitpickup = pygame.mixer.Sound("PowerUps/RepairKit/sounds/repair-kit.wav")
  
    #------------setup---------------------------
    bg = Background("Screen Display/StartScreen/images/startscreen.png")
   
    
 #---------START SCREEN-----------------------------
    while mode == "ready":
        opening.play(1);
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(1000)
                mode = "play"
               # print mode
                opening.stop()
                pygame.time.delay(500)
                startup.play(1)
                startup.fadeout(2100)
        dirty = all.draw(screen)
        for s in all.sprites():
            s.kill()
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        
  #-----GAME SETUP-------------
    bg.kill()
    bg = Background("Screen Display/Background/images/space.png")
    player1 = PlayerShip(2)
    missile = None
    PowerShield("PowerUps/Shield/images/shield.png",[random.randint(50,width-50),(500)])
    RepairKit("PowerUps/RepairKit/images/repairkit.png",[random.randint(50,width-50),(200)])
    EndLine("Screen Display/Background/images/greenComplete.png", startPos=[width/2,50]) 
    MissileBar(player1.missiles, [1000, height - 30])
    #ShieldBar(PowerShield, [1000, height - 80])
    HealthBar(player1.lives, [100, height - 25])
    Hyperspeed("PowerUps/Boost/images/powerup.png",[random.randint(50,width-50),(200)])
   
   
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
        
        all.update(size, player1.lives, player1.missiles)
        
   #-----------------------------------------------------------------------
        playerHitAsteroids = pygame.sprite.spritecollide(player1, asteroids, True, False) #Boolean checks if object should be killed upon collision
        playerHitAbilities = pygame.sprite.spritecollide(player1, abilities, True)
        playerHitLimits = pygame.sprite.spritecollide(player1, limits, True, False)
      
        
        asteroidsHitAsteroids = pygame.sprite.groupcollide(asteroids, asteroids, False, False)
        
        missilesHitAsteroids = pygame.sprite.groupcollide(missiles, asteroids, True, False)
        
        
        while len(asteroids.sprites()) < 5:
          #  print len(asteroids.sprites())
            print len(asteroids.sprites())
            Asteroid(width, asteroids    )
            # for asteroid in asteroidsHitAsteroids :
                # for otherasteroid in asteroidsHitAsteroids[asteroid]:
                    # if asteroid.collideAsteroid(otherasteroid):
                        # otherasteroid.kill()

        if len(asteroids.sprites())< 22:
            if random.randint(0,10) == 0:    #controls how close asteroids spawn together
                Asteroid(width,asteroids)
                #asteroidsHitAsteroids = pygame.sprite.groupcollide(asteroids, asteroids, True, False)

        for ability in playerHitAbilities:
            if ability.kind == "repair":
                player1.lives = 4
                repairkitpickup.play(1);
                repairkitpickup.fadeout(1200)
            if ability.kind == "shield":
                player1.collideShield()
                repairkitpickup.play(1);
                repairkitpickup.fadeout(1200)
            if ability.kind == "hype":
                player1.collideHP()
                mode = "ready2"
                for s in all.sprites():
                    s.kill()
          
        for asteroid in playerHitAsteroids:
			player1.collideAsteroid(asteroid)    # While exploding collision still takes place, talk to spooner about way to solve
			asteroid.collideShip(player1)   	# no explosion detected in code... asteroid collision must be checked 
        
        for missile in missilesHitAsteroids:
            for asteroid in missilesHitAsteroids[missile]:
                missile.collideAsteroid(asteroid)
                asteroid.collideMissile(missile)
           
        
        for limit in playerHitLimits:
             player1.collideEndLine(limit)
             mode = "finish"
             for s in all.sprites():
                 s.kill()
   #--------------------------------------------------------------------------
   

        if player1.lives == 0:
            pygame.time.delay(500)
            closing.play(1);
            closing.fadeout(3000);
            mode = "dead"
            for s in all.sprites():
                s.kill()
                
        #--------------------------------BLIT OBJECTS ---------------------------------
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        #print clock.get_fps()
       
       
       
       
    bg.kill()
    bg = Background("Screen Display/SplashScreen/images/lost.png")
    while mode == "dead":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(1000)
                mode = "ready"
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)


    bg.kill()
    bg = Background("Screen Display/SplashScreen/images/win.png")
    
    while mode == "finish":
        for event in pygame.event.get():
            #print event.type
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(1000)
                mode = "ready"  #ready2
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)



#######################COUNTDOWN#####
    bg.kill()
    bg = Background("Screen Display/Background/images/space.png")
    while mode == "countdown":
        currentImage = 0
        countImages = [pygame.image.load ("Screen Display/Background/images/3.png"),
                       pygame.image.load ("Screen Display/Background/images/2.png"),
                       pygame.image.load ("Screen Display/Background/images/1.png"),
                       pygame.image.load ("Screen Display/Background/images/1.png")]
        image = countImages[currentImage]
        rect = image.get_rect(center = [width/2, height/2])
        lastImage = len(countImages)-1
    
        aniTimer = 0
        aniTimerMax = 60/1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
      
        if aniTimer < aniTimerMax:
            aniTimer += 1
        else:
            aniTimer = 0
            if currentImage < lastImage:
                print "count me"
                currentImage += 1
            else:
                currentImage = 0
            countimage = countimages [currentImage]
            
        if image == countImages[3]:
            mode = "secret"
            
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)


 #------------------------SECRET MODE----------------------------------------------------------------------------       
 #---------------------------------------------------------------------------------------------------------------  
   
   
    bg.kill()
    bg = Background("Screen Display/SplashScreen/images/hyperspeed.png")
    while mode == "ready2":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pygame.time.delay(1000)
                mode = "countdown"
                pygame.time.delay(500)
                startup.play(1);
                startup.fadeout(2100);
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)   
        
    bg.kill()
    bg = Background("Screen Display/Background/images/space.png")
    player1 = PlayerShip(25)
    MissileBar(player1.missiles, [1000, height - 30])
    HealthBar(player1.lives, [100, height - 25])
   
    
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
                if event.key == pygame.K_w:
                    player1.go("northU")
                if event.key == pygame.K_a:
                    player1.go("westU")
                if event.key == pygame.K_s:
                    player1.go("southU")
                if event.key == pygame.K_d:
                    player1.go("eastU")
        
        all.update(size, player1.lives, player1.missiles)
        
   #-----------------------------------------------------------------------
        playerHitAsteroids = pygame.sprite.spritecollide(player1, asteroids, True) #Boolean checks if object should be killed upon collision
        playerHitAbilities = pygame.sprite.spritecollide(player1, abilities, True)
        playerHitLimits = pygame.sprite.spritecollide(player1, limits, True, False)
        
        
        asteroidsHitAsteroids = pygame.sprite.groupcollide(asteroids, asteroids, False, False)
        
        missilesHitAsteroids = pygame.sprite.groupcollide(missiles, asteroids, True, True)
        
        
        while len(asteroids.sprites()) < 3:
          #  print len(asteroids.sprites())
            print len(asteroids.sprites())
            Asteroid(width, asteroids, 25)

        if len(asteroids.sprites())< 3 :
            if random.randint(0,50) == 0:    #controls how close asteroids spawn together
                Asteroid(width,asteroids, 25)
            
        for ability in playerHitAbilities:
            if ability.kind == "repair":
                player1.lives = 4
                LevelUpSound.play(1);
                LevelUpSound.fadeout(1200)
            if ability.kind == "shield":
                player1.collideShield()
                LevelUpSound.play(1);
                LevelUpSound.fadeout(1200)
                
        # for modes in playerHitModes:
            # if modes.kind == "hype":
                # mode = "ready2"
                # for s in all.sprites():
                 # s.kill()
          
        for asteroid in playerHitAsteroids:
            player1.collideAsteroid(asteroid)    
        
        
        for missile in missilesHitAsteroids:
            for asteroid in missilesHitAsteroids[missile]:
                missile.collideAsteroid(asteroid)
                asteroid.collideMissile(missile)
         
        if player1.lives == 0:
            pygame.time.delay(500)
            closing.play(1);
            closing.fadeout(3000);
            mode = "dead"

        #--------------------------------BLIT OBJECTS ---------------------------------
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)

