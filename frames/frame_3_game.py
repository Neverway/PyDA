from Divine_Annihilation import *
from files import text_lines as tl, win_config as win, img_load as img
import os
path = os.path.abspath("frames/retro.ttf")

# This is important and needs to be first
pygame.init()
pygame.font.init()
# Game font

font = pygame.font.SysFont('Courier New', 20)
font2 = pygame.font.Font(path, 12)

render_text = script
text_surface = font.render(render_text, True, (255, 255, 255))
# Variables
# Character
move = True
up = False
down = False
left = False
right = False
facing = img.char_right
character = img.char_right
walk_frame = 0
# Other
show_chatbar = False
player_name = "Dev_01"


def char(x, y):
    win.game_display.blit(character, (x, y))


def hud_hp_shelf():
    win.game_display.blit(img.hp_shelf, (0, 0))
    name_text = font2.render(player_name, False, (255, 255, 255))
    win.game_display.blit(name_text, (2, 4))


def testent(x, y):
    win.game_display.blit(img.test_entity, (x, y))


def chat_text():
    global text_surface
    text_surface = font.render(render_text, True, (255, 255, 255))
    win.game_display.blit(text_surface, (10, 483))


def chatbar():
    win.game_display.blit(img.chtbar, (0, 473))
    chat_text()


def debug():
    global render_text
    global line_count
    global script
    global default_line_count
    default_line_count = 1
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_0:
            script = tl.failsafe.get(1)
            default_line_count = 1
        if event.key == pygame.K_1:
            script = tl.text1.get(1)
            default_line_count = 1
        if event.key == pygame.K_2:
            script = tl.text2.get(1)
            default_line_count = 1
        if event.key == pygame.K_3:
            script = tl.text3.get(1)
            default_line_count = 1
        if event.key == pygame.K_4:
            script = tl.text4.get(1)
            default_line_count = 1
        if event.key == pygame.K_5:
            script = tl.text5.get(2)
            restore = 2
        if event.key == pygame.K_6:
            script = tl.text6.get(3)
            restore = 3


#######################
def pyupdate():
    global walk_frame
    global character
    global move

    if walk_frame + 1 >= 4:
        walk_frame = 0
    if up:
        walk_frame += 1
        character = (img.char_up_walk[walk_frame//3])
    if down:
        walk_frame += 1
        character = (img.char_down_walk[walk_frame//3])
    if left:
        walk_frame += 1
        character = (img.char_right_walk[walk_frame//3])
    elif right:
        walk_frame += 1
        character = (img.char_left_walk[walk_frame//3])
    else:
        character = facing
    if show_chatbar:
        chatbar()
        move = False
    if not show_chatbar:
        move = True
#######################


def game_loop():
    x = (win.display_width * 0.45)
    y = (win.display_height * 0.8)
    x_change = 0
    y_change = 0
    global up
    global down
    global left
    global right
    global walk_frame
    global character
    global facing
    global show_chatbar
    global move
    global event
    global render_text
    global line_count
    global script
    global restore

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            debug()
    # Action / Interaction
            global game_display
            global isfull
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1 and not win.isfull:
                    win.game_display = pygame.display.set_mode((win.display_width, win.display_height), pygame.FULLSCREEN)
                    win.isfull = True
                if event.key == pygame.K_ESCAPE and win.isfull:
                    win.game_display = pygame.display.set_mode((win.display_width, win.display_height))
                    win.isfull = False
                if event.key == pygame.K_F4:
                    game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and not show_chatbar:
                    show_chatbar = True
                    pygame.display.update()
                if event.key == pygame.K_x and line_count >= 1 and show_chatbar:
                    line_count -= 1
                    render_text = script
                    print(line_count)
                    if line_count == 0:
                        show_chatbar = False
                        move = False
                        line_count = restore

                if event.key == pygame.K_c:
                    print(script)
                    print(line_count)

    # Left right movement
            if event.type == pygame.KEYDOWN and move:
                if event.key == pygame.K_LEFT:
                    x_change = -0.025
                    up = False
                    down = False
                    left = False
                    right = True
                    facing = img.char_left
                    pygame.display.update()
                elif event.key == pygame.K_RIGHT:
                    x_change = 0.025
                    up = False
                    down = False
                    left = True
                    right = False
                    facing = img.char_right
                    pygame.display.update()
                else:
                    left = False
                    right = False
                    walk_frame = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    left = False
                    right = False

    # Up Down movement
            if event.type == pygame.KEYDOWN and move:
                if event.key == pygame.K_UP:
                    y_change = -0.025
                    up = True
                    down = False
                    left = False
                    right = False
                    facing = img.char_up
                    pygame.display.update()
                elif event.key == pygame.K_DOWN:
                    y_change = 0.025
                    up = False
                    down = True
                    left = False
                    right = False
                    facing = img.char_down
                    pygame.display.update()
                else:
                    up = False
                    down = False
                    walk_frame = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    up = False
                    down = False

    # End group
        win.game_display.fill(win.black)
        x += x_change
        y += y_change
        pyupdate()
        char(x, y)
        testent(15, 15)
        hud_hp_shelf()
        pygame.display.update()
    clock.tick(30)


game_loop()
pygame.quit()
quit()
