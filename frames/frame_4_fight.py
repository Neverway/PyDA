from files.config import *

player_name = "Dev_1"
tl = tl
img = img
render_text2 = "An enemy draws near!"
main_buttons = True
current_button = 1


def hud_hp_shelf():
    win.blit(img.hp_shelf, (0, 0))
    name_text = font2.render(player_name, False, (255, 255, 255))
    win.blit(name_text, (2, 4))


def chat_text():
    global text_surface
    text_surface = font3.render(render_text2, False, (255, 255, 255))
    win.blit(text_surface, (10, 483))


def chatbar():
    global current_button
    win.blit(img.chtbar, (0, 473))
    fight_button = img.fight_buttons.get(current_button)
    win.blit(img.fight_buttons.get(current_button), (0, 445))
    chat_text()


def char(x, y):
    win.blit(img.fight_char, (x, y))


def debug():
    pass


#######################
def pyupdate():
    chatbar()
    char(15, 200)
    hud_hp_shelf()
#######################


def game_loop():
    game_exit = False
    global event
    global current_button
    fdx = 0
    fdxmv = True
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and main_buttons:
                    current_button += 1
                    if current_button == 4:
                        current_button = 1
                    fight_button = img.fight_buttons.get(current_button)
                    win.blit(img.fight_buttons.get(current_button), (0, 445))
                if event.key == pygame.K_LEFT and main_buttons:
                    current_button -= 1
                    if current_button == 0:
                        current_button = 3
                    fight_button = img.fight_buttons.get(current_button)
                    win.blit(img.fight_buttons.get(current_button), (0, 445))
                if event.key == pygame.K_b:
                    print(current_button)
            debug()


    # End group
        win.fill(black)
        win.blit(img.fight_back, (fdx, 200))
        if fdxmv:
            fdx -= 0.05
        if not fdxmv:
            fdx += 0.05
        if fdx <= -500:
            fdxmv = False
        if fdx >= 1:
            fdxmv = True
        pyupdate()
        pygame.display.update()
    clock.tick(30)


game_loop()
pygame.quit()
quit()
