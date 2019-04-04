from divine.run import *

# Variables
last_splash_update = 0
current_splash_frame = 0
dasplash = img.sp1

# Font
render_text2 = "Version 0.0.5"
text_surface2 = font.render(render_text2, False, (255, 255, 255))

menu_image = img.new_game


# Define functions
def splashan(display, delay):
    global last_splash_update
    global current_splash_frame
    global dasplash
    now = pygame.time.get_ticks()

    if now - last_splash_update > delay:
        last_splash_update = now
        if current_splash_frame >= 11:
            frame_2(display)
        current_splash_frame += 1
        dasplash = img.splash.get(current_splash_frame)
    display.blit(dasplash, (200, 200))


def menu(display, x, y):
    global menu_image
    global mframe
    display.blit(menu_image, (x, y))
    if mframe == 1:
        menu_image = img.new_game
    if mframe == 2:
        menu_image = img.load_game
    if mframe == 3:
        menu_image = img.quit_game


def hp_shelf(display, x, y, name):
    display.blit(img.hp_shelf, (x, y))
    text_name = font.render(name, False, (255, 255, 255))
    display.blit(text_name, (10, 5))


# Frames
def frame_1(display):
    game_exit = False
    background = pygame.Surface(display.get_size())
    background.fill((0, 0, 0))
    while not game_exit:
        for event in pygame.event.get():
            log.debug(event)
            if event.type == pygame.QUIT:
                game_exit = True
                quit()
            if event.type == pygame.KEYDOWN:
                frame_2(display)

        pygame.display.flip()
        display.blit(background, (0, 0))
        splashan(display, 500)
        clock.tick(30)


def frame_2(display):
    game_exit = False
    background = pygame.Surface(display.get_size())
    background.fill((0, 0, 0))
    while not game_exit:
        for event in pygame.event.get():
            log.debug(event)
            if event.type == pygame.QUIT:
                game_exit = True
                quit()
            if event.type == pygame.KEYDOWN:
                global mframe
                if event.key == pygame.K_UP:
                    mframe -= 1
                    pygame.display.update()
                if event.key == pygame.K_UP and mframe < 1:
                    mframe = 3
                elif event.key == pygame.K_DOWN:
                    mframe += 1
                if event.key == pygame.K_DOWN and mframe > 3:
                    mframe = 1
                    pygame.display.update()

        menu(display, 350, 360)
        display.blit(text_surface2, (10, 5))
        display.blit(img.logo, (170, 250))
        display.blit(img.cright, (600, 570))
        pressed_keys = pygame.key.get_pressed()
        Main.update(main, pressed_keys, frame_max=3, frame_min=1)
        pygame.display.flip()
        display.blit(background, (0, 0))
        clock.tick(30)


def frame_3(display):
    game_exit = False
    player = Player()
    background = pygame.Surface(display.get_size())
    background.fill((0, 0, 0))
    while not game_exit:
        for event in pygame.event.get():
            log.debug(event)
            if event.type == pygame.QUIT:
                game_exit = True
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    print("this code is functional")

                if event.key == pygame.K_b:
                    print("B pressed")

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        display.blit(player.image, player.rect)
        hp_shelf(display, 1, 1, "Dev")
        pygame.display.flip()
        display.blit(background, (0, 0))
        clock.tick(30)


def frame_4(display):
    game_exit = False
    player = Player()
    background = pygame.Surface(display.get_size())
    background.fill((0, 0, 0))
    while not game_exit:
        for event in pygame.event.get():
            log.debug(event)
            if event.type == pygame.QUIT:
                game_exit = True

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        display.blit(player.image, player.rect)
        pygame.display.flip()
        display.blit(background, (0, 0))
        clock.tick(30)
