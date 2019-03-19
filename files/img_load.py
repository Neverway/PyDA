import pygame

# Load sprites
# Splash
sp0 = pygame.image.load('sprites/men_splash_logo0.png')
sp1 = pygame.image.load('sprites/men_splash_logo1.png')
sp2 = pygame.image.load('sprites/men_splash_logo2.png')
sp3 = pygame.image.load('sprites/men_splash_logo3.png')
splash = {
    1: sp0,
    2: sp1,
    3: sp2,
    4: sp3,
    5: sp3,
    6: sp3,
    7: sp2,
    8: sp1,
    9: sp0,
    10: sp0,
    11: sp0
}

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
fight_button_fight = pygame.image.load('sprites/hud_fight_button_1.png')
fight_button_act = pygame.image.load('sprites/hud_fight_button_2.png')
fight_button_inven = pygame.image.load('sprites/hud_fight_button_3.png')
fight_buttons = {
    1: fight_button_fight,
    2: fight_button_act,
    3: fight_button_inven
}


# Pause
hud_party_member_1 = pygame.image.load('sprites/hud_party_member_1.png')
hud_party_member_2 = pygame.image.load('sprites/hud_party_member_2.png')
hud_party_member_3 = pygame.image.load('sprites/hud_party_member_3.png')
hud_party_member_4 = pygame.image.load('sprites/hud_party_member_4.png')
hud_party_inven_1 = pygame.image.load('sprites/hud_party_inven_1.png')
hud_party_inven_2 = pygame.image.load('sprites/hud_party_inven_2.png')
hud_party_inven_3 = pygame.image.load('sprites/hud_party_inven_3.png')
hud_party_inven_4 = pygame.image.load('sprites/hud_party_inven_4.png')
hud_party_inven_5 = pygame.image.load('sprites/hud_party_inven_5.png')
hud_party_member = {
    1: hud_party_member_1,
    2: hud_party_member_2,
    3: hud_party_member_3,
    4: hud_party_member_4
}
hud_party_inven = {
    1: hud_party_inven_1,
    2: hud_party_inven_2,
    3: hud_party_inven_3,
    4: hud_party_inven_4,
    5: hud_party_inven_5
}

# Tutorial
cover = pygame.image.load('sprites/tut_book_read_1.png')
page0 = pygame.image.load('sprites/tut_book_read_2.png')
page1 = pygame.image.load('sprites/tut_book_read_3.png')
tut_read = {
    1: cover,
    2: page0,
    3: page1
}
