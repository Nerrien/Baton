#! python3
# Library imports
import pygame
# My imports
pygame.init()
from BatonVar import *
from BatonSprite import *

screen.fill(grey)
pygame.display.set_caption('Baton')

# Levels
level1 = open('Level 1.txt', 'r')

def game_loop():
    
    # Levels
        # Level vars
    Lines = level1.readlines()
    line = 0
    place = 0
    playerCount = 0
    posYCount = 0
    playerPlaceX = 0
    playerPlaceY = 0
        # Spawn loop
    for line in Lines:
        posXCount = 0
        for place in line:
            # Player
            if place == '@':
                spawnX = posXCount * SPACING
                spawnX = spawnX + (SPACING / 2)
                spawnY = posYCount
                spawnY = spawnY * SPACING
                spawnY = spawnY + (SPACING / 2)
                if playerCount == 0:
                    baton = Baton(green, 5, 70)
                    player = Player(magenta, spawnX, spawnY, 40, 40)
                    players.add(player)
                    batons.add(baton)
                    playerCount += 1
                    playerPlaceX = spawnX
                    playerPlaceY = spawnY
                else:
                    print ('Error, can only support 1 player.')
                spawnX = 0
                spawnY = 0
            # Charger enemy
            if place == 'C':
                spawnX = posXCount * SPACING
                spawnX = spawnX + (SPACING / 2)
                spawnY = posYCount
                spawnY = spawnY * SPACING
                spawnY = spawnY + (SPACING / 2)
                enemies.add(Charger(red, spawnX, spawnY))
                spawnX = 0
                spawnY = 0
            # Wall
            if place == '#': 
                spawnX = posXCount * SPACING
                spawnY = posYCount * SPACING
                walls.add(Wall(darkGrey, spawnX, spawnY))
                spawnX = 0
                spawnY = 0
            # Tower enemy
            if place == 'T':
                spawnX = posXCount * SPACING
                spawnY = posYCount * SPACING
                enemies.add(Tower(red, spawnX, spawnY))
                spawnX = 0
                spawnY = 0
            posXCount += 1
        posYCount += 1
        
    # Main loop
    running = True
    while running:
        # Looking through each event
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # If escape key held down, close game
                if event.key == ESCAPE:
                        running = False
                if event.type == pygame.QUIT:
                    running = False
        screen.fill(grey)

        # Sprites
            # Player
        for entity in players:
            entity.handle()
            # Baton
        for entity in batons:
            entity.draw(screen,player.rect.center[0],player.rect.center[1])
            entity.mask = pygame.mask.from_surface(entity.rotImage)
            # Enemies   
        for entity in enemies:
            entity.handle(player.rect.x,player.rect.y) # Enemy ai/blit
            # Walls
        for entity in walls:
            entity.handle()
            # Wall collision - IN PROGRESS
            if entity.rect.x - 0 < player.rect.x and entity.rect.x + 60 > player.rect.x: # if x - 1 lower than player x and x + 61 higher than player x
                if entity.rect.y - 40 < player.rect.y and entity.rect.y > player.rect.y: # if wall below player and player y 
                    player.down = 0
                elif entity.rect.y + 62 > player.rect.y and entity.rect.y < player.rect.y: # wall above player
                    player.up = 0
            elif entity.rect.y - 0 < player.rect.y and entity.rect.y + 60 > player.rect.y:
                if entity.rect.x - 40 < player.rect.x and entity.rect.x > player.rect.x: # wall right of player
                    player.right = 0
                elif entity.rect.x + 62.1 > player.rect.x and entity.rect.x < player.rect.x: # wall left of player
                    player.left = 0
                    
        for entity in eBullets:
            entity.handle(player.rect.x,player.rect.y)

        # Collision
        if pygame.sprite.spritecollide(player, enemies, pygame.sprite.collide_mask): # if player collides with enemies, close game
            running = False
        if pygame.sprite.spritecollide(player, eBullets, pygame.sprite.collide_mask): # if player collides with enemy bullets, close game
            running = False
        if pygame.sprite.spritecollide(baton, eBullets, True, pygame.sprite.collide_mask): # if baton collides with enemy bullet, kill bullet
            pass
        if pygame.sprite.spritecollide(baton, enemies, True, pygame.sprite.collide_mask): # if baton collides with enemy, kill enemy
            pass
        if not enemies: # if enemy group is empty, close game
            print ('You win! Till I add a more comprehensive victory condition.')
            running = False
            
        # Updating screen
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

