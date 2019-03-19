from files.config import *

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
text = tl.fail_safe.get


def delay():
    global last_update2
    global z_allow
    now = pygame.time.get_ticks()
    if zed:
        if now - last_update2 > 200:
            last_update2 = now
            z_allow = True
    if not zed:
            z_allow = False


class PlayerCharacter:
    def char(self, x, y):
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

        win.blit(character, (x, y))

    def action_interaction(self):
        global show_chatbar
        global script
        global line_count
        global render_text
        global zed
        global walking

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z and not show_chatbar and not z_allow:
                show_chatbar = True
                script = text(line_count)
                render_text = script
                # Delay
                zed = True
                x_change = 0
                y_change = 0
                walking = False
            if event.key == pygame.K_z and show_chatbar and z_allow:
                line_count -= 1
                script = text(line_count)
                render_text = script
            if event.key == pygame.K_z and show_chatbar and z_allow and line_count <= 0:
                show_chatbar = False
                line_count = saved_count
                zed = False
            if event.key == pygame.K_m:
                walking = False





def hud_hp_shelf():
    win.blit(img.hp_shelf, (0, 0))
    name_text = font2.render(player_name, False, (255, 255, 255))
    win.blit(name_text, (2, 4))


def testent(x, y):
    win.blit(img.test_entity, (x, y))


def chat_text():

    global text_surface
    text_surface = font.render(render_text, True, (255, 255, 255))
    win.blit(text_surface, (10, 483))


def chatbar():
    win.blit(img.chtbar, (0, 473))
    chat_text()


def debug():
    global render_text
    global script
    global line_count
    global saved_count
    global text

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            saved_count = 1
            line_count = 1
            text = tl.text1.get
            script = text(line_count)
            render_text = script
        if event.key == pygame.K_2:
            saved_count = 1
            line_count = 1
            text = tl.text2.get
            script = text(line_count)
            render_text = script
        if event.key == pygame.K_3:
            saved_count = 2
            line_count = 2
            text = tl.text3.get
            script = text(line_count)
            render_text = script
        if event.key == pygame.K_4:
            saved_count = 3
            line_count = 3
            text = tl.text4.get
            script = text(line_count)
            render_text = script
        if event.key == pygame.K_5:
            saved_count = 9
            line_count = 9
            text = tl.text5.get
            script = text(line_count)
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
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0

    # Character
    global character
    global walking
    global direction
    global move
    global event
    global z_allow

    z_allow = False
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            debug()
    # window
            global game_display
            global isfull
            global win
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4 and not isfull:
                    isfull = True
                    win = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
                if event.key == pygame.K_F1 and isfull:
                    isfull = False
                    win = pygame.display.set_mode((display_width, display_height))
                if event.key == pygame.K_ESCAPE:
                    game_exit = True

                PlayerCharacter.action_interaction(character)

                # Left right movement
            if event.type == pygame.KEYDOWN and move:
                if event.key == pygame.K_LEFT:
                    x_change = -0.05
                    walking = True
                    direction = "left"
                    pygame.display.update()

                elif event.key == pygame.K_RIGHT:
                    x_change = 0.05
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
                    y_change = -0.05
                    walking = True
                    direction = "up"
                    pygame.display.update()

                elif event.key == pygame.K_DOWN:
                    y_change = 0.05
                    walking = True
                    direction = "down"
                    pygame.display.update()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                    walking = False

            if event.type == pygame.K_v:
                import frames.frame_4_fight

    # End group
        win.fill(black)
        x += x_change
        y += y_change
        pyupdate()
        delay()
        testent(125, 125)
        PlayerCharacter.char(character, x, y)
        hud_hp_shelf()
        pygame.display.update()
    clock.tick(30)


game_loop()
pygame.quit()
