import pygame
import math
from pygame.math import Vector2
import time

from BatonVar import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color, posX, posY, surfWidth, surfHeight):
        # Parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([surfWidth,surfHeight])
        self.image.fill(white)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # Movement
        self.rect.x = posX
        self.rect.y = posY
        self.up = 0
        self.right = 0
        self.down = 0
        self.left = 0
        pygame.draw.ellipse(self.image, color, [0,0,surfWidth,surfHeight]) # WHAT IS THIS? The rect frame or the position or what?
        pygame.draw.ellipse(self.image, black, [0,0,surfWidth,surfHeight], 2)
        # Player attributes
        self.speed = (display_width * 0.002)
    def handle(self):
        self.rect.y -= self.up
        self.rect.x += self.right
        self.rect.y += self.down
        self.rect.x -= self.left
        screen.blit(self.image, self.rect)
        
        # Looking through each event
        pressed = pygame.key.get_pressed()
        if pressed[W]:
            self.up = self.speed
        else:
            self.up = 0
        if pressed[D]:
            self.right = self.speed
        else:
            self.right = 0
        if pressed[S]:
            self.down = self.speed
        else:
            self.down = 0
        if pressed[A]:
            self.left = self.speed
        else:
            self.left = 0
        # slow down diagonal movement
        if pressed[UP] and pressed[RIGHT]: # up right
            self.up = self.up * 0.7
            self.right = self.right * 0.7
        if pressed[DOWN] and pressed[RIGHT]: # down right
            self.down = self.down * 0.7
            self.right = self.right * 0.7
        if pressed[DOWN] and pressed[LEFT]: # down left
            self.down = self.down * 0.7
            self.left = self.left * 0.7
        if pressed[UP] and pressed[LEFT]: # up left
            self.up = self.up * 0.7
            self.left = self.left * 0.7
        
# -----------------------------------------------------------------
class Baton(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        # Parent class (Sprite) constructor
        super().__init__()
        self.originalImage = pygame.image.load("Baton.png").convert()
        self.image = self.originalImage
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = display_width/2
        self.rect.y = display_height/2
        self.angle = 0
        self.rotImage = self.image
    def draw(self, surface, x, y):
        xSide = pygame.mouse.get_pos()[0] - x
        ySide = pygame.mouse.get_pos()[1] - y
        self.angle = math.degrees(math.atan2(xSide,ySide))
        # Offset to place on 
        x -= 5
        y -= 85
        topleft = x,y
        rotImage = pygame.transform.rotate(self.image, self.angle)
        newRect = rotImage.get_rect(center = self.image.get_rect(topleft = topleft).center)
        self.rect = newRect.topleft
        surface.blit(rotImage, newRect.topleft)
        self.rotImage = rotImage
# -----------------------------------------------------------------
class Charger(pygame.sprite.Sprite):
    def __init__(self, color, posX, posY):
        # Parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([C_WIDTH,C_HEIGHT])
        self.image.fill(white)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect() # Boundary box
        # Set original pos
        self.rect.x = posX
        self.rect.y = posY
        # Calculate vector things
        self.pos = Vector2(self.rect.center)
        # Drawing sprite
        pygame.draw.ellipse(self.image, color, [0,0,C_WIDTH,C_HEIGHT]) # Enemy shape
        pygame.draw.ellipse(self.image, black, [0,0,C_WIDTH,C_HEIGHT], 2) # Black outline
        # Charger attributes
        self.speed = (display_width * 0.001)
    def handle(self,x,y):
        self.angle = ([x + 20,y + 20] - self.pos).normalize()
        self.pos += self.angle * self.speed
        self.rect.center = self.pos
        screen.blit(self.image, self.rect)
# ----------------------------------------------------------------------------
class Wall(pygame.sprite.Sprite):
    def __init__(self, color, posX, posY):
        # Parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([W_WIDTH, W_HEIGHT]) # Make surface for image
        self.color = color
        self.image.fill(self.color) # Colour
        self.rect = self.image.get_rect() # Boundary box
        self.rect.x = posX
        self.rect.y = posY
        pygame.draw.rect(self.image, color, (0,0,W_WIDTH,W_HEIGHT)) # Create image
    def handle(self):
        screen.blit(self.image, self.rect) # Draw to screen
# ----------------------------------------------------------------------------
class Bullet(pygame.sprite.Sprite):
    def __init__(self, color, posX, posY,tX,tY):
        # Parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([B_WIDTH, B_HEIGHT])
        self.image.fill(white)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect(center=[posX,posY])
        # Set original pos
        self.rect.x = posX + 20
        self.rect.y = posY + 20
        # Calculate vector things
        self.pos = Vector2(self.rect.center)
        self.angle = ([tX + 20,tY + 20] - self.pos).normalize()
        # Drawing sprite
        pygame.draw.ellipse(self.image, color, (0,0,B_WIDTH, B_HEIGHT)) # Bullet shape
        pygame.draw.ellipse(self.image, black, (0,0,B_WIDTH, B_HEIGHT),2) # Black outline
        # Bullet attributes
        self.speed = (display_width * 0.002)
    def handle(self,x,y):
        self.pos += self.angle * self.speed
        self.rect.center = self.pos
        screen.blit(self.image, self.rect)
# ---------------------------------------------------------------------------
class Tower(pygame.sprite.Sprite):
    def __init__(self, color, posX, posY):
        # Parent class (Sprite) constructor
        super().__init__()
        self.image = pygame.Surface([T_WIDTH,T_HEIGHT])
        self.image.fill(white)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.firstShot = int(round(time.time() * 1000))
        # Set original pos
        self.rect.x = posX
        self.rect.y = posY
        # Drawing sprite
        pygame.draw.rect(self.image, color, (0,0,T_WIDTH,T_HEIGHT)) # Tower shape
        pygame.draw.rect(self.image, black, (0,0,T_WIDTH,T_HEIGHT),2) # Black outline
        pygame.draw.ellipse(self.image, color, (10,10,C_WIDTH,C_HEIGHT)) # Enemy unit shape
        pygame.draw.ellipse(self.image, black, (10,10,C_WIDTH,C_HEIGHT),2) # Black outline
    def handle(self,x,y):
        nextShot = int(round(time.time() * 1000)) - self.firstShot
        if nextShot > 1050:
            eBullets.add(Bullet(red,self.rect.x,self.rect.y,x,y))
            self.firstShot = int(round(time.time() * 1000))
        screen.blit(self.image, self.rect)
        


