from Divine_Annihilation import *
from files import text_lines as tl, win_config as win, img_load as img

# This is important and needs to be first
pygame.init()
pygame.font.init()
# Font
render_text2 = "Version 0.0.1"
font = pygame.font.SysFont('Courier New', 20)
text_surface2 = font.render(render_text2, True, (255, 255, 255))

menu_id = 1

bar = img.new_game


def menu(x, y):
    global bar
    win.game_display.blit(bar, (x, y))
    if menu_id == 1:
        bar = img.new_game
    if menu_id == 2:
        bar = img.load_game
    if menu_id == 3:
        bar = img.quit_game


def debug():
    global line_count
    global script
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_0:
            line_count = 1
            script = tl.failsafe.get(line_count)
        if event.key == pygame.K_1:
            line_count = 1
            script = tl.text1.get(line_count)
        if event.key == pygame.K_2:
            line_count = 1
            script = tl.text2.get(line_count)
        if event.key == pygame.K_3:
            line_count = 1
            script = tl.text3.get(line_count)
        if event.key == pygame.K_4:
            line_count = 1
            script = tl.text4.get(line_count)
        if event.key == pygame.K_5:
            line_count = 2
            script = tl.text5.get(line_count)
        if event.key == pygame.K_6:
            line_count = 3
            script = tl.text6.get(line_count)


#######################
def pyupdate():
    menu(350, 360)
    win.game_display.blit(text_surface2, (10, 5))
    win.game_display.blit(img.logo, (170, 250))
    win.game_display.blit(img.cright, (600, 570))
#######################


def game_loop():
    global event
    global menu_id
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            debug()
    # Action / Interaction
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and menu_id == 1:
                    print("New Game")
                    from frames import frame_3_game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and menu_id == 2:
                    print("Load Game")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and menu_id == 3:
                    game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    print(menu_id)

    # Up Down movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menu_id -= 1
                    pygame.display.update()
                if event.key == pygame.K_UP and menu_id < 1:
                    menu_id = 3
                elif event.key == pygame.K_DOWN:
                    menu_id += 1
                if event.key == pygame.K_DOWN and menu_id > 3:
                    menu_id = 1
                    pygame.display.update()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    pass

    # End group
        win.game_display.fill(win.black)
        pyupdate()
        pygame.display.update()
    clock.tick(30)


game_loop()
pygame.quit()
quit()
