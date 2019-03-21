from files.config import *
from files.config import win

# Font
render_text2 = "Version 0.0.3"
text_surface2 = font2.render(render_text2, False, (255, 255, 255))
menu_id = 1
bar = img.new_game


def menu(x, y):
    global bar
    win.blit(bar, (x, y))
    if menu_id == 1:
        bar = img.new_game
    if menu_id == 2:
        bar = img.load_game
    if menu_id == 3:
        bar = img.quit_game


def menu_control():
    global menu_id
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
        if event.key == pygame.K_z and menu_id == 1:
                    snd.menu_select.play()
                    print("New Game")
                    import frames.frame_3_game_test
        if event.key == pygame.K_z and menu_id == 2:
                    snd.menu_select.play()
                    print("Load Game")
        if event.key == pygame.K_z and menu_id == 3:
                    snd.menu_select.play()
                    game_exit = True
        if event.key == pygame.K_c:
            pass
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
            print("none")


def debug():
    global line_count
    global script
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_0:
            line_count = 1
            script = tl.fail_safe.get(line_count)
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


def pyupdate():
    menu(350, 360)
    win.blit(text_surface2, (10, 5))
    win.blit(img.logo, (170, 250))
    win.blit(img.cright, (600, 570))


def game_loop():
    global event
    global menu_id
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            debug()
            menu_control()

    # End group
        win.fill(black)
        pyupdate()
        pygame.display.update()
    clock.tick(30)


game_loop()
pygame.quit()
quit()
