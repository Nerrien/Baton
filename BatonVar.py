import pygame

# Display settings
display_width = 1920
display_height = 1080
# RGB colour codes
black = (0,0,0)
white = (255,255,255)
green = (100,200,100)
red = (200,100,100)
blue = (100,100,200)
grey = (100,100,100)
darkGrey = (50,50,50)
magenta = (228,5,220)
# Controls
ESCAPE = pygame.K_ESCAPE
UP = pygame.K_UP
RIGHT = pygame.K_RIGHT
DOWN = pygame.K_DOWN
LEFT = pygame.K_LEFT
W = pygame.K_w
A = pygame.K_a
S = pygame.K_s
D = pygame.K_d
# Define pygame modules
screen = pygame.display.set_mode((display_width,display_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
# Map definitions
SPACING = 60
# Sprite Groups
    # Players
players = pygame.sprite.Group()
    # batons
batons = pygame.sprite.Group()
    # enemies group
enemies = pygame.sprite.Group()
    # Enemy bullets group, so I can differentiate for purposes of progress
eBullets = pygame.sprite.Group()
    # wall group
walls = pygame.sprite.Group()
# Charger definitions
C_WIDTH = 40
C_HEIGHT = C_WIDTH
# Player definitions
PWIDTH = 40
PHEIGHT = PWIDTH
# Wall definitions
W_WIDTH = SPACING
W_HEIGHT = SPACING
# Tower definitions
T_WIDTH = SPACING
T_HEIGHT = SPACING
# Bullet definitions
B_WIDTH = 15
B_HEIGHT = 15

# ---------------------------------------------------------------

