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
up_walk_1 = pygame.image.load('sprites/ent_char_up_walk_1.png')
up_walk_2 = pygame.image.load('sprites/ent_char_up_walk_2.png')
up_walk_3 = pygame.image.load('sprites/ent_char_up_walk_3.png')
down_walk_1 = pygame.image.load('sprites/ent_char_down_walk_1.png')
down_walk_2 = pygame.image.load('sprites/ent_char_down_walk_2.png')
down_walk_3 = pygame.image.load('sprites/ent_char_down_walk_3.png')
left_walk_1 = pygame.image.load('sprites/ent_char_left_walk_1.png')
left_walk_2 = pygame.image.load('sprites/ent_char_left_walk_2.png')
left_walk_3 = pygame.image.load('sprites/ent_char_left_walk_3.png')
right_walk_1 = pygame.image.load('sprites/ent_char_right_walk_1.png')
right_walk_2 = pygame.image.load('sprites/ent_char_right_walk_2.png')
right_walk_3 = pygame.image.load('sprites/ent_char_right_walk_3.png')
# Walk
char_left_walk = {
    1: left_walk_1,
    2: left_walk_2,
    3: left_walk_3
}
char_right_walk = {
    1: right_walk_1,
    2: right_walk_2,
    3: right_walk_3
}
char_up_walk = {
    1: up_walk_1,
    2: up_walk_2,
    3: up_walk_3
}
char_down_walk = {
    1: down_walk_1,
    2: down_walk_2,
    3: down_walk_3
}


# Hud
chtbar = pygame.image.load('sprites/hud_chatbar.png')
hp_shelf = pygame.image.load('sprites/hud_hp_shelf.png')

# Entities
test_entity = pygame.image.load('sprites/ent_testent.png')

# Fight
fight_back = pygame.image.load('sprites/back_fight_colorbar.png')
fight_char = pygame.image.load('sprites/ent_fight_char.png')
