import pygame

# Load sprites
# Splash
splash = pygame.image.load('sprites/men_splash_logo.png')

# Main Menu
new_game = pygame.image.load('sprites/men_main_1new.png')
load_game = pygame.image.load('sprites/men_main_2load.png')
quit_game = pygame.image.load('sprites/men_main_3quit.png')
logo = pygame.image.load('sprites/men_main_logo.png')
cright = pygame.image.load('sprites/men_main_copyright.png')

# Character
char_up = pygame.image.load('sprites/ent_char_up.png')
char_down = pygame.image.load('sprites/ent_char_down.png')
char_left = pygame.image.load('sprites/ent_char_left.png')
char_right = pygame.image.load('sprites/ent_char_right.png')
char_up_walk = [pygame.image.load('sprites/ent_char_up_walk_1.png'), pygame.image.load('sprites/ent_char_up_walk_2.png'), pygame.image.load('sprites/ent_char_up_walk_3.png'), ]
char_down_walk = [pygame.image.load('sprites/ent_char_down_walk_1.png'), pygame.image.load('sprites/ent_char_down_walk_2.png'), pygame.image.load('sprites/ent_char_down_walk_3.png'), ]
char_left_walk = [pygame.image.load('sprites/ent_char_left_walk_1.png'), pygame.image.load('sprites/ent_char_left_walk_2.png'), pygame.image.load('sprites/ent_char_left_walk_3.png'), ]
char_right_walk = [pygame.image.load('sprites/ent_char_right_walk_1.png'), pygame.image.load('sprites/ent_char_right_walk_2.png'), pygame.image.load('sprites/ent_char_right_walk_3.png'), ]

# Hud
chtbar = pygame.image.load('sprites/hud_chatbar.png')
hp_shelf = pygame.image.load('sprites/hud_hp_shelf.png')

# Entities
test_entity = pygame.image.load('sprites/ent_testent.png')
