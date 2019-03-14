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

# Character
move = True
character = img.char_right
walking = False
direction = "right"
current_frame = 0
last_update = 0
# Other
player_name = "Dev_01"

# Text
show_chatbar = False
last_update2 = 0
zed = False
line_count = 0
saved_count = 1


def delay():
    global last_update2
    global zallow
    now = pygame.time.get_ticks()
    if zed:
        if now - last_update2 > 200:
            last_update2 = now
            zallow = True
    if not zed:
            zallow = False


def char(x, y):
    global character
    global last_update
    global current_frame
    now = pygame.time.get_ticks()
    if not walking and direction == "left":
        character = img.char_left
    if not walking and direction == "right":
        character = img.char_right
    if not walking and direction == "up":
        character = img.char_up
    if not walking and direction == "down":
        character = img.char_down
    if walking:
        if now - last_update > 200:
            last_update = now
            if current_frame >= 3:
                current_frame = 0
            current_frame += 1
            if direction == "up":
                character = img.char_up_walk.get(current_frame)
            if direction == "down":
                character = img.char_down_walk.get(current_frame)
            if direction == "left":
                character = img.char_left_walk.get(current_frame)
            if direction == "right":
                character = img.char_right_walk.get(current_frame)

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
    global script
    global line_count
    global saved_count

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            saved_count = 1
            line_count = 1
            script = tl.text1.get(line_count)
            render_text = script
        if event.key == pygame.K_2:
            saved_count = 1
            line_count = 1
            script = tl.text2.get(line_count)
            render_text = script
        if event.key == pygame.K_3:
            saved_count = 2
            line_count = 2
            script = tl.text3.get(line_count)
            render_text = script


#######################
def pyupdate():
    global move

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


    # Character
    global character
    global walking
    global direction
    global move

    global event

    global render_text
    global script
    global show_chatbar
    global zed
    global zallow
    global line_count

    zallow = False

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            debug()

    # window
            global game_display
            global isfull
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and not win.isfull:
                    win.game_display = pygame.display.set_mode((win.display_width, win.display_height), pygame.FULLSCREEN)
                    win.isfull = True
                if event.key == pygame.K_F1 and win.isfull:
                    win.game_display = pygame.display.set_mode((win.display_width, win.display_height))
                    win.isfull = False
                if event.key == pygame.K_ESCAPE:
                    game_exit = True

    # Action / Interaction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and not show_chatbar and not zallow:
                    show_chatbar = True
                    print("Show the cats!")
                    # Delay
                    zed = True
                if event.key == pygame.K_z and show_chatbar and zallow:
                    line_count -= 1
                    print(line_count)
                    print("Meow.")
                if event.key == pygame.K_z and show_chatbar and zallow and line_count <= 0:
                    show_chatbar = False
                    line_count = saved_count
                    zed = False

                if event.key == pygame.K_v:
                    import frames.frame_4_fight

    # Left right movement
            if event.type == pygame.KEYDOWN and move:
                if event.key == pygame.K_LEFT:
                    x_change = -0.1
                    walking = True
                    direction = "left"
                    pygame.display.update()

                elif event.key == pygame.K_RIGHT:
                    x_change = 0.1
                    walking = True
                    direction = "right"
                    pygame.display.update()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    walking = False

    # Up Down movement
            if event.type == pygame.KEYDOWN and move:
                if event.key == pygame.K_UP:
                    y_change = -0.1
                    walking = True
                    direction = "up"
                    pygame.display.update()

                elif event.key == pygame.K_DOWN:
                    y_change = 0.1
                    walking = True
                    direction = "down"
                    pygame.display.update()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    walking = False

    # End group
        win.game_display.fill(win.black)
        x += x_change
        y += y_change
        pyupdate()
        delay()
        char(x, y)
        testent(15, 15)
        hud_hp_shelf()
        pygame.display.update()
    clock.tick(30)


game_loop()
pygame.quit()
quit()
